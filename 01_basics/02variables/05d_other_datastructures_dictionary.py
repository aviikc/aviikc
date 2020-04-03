#Python Collections
#Source https://www.w3schools.com/python/python_tuples.asp

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Print the last item of the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Return the third, fourth, and fifth item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Once a tuple is created, you cannot change its values.
# Hence tuples are immutable

# Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)





