# Python Performance Benchmarks

A collection of benchmarks exploring various aspects of Python performance. This project aims to provide empirical data about different Python constructs, helping developers make informed decisions about their code.

## Overview

This repository contains benchmarks for various Python operations, data structures, and programming patterns. Each benchmark is designed to provide clear, reproducible results that can guide practical development decisions.

## Structure

| Category | Status | Files |
|----------|--------|-------|
| 1-data-structures | Implemented | [List vs Tuple Access](results/1-data-structures/list-vs-tuple-access.md), [Dict vs List Membership](results/1-data-structures/dict-vs-list-membership.md), [Set vs List Membership](results/1-data-structures/set-vs-list-membership.md) |
| 2-string-operations | In Progress | - concatenation_vs_join.py<br>- formatting_methods.py<br>- substring_search.py |
| 3-function-calls | Planned | - |
| 4-loops | Planned | - |
| 5-imports | Backlog | - |
| 6-exception-handling | Backlog | - |
| 7-math-operations | Backlog | - |
| 8-sorting | Backlog | - |
| 9-io-operations | Backlog | - |
| 10-multithreading-async | Backlog | - |
| 11-caching-lookup | Backlog | - |
| 12-python-internals | Backlog | - |

## Running Benchmarks

```sh
# Run a specific benchmark
python benchmarks/category/benchmark-name.py
```

```sh
# Example:
python benchmarks/1-data-structures/list-vs-tuple-access.py
```

## Results

The results documented in this repository were collected on a standardized test environment. However, performance characteristics may vary across different hardware configurations and Python versions. Users are encouraged to run these benchmarks on their own systems to gather data specific to their environment.

Future improvements to this project will include tools for collecting and comparing benchmark results across different machines and configurations, enabling more comprehensive performance analysis for specific use cases.

### Result Configurations

| Machine | CPU | RAM | Python Version | OS | Date | Notes |
|---------|-----|-----|----------------|----|----|-------|
|[Author](https://github.com/zbuhrer) | Apple M2 | 16 GB  | Python 3.12 | MacOS Sonoma Version 14.5 (23F79) | Feb 2025  | Initial Benchmarking |
|         |     |     |                |    |    |       |
|         |     |     |                |    |    |       |

> **Note**: I would like to implement a database-driven solution to better track and compare results across different configurations. This will enable more sophisticated analysis and visualization of performance characteristics across environments.
