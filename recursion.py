#Recursion in Python
def factorial(n):
    #Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    #Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
#Example usage
print(factorial(5)) #Output: 120