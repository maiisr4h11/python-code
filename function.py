#defining a function
def greet(): 
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today?")

greet() #calling a function
print("bye")

def greet(name):
    print (f"Hello {name}")
greet("Sarah")

def greet(name = "sarah"):
    print(f"hello {name}")

greet()
greet("Mike")

#return statement
def multiply(x, y):
    return x * y

result = multiply(2, 3)
print("The result is", result)

#conditional statement
def checknumber(number):
    if number > 0:
        return("The number is positive")
    elif number < 0:
        return("The number is negative")
    elif number == 0:
        return("The number is zero") 
print(checknumber(0))
print(checknumber(-5))
print(checknumber(3))

#Positional arguments
def greet(name, location):
    print(f"Hello {name}, welcome to {location}")
greet("Sarah", "Malaysia")

#keyword arguments

def greet(name, location):
    print(f"Hello {name}, welcome to {location}")

greet(location = "Malaysia", name = "Sarah")

#default arguments
def greet(first_name, last_name="Smith"):
    print(f"Hello, {first_name} {last_name}!")

greet("John")         # Uses default last name
greet("Jane", "Doe")  # Overrides default last name

