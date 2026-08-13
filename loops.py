# while loop;
num = [1,5,9,3,2,4,8]
index=0
while(index < len(num)):
  print(f"the num index is : {num[index]} at position {index}")
  index+=1 
    
  # Question 1
  # print the multipulication table of given number ;
n = int(input("enter the number:"))
i=1
while i<=10:
    print(f"The table of :{n} * {i} = ",n*i)
    i+=1
  
 # find a specific value in a list;
list = [1,2,2,7,4,6,2,2,5]
i=0   # initialize index at startup is 0;
x=2   # define searching value;
while i<len(list):
  if(list[i]==x):
    print(f"the value is found:{x} at index :->",i)
  else:
    print("The result is searching:")
  i+=1
print("the total number of time the value occur is:",list.count(2))  


# condition in loops Break & continue
i=0
while i<=5:
    print(i)
    if i == 4:
     break
    i+=1
print("loop is ended")    
  # continue condition mean skip value;
j=0
while j<=10:
   if(j%2==1):       # print even number 
      j+=1 
      continue
   print(j)
   j+=1
print("loop is ended:")   
  

    # for loop ;
nums = ("ali","bilal","captian","driver","electronic","fathi")
for value in nums:
    print(value)
print("END")    
# print individual character;
str = "individual"
for char in str:
    if(char=='a'):
      print("value is found:","a")
      break
    print(char) 
   # skipping the even numbers;
nums = (1,2,3,4,5,6,7,8,9)
for n in nums:
   if(n%2==0):
      continue
   print(n)
     # print the index of given value;
number = (1,5,8,5,4,8,9,3)
value = 8
index = 0
for n in number:
   if(n==value):
      print("the value is found at index",index)
   index+=1
  # WAP to print some of n natural number (while loop);
num = int(input("enter the number:"))
i=1
sum=0
while i<=num:
    sum +=i
    i+=1
    print(sum)


    # print table using for loop;
num = int(input("enter the number:"))
for i in range(1,num,1):
  multiple = num*i
  print(f"the multiple of no {num}*{i}",multiple)
  # using pass keyvalue;
  for i in range(5):
    pass
  print("the pasuse statement:")
     # WAP to find the factorial of first n number:
n = int(input("enter the number"))
fact=1
i=1
for i in range(1,n+1,1):
   fact *=i
   i+=1
print("the factorial of number is :",fact) 