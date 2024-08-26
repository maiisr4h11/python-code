# my_set = {1,2,3,4,1,3,4,2,1,5} # {} is used to create a set
# print(my_set)

# mixed_set = {1,2,3,"Apple",1,4,5.12}
# print(mixed_set)

# myset = set([1,2,3,4,5]) # () is used to create a set
# print(myset)


# #set methods
# myset = {1,2,3,4,5}
# myset.add(6)
# print(myset)

# myset = {1,2,3}
# myset.update([3,4,5])
# print(myset)

# myset = {1,2,3,4,5}
# myset.remove(3) #remove throws an error if the item is not in the set
# print(myset)

# myset = {1,2,3,4,5}
# myset.discard(6) #discard does not throw an error if the item is not in the set
# print(myset)

# myset = {1,2,3,4,5}
# removed_item = myset.pop() #pop removes an item from the set
# print(removed_item)
# print(myset)

# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)
# fruits.clear()
# print(fruits)

# #intersection
# myset = {1,2,3}
# another_set = {2,3,4,5,6}
# print(myset.intersection(another_set))
# intersection_Set = myset & another_set 
# print(intersection_Set)

set1 = {1,2,3}
set2 = {2,3,4}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

sym_diff_set = set1 ^ set2 #symmetric difference is the set of items that are in either set1 or set2 but not in both
print(sym_diff_set)

set2 = {2,3,4}
set1 = {1,2,3}
difference_set = set2.difference(set1) #difference is the set of items that are in set2 but not in set1
print(difference_set)

set1 = {1,2,3}
set2 = {2,3,4}
union_set = set1.union(set2) #union is the set of items that are in either set1 or set2
print(union_set)
union_set2 = set1 | set2
print(union_set2)

set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1.issubset(set2))

set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1.issuperset(set2)) #check if set1 is a superset of set2 . superset means that every item in set1 is in set2

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2)) #check if set1 and set2 have no items in common