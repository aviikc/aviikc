#Python Collections
#Source https://www.w3schools.com/python/python_lists.asp

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Print the second item of the list: Kind of like indexing in strings
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Slicing a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Return the third, fourth, and fifth item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  #returns the items from the beginning to "orange"

# Change the second item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#Appendind Items to list   ::           VERY IMPORTANT
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Remove an item from list   ::         VERY IMPORTANT
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified) 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

