#list methods

fruits = ["apple", "banana", "cherry"]
fruits.append("orange") #add an item to the end of the list
print(fruits) 

#insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange") #insert an item at a specific position
print(fruits)

#extend
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]
fruits.extend(cars) #add multiple items to the end of the list
print(fruits)

#remove
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") #remove an item by value
print(fruits)

#pop
fruits = ["apple", "banana", "cherry"]
fruits.pop(1) #remove an item by index
print(fruits)

#clear
fruits = ["apple", "banana", "cherry"]
fruits.clear() #remove all items from the list
print(fruits)
