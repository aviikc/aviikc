# When printing out if we need to format our document in the
# output we use string literals like \n, \t, \\
# the whole list is here https://docs.python.org/2.0/ref/strings.html


#example
print("Twinkle Twinkle Little Star\nHow I Wonder What You Are.")
#\n gives a new line

#example
#print("Total:\t"+500) #Gives a TypeError because we can only concatenate string to string
# Please remember that if there is a mismatch in data-type for an operation we end up with TypeError

print("Total:\t"+"500") #Using \t we used the tab space currently set to 4 spaces on my IDE.

# What if we want to print “A ship you boarded,” Stephanie said. “Tell me, was it a luxury cabin or more like steerage?”
print("\"A ship you boarded,\" Stephanie said. \"Tell me, was it a luxury cabin or more like steerage?\"")
# This is called escape character

#Specially when writing urls in windows we forward slash "\". So the path
# D:\classes\python\postCovid\01_basics\01printing_output might give python interpretor 
# ideas like \c, \p, \0, etc whic might or might not be an escape character.
# in such cases we use "\\"
print("D:\classes\python\postCovid\01_basics\01printing_output") #might end up meaning somting else

#whereas
print("D:\\classes\\python\\postCovid\\01_basics\\01printing_output") #is more pythonic