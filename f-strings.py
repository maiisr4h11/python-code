#f-strings in Python
# name = "Sarah"
# age = "23"
# greeting = f"Hello, my name is {name} and I am {age} years old." #f-strings is for string concatenation
# print(greeting)

# a = 5
# b = 10
# print(f"The sum of {a} and {b} is {a+b}")

#Formatting Numbers
# pi = 3.14159
# formatted = f"The value of pi is {pi:.2f}" #2 decimal places
# print(formatted)

#Nested f-strings 
name = "Sarah"
age = 23
print(f"Hello, my name is {name} and I am {age} years old.")
message = f"User:  {f'Name: {name}, Age: {age}'}"
print(message)

# Multline f-strings

name = "Charlie"
age = 25
message = f"""
Hello,
my name is {name},
I am {age} years old
"""
print(message)