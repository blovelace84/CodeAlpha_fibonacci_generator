import time

def fibonacci_generator():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b

#Example Usage:
fib = fibonacci_generator()
for _ in range(20): #Generate the first 20 numbers
    print(next(fib))
    time.sleep(1)
