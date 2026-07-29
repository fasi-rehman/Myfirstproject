# set is a collection of unordered element;
# Each elements in the sets must be unique or immutable;

collections = {1,2,3,4,"ali","iT",2,4,3,3,"student"}
print(collections)
print(type(collections))
print(len(collections))

# create a empty set
student = set()
student.add("aldi")      # sets are mutable
student.add("khan")
student.add(3)
student.add(2)
student.add(1)
student.add((1,3,4,4,5,6,7,8))   # add a tuples in a sets


print(student)                   #sets elements are immutable;
print(type(student))
student.remove("aldi")  #remove an elements
print(student.pop())  #remove an random elements
print(student.pop())
print(student.pop())
print(student)

student.clear()
print(type(student))
print(len(student))
print(student)


# union method in sets 
time = {1,2,3,4}
date = {2,5,5,1,7,9}
print("This is union of two sets")   #{1,2,3,4,5,7,9}
print(time.union(date))
print("check that there is no changes in original sets")
print(time) # there is no changes in original set time
print(date) # there is no changes in original sets date


 #intersection method 

print("This is intersection")
print(time.intersection(date))  #{1,2}


#     #practic Question ......1....?

# store the following world meaning in a python dictinary;

""" table : "a piece of furniture", "list of facts & figures"
     cat   : "a small animal" """
data = {
    "table": ["a piece of furniture","list of facts & figures"],
    "cat"  : "a small animal"
}
print(data)
  #  Question......2....

  # you are given a list of subjects for students.Assume one classroom is required for subject.now many classrooms are needed by all students.
""" "python" ,"java","c++","python","javascript", "java","python","java","c++","c": """
sets = {
    "python","java","c++","python","javascript", "java","python","java","c++","c"
}
print(sets)
print(len(sets))

#  Question ..3...?
""" WAP to enter marks of 3 subjects form the user and store them in a dictionary. Start with an empty dictionary & add one by one.Use subject name as key & marks as value."""

marks = {}
for i in range(3):   # time complexity is big O(n);
     subject = input(f"Enter name of subject {i+1}: ").strip()

     grade = int(input(f"Enter marks for {subject}: ").strip())
     marks[subject] = grade
print("Marks:", marks)


   # Method 2
mark = {}
x = int(input("enter phy marks: "))
mark.update({"phy" : x})
x = int(input("enter math marks: "))
mark.update({"chem" : x})
x = int(input("enter chem marks: "))
mark.update({"comp" : x})

print(mark)

""" Figure ut a way to store 9 & 9.0 as a separate values in the set."""
value = {  # in this situation we store one as a string 
   ("float",9.0),
   ("int",9)
}
print(value)
values ={"9.0",9}  # built in data type
print(values)
num ={"9",9.0}     # built in data type
print(num)