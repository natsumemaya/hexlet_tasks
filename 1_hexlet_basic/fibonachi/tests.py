from solution import fib


def test_fib():
    print("fib(0)", fib(0) == 0)
    print("fib(1)", fib(1) == 1)
    print("fib(2)", fib(2) == 1)
    print("fib(3)", fib(3) == 2)
    print("fib(4)", fib(4) == 3)
    print("fib(5)", fib(5) == 5)
    print("fib(10)", fib(10) == 55)

test_fib()