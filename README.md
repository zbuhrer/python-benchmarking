# Python Performance Benchmarks

A collection of benchmarks exploring various aspects of Python performance. This project aims to provide empirical data about different Python constructs, helping developers make informed decisions about their code.

## Overview

This repository contains benchmarks for various Python operations, data structures, and programming patterns. Each benchmark is designed to provide clear, reproducible results that can guide practical development decisions.

## Structure

| Category | Status | Files |
|----------|--------|-------|
| 1-data-structures | Implemented | - dict-vs-list-membership.py<br>- list-vs-tuple-access.py<br>- set-vs-list-membership.py |
| 2-string-operations | Implemented | - concatenation_vs_join.py<br>- formatting_methods.py<br>- substring_search.py |
| 3-function-calls | Empty | - |
| 4-loops | Empty | - |
| 5-imports | Empty | - |
| 6-exception-handling | Empty | - |
| 7-math-operations | Empty | - |
| 8-sorting | Empty | - |
| 9-io-operations | Empty | - |
| 10-multithreading-async | Empty | - |
| 11-caching-lookup | Empty | - |
| 12-python-internals | Empty | - |

## Running Benchmarks

```bash
# Run a specific benchmark
python benchmarks/category/benchmark-name.py

# Example:
python benchmarks/1-data-structures/list-vs-tuple-access.py
```

## Sample Results

### Data Structures

#### List vs Tuple Access
```
Benchmarking List vs Tuple Access:
Size       List (s)   Tuple (s)  Ratio
----------------------------------------
100        0.013662  0.012261  1.11x
10000      0.013086  0.012261  1.07x
1000000    0.012593  0.012743  0.99x
```

[Additional benchmarks results will be added as they are implemented]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Guidelines for Adding New Benchmarks

1. Create a new Python file in the appropriate category directory
2. Include clear documentation within the code
3. Ensure consistent output formatting
4. Add results to this README
5. Include analysis of the results

## License

[Add your chosen license]

## Acknowledgments

- Contributors
- Resources and references used
