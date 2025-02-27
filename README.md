This project generates Fibonacci numbers using a generator function. The numbers are displayed one at a time with a delay creating a slow-motion effect. 
Features:
  1. Uses a generator function to yield Fibonacci numbers infinitely
  2. Implements a time delay between numbers for a smooth display
How to run code:
  1. Ensure you have Python installed on your machine
  2. Clone this repository or copy the script
  3. Run the script using the following command on your terminal: python fibonacci_generator.py
Code Example:
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

How it works:
  1. The fibonacci_generator() function generates the numbers indefinitely.
  2. the time_sleep(1) function adds a 1-second delay between outputs.
  3. The script prints the first 10 numbers in a slow-motion effect.
License:
Open source and free to use,
