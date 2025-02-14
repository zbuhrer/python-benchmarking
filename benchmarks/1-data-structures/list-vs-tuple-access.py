import timeit
import random


def setup_data(size):
    data_list = list(range(size))
    data_tuple = tuple(range(size))
    return data_list, data_tuple


def benchmark_access(size, iterations):
    data_list, data_tuple = setup_data(size)
    indices = [random.randint(0, size-1) for _ in range(iterations)]

    # List access
    list_time = timeit.timeit(
        lambda: [data_list[i] for i in indices],
        number=1000
    )

    # Tuple access
    tuple_time = timeit.timeit(
        lambda: [data_tuple[i] for i in indices],
        number=1000
    )

    return list_time, tuple_time


if __name__ == "__main__":
    sizes = [100, 10000, 1000000]
    iterations = 1000

    print("Benchmarking List vs Tuple Access:")
    print(f"{'Size':<10} {'List (s)':<10} {'Tuple (s)':<10} {'Ratio':<10}")
    print("-" * 40)

    for size in sizes:
        list_time, tuple_time = benchmark_access(size, iterations)
        ratio = list_time / tuple_time
        print(f"{size:<10} {list_time:.6f}  {tuple_time:.6f}  {ratio:.2f}x")
