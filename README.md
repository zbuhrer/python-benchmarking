# Python Performance Benchmarks

A collection of benchmarks exploring various aspects of Python performance. This project aims to provide empirical data about different Python constructs, helping developers make informed decisions about their code.

## Overview

This repository contains benchmarks for various Python operations, data structures, and programming patterns. Each benchmark is designed to provide clear, reproducible results that can guide practical development decisions.

## Database System

The project uses SQLite to store and track benchmark results. This enables:
- Systematic collection of benchmark data
- Historical performance tracking
- Cross-environment result comparison
- Data-driven performance analysis

### Database Setup

```sh
# Initialize the database and create required tables
python database.py
```

### Database Schema

The database consists of two main tables:

**benchmarks**
- `id`: Primary key
- `name`: Benchmark name
- `category`: Category (e.g., "data-structures", "string-operations")
- `description`: Detailed description of what is being tested
- `script_path`: Path to the benchmark script

**results**
- `id`: Primary key
- `benchmark_id`: Foreign key referencing benchmarks table
- `timestamp`: When the benchmark was run
- `execution_time`: Total execution time
- `output`: Detailed benchmark results

### Running Benchmarks

```sh
# Run all benchmarks and store results in database
python run_benchmarks.py

# Query and display results
python query_results.py
```

## Structure

```sh
python-benchmarking/
├── benchmarks/                     # Main benchmarks directory
│   ├── 1-data-structures/         # ✓ Implemented
│   │   ├── dict-vs-list-membership.py
│   │   ├── list-vs-tuple-access.py
│   │   └── set-vs-list-membership.py
│   ├── 2-string-operations/       # 🔄 In Progress
│   ├── 3-function-calls/          # 📅 Planned
│   ├── 4-loops/                   # 📅 Planned
│   ├── 5-imports/                 # ⏳ Backlog
│   ├── 6-exception-handling/      # ⏳ Backlog
│   ├── 7-math-operations/         # ⏳ Backlog
│   ├── 8-sorting/                 # ⏳ Backlog
│   ├── 9-io-operations/           # ⏳ Backlog
│   ├── 10-multithreading-async/   # ⏳ Backlog
│   ├── 11-caching-lookup/         # ⏳ Backlog
│   ├── 12-python-internals/       # ⏳ Backlog
│   └── results/                   # Benchmark results in markdown
│       ├── 1-data-structures/
│       └── 2-string-operations/
├── database.py                    # Database initialization and management
├── main.py                        # Main application entry point
├── query_results.py              # Tools for querying benchmark results
└── run_benchmarks.py             # Benchmark execution script
```

## Results

Results are stored in the SQLite database and can be analyzed using the provided query tools. The system tracks:
- Execution times across different runs
- Performance variations between environments
- Historical trends

### Result Configurations

| Machine | CPU | RAM | Python Version | OS | Date | Notes |
|---------|-----|-----|----------------|----|----|-------|
|[zbuyhrer](https://github.com/zbuhrer) | Apple M2 | 16 GB  | Python 3.12 | MacOS Sonoma Version 14.5 (23F79) | Feb 2025  | Initial Benchmarking |

## Contributing

When adding new benchmarks:
1. Create a new benchmark script in the appropriate category directory
2. Ensure the script outputs results in the expected format
3. Run the benchmark using `run_benchmarks.py`
4. Verify results are properly stored in the database
5. Update documentation as needed

## Future Improvements

- Web interface for viewing and comparing results
- Automated environment detection and logging
- Statistical analysis of benchmark results
- Performance visualization tools
- Cross-version Python testing
