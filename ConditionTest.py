# write a program to check whether the number entered by the user is even or odd.

num = int(input("Enter the number :"))
if num %2 == 0:
    print("the given number is even:",num)
else:
    print("the given number is odd:",num)

# write a program to find a greatest of three number entered by the user.


num1 =int(input("Enter the first num1: = "))
num2 =int(input("Enter the second num2: = "))
num3 =int(input("Enter the third num3: = "))
num4 =int(input("Enter the fourth num4: = "))
if num1>num2 and num1>num3 and num1>num4:
    print("the greatest number is:",num1)
elif num2>num1 and num2>num3 and num2>num4:
    print("the greatest number is:",num2)
elif num3>num1 and num3>num2 and num3>num4:
    print("the greatest number is:",num3)    
else:
    print("the greatest number is:",num4)

# write a program to check the number is multiple of 7 or not.


num = int(input("Enter the number: "))
if num % 7 ==0:
    print("the given number is multiple of 7:",num)
else:
    print("the given number is not multiple of 7:",num)