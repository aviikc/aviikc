
# Chained Comparison Operators
'''
An interesting feature of Python is the ability to chain multiple comparisons to perform a more complex test. You can use these chained comparisons as a shorthand for larger Boolean Expressions.

In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in python: and and or.

Let's look at a few examples of using chains:
'''

print(1 < 2 < 3)   #Result: True

# The above statement check if 1 was less than 2 and if 2 was less than 3. We could have written this using an and statement in Python:

print(1<2 and 2<3) #Result: True

# The and is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:

print(1 < 3 > 2)  #Result: True

# The above checks if 3 is larger than both the other numbers, so you could use and to rewrite it as:

print(1<3 and 3>2)  #Result: True

# Its important to note that Python is checking both instances of the comparisons. We can also use or to write comparisons in Python. For example:

print(1==2 or 2<3)  #Result: True

# Note how it was true, this is because with the or operator, we only need one or the other two be true. Let's see one more example to drive this home:

print(1==1 or 100==1)  #Result: True

#These are called comparison operators
