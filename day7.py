collection = [1, 2, 3, 4, 5]
# print(collection)
# print(len(collection))
# print(collection[0])
# print(collection[1])
# print(collection[2])
# print(collection[3])
# print(collection[4])
# coll = set()
# print(coll)
# collection = [1, 2, 3, 4, 5]

# Convert it to a set
my_set = set(collection)
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # {1, 2, 3, 4, 5, 6}
my_set.update([7, 8])  # {1, 2, 3, 4, 5, 6, 7, 8}
my_set.discard(1)  # {2, 3, 4, 5, 6, 7, 8}
my_set.remove(2)  # {3, 4, 5, 6, 7, 8}
