#!/usr/bin/env python

from typing import List


def fib1(n: int) -> int:
    assert (n >= 0), 'n must be a natural number'

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    assert (n >= 0), 'n must be a natural number'

    if n == 0:
        return 0

    # Create an "array" (a list tbh) of 0..n-elements
    f: List[int] = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


if __name__ == '__main__':
    print(fib1(30))
    print(fib2(30))
