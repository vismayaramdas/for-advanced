print("********   welcome to luminar")
print("enter the number1 :")
num1=int(input())
print("enter the second number")
num2=int(input())
print("these are the operators you can use")
print("1. addition")
print("2. subtraction")
print("3. division")
print("4. modulus")
a=input("please choose an option from these(1,2,3,4,5):")
if a=="1":
    print("addition")
    print("the sum of the two numbers is:",num1+num2)
if a=="2":
    print("subtraction")
    print("the difference of the two numbers is:", num1 - num2)
if a=="3":
    print("division")
    print("the divident of the two numbers is:", num1 / num2)
if a=="4":
    print("modulus")
    print("the mod of the two numbers is:", num1 % num2)

