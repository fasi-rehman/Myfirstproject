record = ["Ali",20,96.2,"married","sargodha"]
print(record)            # print the whole student record
print(type(record))      # print class of list.
print(len(record))       # print length of list.
print(record[3:5])       # print sublist of list
record[0] = "Ali Khan"   # String are mutable in  python
print(record)            # print list after changing.
print(record[0])         # print 0 index value of list.
record.append("geneious")
print(record)
record.count("r")
record.remove(96.2)
print(record)
record.insert(3,"Master")
print(record)
    # this is new list.
result = [8,4,7,2,5,1,2,9,3]
result.reverse()
print(result)
result.sort(reverse = True)  # sort in decending order
print(result)
result.reverse()  # it only reverses the list to decending order
print(result)
print(result.pop())
print(result.sort())      #sort in accending order
print(result)
print(result.index(8)) # print index of 3 in list
print(result.pop(1))   # remove element at index 1
print(result.append(10))  # add element at the end of the list
result.clear()     #this removes all the elements from list
print(result)
print("List is empty now")

