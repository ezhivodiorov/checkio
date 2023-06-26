def fib(number):
    a, b = 0, 1
    for x in range(number):
        # yield a
        a, b = b, a + b
    return a
print(fib(1))
