import sqlite3
import subprocess
import os


DATABASE_PATH = 'benchmarks.db'
BENCHMARKS_DIR = 'benchmarks'


def create_connection():
    """Creates a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print(f"Connected to SQLite version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)

    return conn


def insert_benchmark(conn, name, category, description, script_path):
    """Inserts a benchmark into the benchmarks table."""
    try:
        sql = '''INSERT INTO benchmarks(name, category, description, script_path)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (name, category, description, script_path))
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting benchmark: {e}")
        return None


def insert_result(conn, benchmark_id, execution_time, output):
    """Inserts a benchmark result into the results table."""
    sql = '''INSERT INTO results(benchmark_id, execution_time, output)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (benchmark_id, execution_time, output))
    conn.commit()
    return cur.lastrowid


def run_benchmark(script_path):
    """Runs a benchmark script and returns the output."""
    try:
        process = subprocess.run(
            ['python3', script_path], capture_output=True, text=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running benchmark {script_path}: {e}")
        return None


def parse_benchmark_output(output):
    """Parses the benchmark output and extracts the results."""
    results = []
    lines = output.splitlines()

    # Skip header lines
    data_lines = [line.strip() for line in lines if line.strip()
                  and not line.startswith(('-', 'Benchmarking', 'Size'))]

    for line in data_lines:
        try:
            parts = line.split()
            if len(parts) >= 4:
                results.append({
                    'Size': int(parts[0]),
                    'List (s)': float(parts[1]),
                    'Tuple (s)': float(parts[2]),
                    'Ratio': float(parts[3].replace('x', ''))
                })
        except (ValueError, IndexError) as e:
            print(f"Warning: Could not parse line: {line} - {e}")
            continue

    return results


def find_benchmark_scripts(benchmarks_dir):
    """Finds all benchmark scripts in the specified directory."""
    scripts = []
    for root, _, files in os.walk(benchmarks_dir):
        for file in files:
            if file.endswith('.py'):
                scripts.append(os.path.join(root, file))
    return scripts


if __name__ == '__main__':
    conn = create_connection()
    if conn:
        scripts = find_benchmark_scripts(BENCHMARKS_DIR)
        for script in scripts:
            print(f"Running benchmark: {script}")
            output = run_benchmark(script)
            if output:
                # Extract the benchmark name and category from the script path
                parts = script.split(os.sep)
                if len(parts) >= 3:
                    category = parts[1]
                    name = parts[-1].replace('.py', '')
                else:
                    category = 'Unknown'
                    name = script  # Use the full path as the name if parsing fails

                # Insert benchmark metadata into the database
                benchmark_id = insert_benchmark(
                    conn, name, category, "", script)

                # Parse the output and insert the results into the database
                results = parse_benchmark_output(output)
                for result in results:
                    # Average execution time
                    execution_time = (
                        result['List (s)'] + result['Tuple (s)']) / 2
                    insert_result(conn, benchmark_id,
                                  execution_time, str(result))

        conn.close()
        print("Benchmarks completed and results stored in the database.")
