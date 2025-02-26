def fibonacci_generator(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
#Example usage
fib = fibonacci_generator(10)
for _ in range(10): # Generate the first 10 numbers
    print(next(fib))

