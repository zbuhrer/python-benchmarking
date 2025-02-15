import flet as ft
import sqlite3
import subprocess
import os
from datetime import datetime
from typing import List, Dict


class BenchmarkGUI:
    def __init__(self):
        self.db_path = 'benchmarks.db'
        self.current_category = None
        self.running_benchmark = False

    def main(self, page: ft.Page):
        self.page = page  # Store page reference
        page.title = "Python Benchmark Manager"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        page.spacing = 20

        # Create UI components
        self.status_text = ft.Text("Ready to run benchmarks", size=16)
        self.progress_ring = ft.ProgressRing(visible=False)

        self.category_dropdown = ft.Dropdown(
            label="Select Category",
            width=200,
            options=[
                ft.dropdown.Option("all", "All Categories"),
                ft.dropdown.Option("data-structures", "Data Structures"),
                ft.dropdown.Option("string-operations", "String Operations"),
                ft.dropdown.Option("function-calls", "Function Calls"),
                ft.dropdown.Option("loops", "Loops"),
            ],
            value="all",
            on_change=self.on_category_selected
        )

        self.run_button = ft.ElevatedButton(
            "Run Benchmarks",
            icon=ft.icons.PLAY_ARROW_ROUNDED,
            on_click=self.run_benchmarks
        )

        self.results_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Benchmark")),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Execution Time (s)")),
                ft.DataColumn(ft.Text("Date")),
            ],
            rows=[]
        )

        # Layout
        page.add(
            ft.Row([
                ft.Text("Python Benchmark Manager",
                        size=32, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER),

            ft.Row([
                self.category_dropdown,
                self.run_button,
                self.progress_ring,
            ], alignment=ft.MainAxisAlignment.START),

            self.status_text,

            ft.Container(
                content=self.results_table,
                padding=10,
                border=ft.border.all(1, ft.colors.GREY_400),
                border_radius=10,
            )
        )

        # Load initial results
        self.load_results()

    def get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def format_timestamp(self, timestamp):
        """Format timestamp string or integer to datetime string."""
        try:
            # If timestamp is a string, try to parse it directly
            if isinstance(timestamp, str):
                return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            # If timestamp is an integer (Unix timestamp)
            elif isinstance(timestamp, (int, float)):
                return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            else:
                return "Invalid timestamp"
        except (ValueError, TypeError):
            return "Invalid timestamp"

    def load_results(self):
        """Load and display benchmark results from the database."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            query = """
                SELECT b.name, b.category, r.execution_time, r.timestamp
                FROM benchmarks b
                JOIN results r ON b.id = r.benchmark_id
                WHERE (? IS NULL OR b.category = ?)
                ORDER BY r.timestamp DESC
            """

            category = None if self.category_dropdown.value == "all" else self.category_dropdown.value
            cursor.execute(query, (category, category))

            results = cursor.fetchall()

            # Clear existing rows
            self.results_table.rows.clear()

            # Add new rows
            for result in results:
                name, category, execution_time, timestamp = result
                self.results_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(name)),
                            ft.DataCell(ft.Text(category)),
                            ft.DataCell(
                                ft.Text(f"{float(execution_time):.6f}")),
                            ft.DataCell(
                                ft.Text(self.format_timestamp(timestamp))),
                        ]
                    )
                )

            # Update the UI
            self.results_table.update()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    async def run_benchmarks(self, e):
        if self.running_benchmark:
            return

        self.running_benchmark = True
        self.progress_ring.visible = True
        self.run_button.disabled = True
        self.status_text.value = "Running benchmarks..."
        self.update_ui()

        try:
            category = self.category_dropdown.value
            benchmark_dir = "benchmarks"

            if category != "all":
                benchmark_dir = os.path.join(benchmark_dir, category)

            for root, _, files in os.walk(benchmark_dir):
                for file in files:
                    if file.endswith('.py'):
                        script_path = os.path.join(root, file)
                        self.status_text.value = f"Running: {script_path}"
                        self.status_text.update()

                        process = subprocess.run(
                            ['python3', script_path],
                            capture_output=True,
                            text=True,
                            check=True
                        )

                        await self.page.update_async()

            self.status_text.value = "Benchmarks completed successfully!"
            self.load_results()

        except Exception as e:
            self.status_text.value = f"Error running benchmarks: {str(e)}"
        finally:
            self.running_benchmark = False
            self.progress_ring.visible = False
            self.run_button.disabled = False
            self.update_ui()

    def on_category_selected(self, e):
        self.load_results()

    def update_ui(self):
        self.status_text.update()
        self.progress_ring.update()
        self.run_button.update()
        self.results_table.update()


if __name__ == '__main__':
    app = BenchmarkGUI()
    ft.app(target=app.main)
