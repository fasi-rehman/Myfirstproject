str = "string in"
str2 = "python;"
concatination = str + " " +str2   # joining two string
print(concatination)
print(len(concatination)) 
print(len(str))
print(len(str2))  # print string length
print(str)
print(str2)
print(str[2])
print(str2[3])    # getting specific index value
print(str[1:5])   # Slicing the string
print(str[2:len(str)]) #slicing form specific start to end using length function
print(str[0:])    # in this method python automatically understand to print string till end;
print(str[-6:-1]) # we are tracking backword 
# function in python 
str1 = "i am studying python:"
print(str1)
print(str1.capitalize())
str1 = str1.capitalize()    # capitalize the first char of a string 
print(str1)
print(str1.replace("python","java"))  # replece the old occurence with new string :
print(str1.count("t"))   # count the occerence of specific substring or char:
print(str1.endswith(":"))  # return true if the string end with substring:
print(str1.find("python"))     # return the first index of 1st occurence:
print(str1.find("j"))

