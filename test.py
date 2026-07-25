a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
# relational operators;
print(a==b) # False
print(a!=b) # True
print(a<=b) # False
print(a>=b) # True
print(a<b)  # False
print(a>b)  # True
print(not False)
print(not (a<b))
val1 = False
val2 = False
print("AND Operator:" ,val1 and val2)
print("OR Operator:" , (a>b) or (a==b))
#Type conversion;
#in type conversion python compilar automatically convert;
#in type costing programmer forcefully convert the value type 
name = input("enter your name:")
print(type(name),name)
age = int(input("enter your age:"))
print(type(age),age)
marks = float(input("enter your marks:"))
print(type(marks),marks)