import sqlite3


def print_results():
    conn = sqlite3.connect('benchmarks.db')
    cursor = conn.cursor()

    print("\nBenchmark Summary:")
    print("-" * 80)

    cursor.execute("""
        SELECT b.name, b.category, r.timestamp, r.execution_time, r.output
        FROM benchmarks b
        JOIN results r ON b.id = r.benchmark_id
        ORDER BY r.timestamp DESC
    """)

    rows = cursor.fetchall()
    for row in rows:
        name, category, timestamp, execution_time, output = row
        print(f"\nBenchmark: {name}")
        print(f"Category: {category}")
        print(f"Timestamp: {timestamp}")
        print(f"Execution Time: {execution_time:.6f} seconds")
        print(f"Output: {output}")
        print("-" * 80)

    conn.close()


if __name__ == "__main__":
    print_results()
