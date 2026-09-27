num = int(input("Enter a integer: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

marks = int(input("Enter your marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

age = int(input("Enter your age: "))
if age>=18:
    print("Adult")
else:
    print("Minor")

integer = int(input("Enter an interger"))
if integer>0:
    print("Positive")
elif integer==0:
    print("Non-Positive")
else:
    print("Non-Positive")

num = int(input("Enter a integer: "))
if num%3==0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")

passw = input("Enter Password")
if passw == "python123":
    print("Correct Password")
else: 
    print("Invalid Password")

user = input("Enter username")
if user == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")

num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))
if num1==num2:
    print("Both are Equal")
else:
    if num1>num2:
        print("num1")
    else:
        print("num2")

temp = int(input("Enter the temperature in celsius"))
if temp>30:
    print("Hot")
else:
    print("comfortable")

discount = int(input("Enter the order ammount: "))
if discount>=5000:
    print("Discount Available")
else:
    print("No Discount")

