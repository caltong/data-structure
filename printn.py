import sys

sys.setrecursionlimit(10000000)


def printn(n):
    if n:
        printn(n - 1)
        print(n)


printn(1000)
