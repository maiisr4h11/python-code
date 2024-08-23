# break and continue

for i in range (1,11):
    print (i)
    if i == 5:
        print("The loop is stopped")
        break

count = 0
while True:
    count+=1
    print(count)
    if count == 7:
        print ("The loop is stopped")
        break

#continue statement

for i in range (1,11):
    if i == 6:
        continue
    print ("The value of i is :", i)

#string example
word = "python"
for i in word:
    if i == "h":
        continue # Skip the rest of the loop when the letter is 'h'
    print(i)

#array example
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("The odd number is:")
for i in number:
    if i % 2 == 0:
        continue
    print (i)
