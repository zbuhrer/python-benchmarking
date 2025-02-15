import sqlite3


def init_database():
    conn = sqlite3.connect('benchmarks.db')
    cursor = conn.cursor()

    # Create benchmarks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS benchmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        script_path TEXT NOT NULL
    )
    ''')

    # Create results table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        benchmark_id INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        execution_time REAL NOT NULL,
        output TEXT,
        FOREIGN KEY (benchmark_id) REFERENCES benchmarks (id)
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_database()
