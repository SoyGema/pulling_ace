import sys

from beyond_the_nest.beyond_the_nest import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
