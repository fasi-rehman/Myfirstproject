# """ Tuples is a built in data type that lets us create immutable sequence."""
tup = (1,3,5,3,2,7,1,9,4,6)
print(type(tup))
print(tup)
print(tup[1:])
print(tup.index(6))
print(tup.count(1))

 # write a program to asked a user to enter a three numbers & store them in a list;
  # Method1:
String = []

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str3 = input("Enter third string: ")
String.append(str1)
String.append(str2)
String.append(str3)
print(String)
 # Method 2: without using any extra variable;# string = []
String.append(input("Enter first string:"))

String.append(input("Enter second string:"))
String.append(input("Enter third string:"))
print(String)
  # Method 3: using list comprehension;
string = [input("Enter string:") for i in range(3)]
print(string)

 # Method 4: using for loop;
jobs = []
for i in range(0,3,1):
    job = input("Enter job title:")
    jobs.append(job)

print(jobs)
 # write a program to check if the list contain a palindrome of element;
list = [1,2,2,1]
list_copy = list.copy()
list_copy.reverse()
if(list_copy == list):
 print("The list is palindrome :")
else:
 print("The list is not a palindrome :")
 # write a program to count a number of student with "A" grade in the following tuples;("C","D","A","A","B","A")
tups = ["C","D","A","A","B","A"]
student = tups.count("A")
print("The student with grade A are:",student)
tups.sort()
print(tups)
