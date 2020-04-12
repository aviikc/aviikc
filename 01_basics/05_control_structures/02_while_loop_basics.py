# The Basic while loop
# The while loop we can execute a set of statements as long as a condition is true.


x=0               #Assigned and initialized
while(x<7):
    print(x)       #Statement
    x = x+1 # This statement can be written as x += 1  # Increment

# We assign a value to variable x. In this case 0.
# With the while block we are testing the truthfulness of the situation
# In other words we are looking for a boolean true or false while 
# testing the situation x<7 while incrementing the value of x with 1.
# Eventually the value of x will be 7 and above the condition x<7 will
# test false so the loop will stop.
# https://www.w3schools.com/python/python_while_loops.asp





# We can even test while loops on true situations like:

while True:
    my_input = input("Enter a value: ")
    if my_input == "q" or my_input == "Q":
        print("loop broken")
        break       
    else:
        print("Loop on!")
        continue




# while loop can be coupled  with the else statement :

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")