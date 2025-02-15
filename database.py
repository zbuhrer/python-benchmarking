import sqlite3

def create_connection():
    """Creates a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect('benchmarks.db')
        print(f"Connected to SQLite version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)

    return conn

def create_tables(conn):
    """Creates the tables for storing benchmark data."""
    try:
        cursor = conn.cursor()

        # Table to store benchmark metadata
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS benchmarks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                description TEXT,
                script_path TEXT UNIQUE NOT NULL
            )
        """)

        # Table to store individual benchmark run results
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                benchmark_id INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                execution_time REAL,
                output TEXT,
                FOREIGN KEY (benchmark_id) REFERENCES benchmarks (id)
            )
        """)

        conn.commit()
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    connection = create_connection()
    if connection:
        create_tables(connection)
        connection.close()
