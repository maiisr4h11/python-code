
# file = open("hello.txt", "w") # w is for write mode
# file.write("Selamat datang, ")
# file.close()

# file = open("hello.txt", "a") # a is for append mode
# file.write(" dan baik")
# file.close()

# file = open("hello.txt", "r") # r is for read mode
# print(file.read())
# file.close()

# with open("hello.txt", "r") as file: # r is for read mode
#     print(file.read())

# file = open("hello.txt","r")
# line = file.readline() #read one line
# print(line)
# file.close()

# file = open("hello.txt","r")
# line = file.readlines() #read more than one line
# print(line)
# file.close()

# file = open("hello.txt","a")
# lines = ["First line\n", "Second line\n", "Third line\n"]
# file.writelines(lines)
# file.close()

# with open("hello.txt","r") as file:
#     file.seek(5) # read start from 5th character
#     content = file.read()
#     print(content)

with open ("hello.txt","w") as f:
    f.write("Hello World")
    f.truncate(5)
    

