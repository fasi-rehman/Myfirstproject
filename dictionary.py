  # Dictionaries are used to store data value in a key value pair;
  # They are unordered or mutable or don't allow duplicate keys;
dict={
    "name" : "fasi ur rehman",
    "age"  :  20,
    "surname" : "fasi",
    "marks"  : 94.23,
    "address" :"sargodha",
    "student" : True,
    "jobian" : False,
}
print(dict)
print(type(dict))
print(len(dict))
print(dict["name"])
print(dict["age"])
print(dict["jobian"])
dict["name"] = 'cyber_security'
print(dict["name"])
dict["Father_name"] = "Ramzan"
print(dict)

  # create a null dictionary ;
null ={}
null["name"] = "ambala muslim gurduate college sargodha"
print(null)


  # creating a nested dictionary;
student = {
    "name" : "Fasi",
    "subject" : {
        "phy" : 98,
        "chem" :92,
        "Math" :94,
    }
} 
print(student)
print(student["subject"])
print(student["subject"] ["Math"])
print(student["name"])
  
# dictionary methods;
# dict.keys()  => return all keys of dictionary;
print(student.keys())
print(len(student))
print(list(student.keys()))
print(tuple(student.keys()))
print(len(list(student.keys())))
  # dict.values() => return all value of dictionary;
print(list(student.values()))

# dict.items()  => return all (key,value) pair as a tuples;
print(student.items())
 # access individual keys
pairs = (list(student.keys()))
print(pairs[1])
   # dict.get()  => return the keys value;
print(student.get("named")) # it show no error only show none
print(student["subject"])   # it show error if keys not exist

  # dict.update() => add new keys or dictionary in existing dict
student.update({"profession" : "IT", "Date":"Augest,2026"})
print(student)
new_dict = {"name":"ali","works":"employee"}
print(student.update(new_dict))
print(student)