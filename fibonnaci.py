#Write a recursive function named fibonacci(n) that takes an integer n and returns the nth Fibonacci number.
# The Fibonacci sequence is defined as:
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1




def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
number = int(input("Enter a number: "))

for i in range(number):
    print(fibonacci(i))

