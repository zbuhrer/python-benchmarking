import timeit
import random


def setup_data(size):
    data_dict = {str(i): i for i in range(size)}
    data_list = list(range(size))
    # Pre-generate test values to ensure fair comparison
    test_values = ([str(random.randint(0, size-1)) for _ in range(500)] +
                   [str(random.randint(size, size*2)) for _ in range(500)])
    return data_dict, data_list, test_values


def benchmark_membership(size):
    data_dict, data_list, test_values = setup_data(size)

    # Dict key lookup
    dict_time = timeit.timeit(
        lambda: [k in data_dict for k in test_values],
        number=100
    )

    # List membership
    list_time = timeit.timeit(
        lambda: [int(k) in data_list for k in test_values],
        number=100
    )

    return dict_time, list_time


if __name__ == "__main__":
    sizes = [100, 10000, 100000]

    print("Benchmarking Dict vs List Membership:")
    print(f"{'Size':<10} {'Dict (s)':<10} {'List (s)':<10} {'Ratio':<10}")
    print("-" * 40)

    for size in sizes:
        dict_time, list_time = benchmark_membership(size)
        ratio = list_time / dict_time
        print(f"{size:<10} {dict_time:.6f}  {list_time:.6f}  {ratio:.2f}x")
