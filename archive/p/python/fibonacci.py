import sys


def fibonacci(n):
    fib = fibs()
    # prints fibonacci numbers from 1 to n
    for i in range(1, n + 1):
        print(f'{i}: {next(fib)}')


def fibs():
    first = 1
    second = 1
    # returns fibonacci number for 1
    yield first
    # continues here and returns fibonacci number for 2
    yield second
    
    while True:
        # calculates next fibonaaci number by summing first and second
        new = first + second
        yield new
        # update last two fibonacci numbers that are used to calculate the next one
        first = second
        second = new


def main(args):
    try:
        fibonacci(int(args[0]))
    except (IndexError, ValueError):
        print("Usage: please input the count of fibonacci numbers to output")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
