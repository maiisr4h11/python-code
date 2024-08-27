# a = input("Enter a number: ")
# print(f"Multiplication of number is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
# except:
#     print("Error occured")

# print("Some imp lines of code")
# print("End of program")

#Handle multiple errors
def read_number_from_file(filepath):
    try:
        with open(filepath) as file:
            number_str = file.read()
            number = int(number_str)
            return number
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except ValueError:
        print(f"Invalid number in file: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Operation completed")

number = read_number_from_file("number.txt")
print(number)

#Finally keyword in Python
#It is used to define a block of code that will be executed regardless of whether an exception is raised or not.


