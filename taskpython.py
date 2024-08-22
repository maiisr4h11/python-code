#Question 1
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number", num, "is even")
else:
    print("The number", num, "is odd")

#Question 2
mul = int(input("Enter a number: "))
while mul in range(1, 11):
    print(num, "x", mul, "=", num * mul)
    mul += 1
    
# Question 3
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")
    
# Question 4
 
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1
print("The number of vowels in the string is:", count)



    