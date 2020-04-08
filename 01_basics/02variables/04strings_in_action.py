# Python Strings - This shit is important

a = "Hello Boys and Girls" #This is a string
b = "D:\\classes\\python\\postCovid\\qt_passanger_data"
c = "1234" #This is also a string as the integers are inside an inverted comma

#length of a string 
#To find the length of a string use len() function
print(len(a)) #Result: 20        This gives the total characters in a string and its always an integer

#Casing 
#upper(), upper()
#Please see the way these functions are used.
print(a.upper()) #Result: HELLO BOYS AND GIRLS converts caracters to upper case
print(a.lower()) #Result: hello boys and girls converts characters to lower case





#Slicing - Slicing up strings
print(a[0])  #Result: H
#Indexing of the elements in the string start from left are 0,1,2,3,4.....till the last letter.
# Since the index starts from 0, the total length of string is always (last_index - 1)
#So print(a[3]) #This should yeild given_index+1 ie, 4+1 or the 5th letter since indexing starts from 0
print(a[4]) #Result: o which is the 5th letter

#Similiarly
print(b[12]) #Result: y
print(a[9]) #Result: s

#We can even use negetive numbers in slicing
print(a[-1]) #Result: s       Yeilds the last letter of the string
print(b[-1]) #Result: a       Yeilds the last letter of the string
print(c[-1]) #Result: 4       Yeilds the last letter of the string

#So You can see negetive indexing counts the characters in the string from right to
#left whereas positive indexing is quite the opposite.
#Also note Negetive index starts at -1 whereas positive index starts at 0.
#Use negative indexes to start the slice from the end of the string


#This is all good when we are looking for single characters but you can return a range of characters by using the slice syntax
# This done by specifying the start index and the end index, separated by a colon
print(b[2:5])  #This means get the characters from position 2 to position 5 (not included)
# The result is from index+1 ie 2+1 3rd character till the 5+1 ie, 6th but not including it hence 5th character.
# Result: \cl

#Now try
print(a[-5:-1]) #Result: Girl
# If we were to print till the last letter or the full letter Girls use
print(a[-5:])
#An open end means zero

