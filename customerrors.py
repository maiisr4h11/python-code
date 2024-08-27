# a = int(input("Enter a number: "))
# if(a < 5 or a > 9):
#     #
#     raise ValueError("The number should be between 5 and 9")
# print("The number is valid")

def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    # else:
    #     print("The number is positive")
    return number

# a = check_positive(int(input("Enter a number: ")))

def getInput():
    try:
        user_input = input("Enter a positive number: ")
        number = int(user_input)
        check_positive(number)
        print("The number is positive.")
    except ValueError as e:
        print(f"Invalid input: {e}.")

getInput()
