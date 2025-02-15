import timeit
import random


def setup_data(size):
    """Create test data structures and test values."""
    data_set = set(range(size))
    data_list = list(range(size))

    # Generate test values: 50% present, 50% absent for fair comparison
    test_values = (
        [random.randint(0, size-1) for _ in range(500)] +  # Present values
        [random.randint(size, size*2) for _ in range(500)]  # Absent values
    )
    return data_set, data_list, test_values


def benchmark_membership(size):
    """Benchmark membership testing for both set and list."""
    data_set, data_list, test_values = setup_data(size)

    # Set membership testing
    set_time = timeit.timeit(
        lambda: [x in data_set for x in test_values],
        number=100
    )

    # List membership testing
    list_time = timeit.timeit(
        lambda: [x in data_list for x in test_values],
        number=100
    )

    return set_time, list_time


if __name__ == "__main__":
    # Added larger size to better show difference
    sizes = [100, 10000, 100000, 1000000]

    print("Benchmarking Set vs List Membership:")
    print(f"{'Size':<10} {'Set (s)':<10} {'List (s)':<10} {'Ratio':<10}")
    print("-" * 40)

    for size in sizes:
        try:
            set_time, list_time = benchmark_membership(size)
            ratio = list_time / set_time
            print(f"{size:<10} {set_time:.6f}  {list_time:.6f}  {ratio:.2f}x")
        except Exception as e:
            print(f"{size:<10} Error: {str(e)}")
