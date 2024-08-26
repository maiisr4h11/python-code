my_dict ={
    "name":"John",
    "age":30,
    "city":"New York"
}
print(my_dict)

#Using the dict() function
my_dictv= dict(name="Alice", age=30, city="London")
print(my_dictv)

#Using the get() method
print(my_dict.get("name", "Not Found")) #Not Found is the default value if the key is not found
print(my_dictv.get("age"))

my_dict = {"name": "John", "age": 30, "city": "New York"}
item = my_dict.popitem()
print(item)
print(my_dict)

keys = {"name", "age", "city"}
my_dict = dict.fromkeys(keys, "Unknown")
print(my_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

my_dict = {"name": "Alice", "age": 25}
print(my_dict.values())  # Output: dict_values(['Alice', 25])

my_dict = {"name": "Alice", "age": 25}
my_dict.update({"age": 26, "city": "New York"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

