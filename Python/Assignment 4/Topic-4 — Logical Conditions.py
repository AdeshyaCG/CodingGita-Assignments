marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))
if marks >=60:
    if attendance >=75:
        print("Eligible")
else:
    print("Not Eligible")

marks = int(input("Enter Your marks: "))
income = int(input("Enter your income: "))
if marks>=85 or income<300000:
    print("Sholorship Avilable")
else:
    print("No Scholarship")

day = input("Enter day name: ")
if day == "Saturday" or "Sunday":
    print("Weekend")
else:
    print("Weekday")

user = input("Enter username: ")
passw = input("Enter password: ")
if user == "student" and passw == "python123":
    print("Access Granted")
else:
    print("Access Denied")

avilable = input("Enter your adress: ")
if avilable == "Ahmedabad" or "Ghandhinagar":
    print("Delivery Avilable")
else:
    print("Delivery Unavilable")

num = int(input("Enter an integer"))
if 10<=num<=50:
    print("Inside Range")
else: 
    print("Outside Range")

ammount = int(input("Enter the ammount: "))
otp = int(input("Enter the OTP: "))
if ammount<=50000 and otp == 1234:
    print("Transaction Approved")
else:
    print("Transacton Declined")

