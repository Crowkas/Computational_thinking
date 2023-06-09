import time
import sys

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

if __name__ == '__main__':
    n_values = [1000, 10000, 50000, 100000, 200000]
    sys.setrecursionlimit(max(n_values) + 10)

    print("n\t\tLoop\t\t\t\tRecursividad")
    print("\t\tTiempo (s)\t\t\tTiempo (s)")

    for n in n_values:
        start = time.time()
        factorial(n)
        end = time.time()
        loop_time = end - start

        start = time.time()
        factorial_r(n)
        end = time.time()
        recursive_time = end - start

        print(f"{n}\t\t{loop_time}\t\t{recursive_time}")