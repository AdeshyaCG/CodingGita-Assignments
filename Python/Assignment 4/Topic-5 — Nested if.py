user = input("Enter your name: ")
passw = int(input("Enter password: "))
if user == "admin":
    if passw == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

age = int(input("Enter your age: "))
test_status = input("Enter your Test Status: ")
if age >=18:
    if test_status == "pass":
        print("Licence Aproved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")

balance = int(input("Enter your balance"))
ammount = int(input("Enter your withrawal ammount: "))
if balance>ammount:
    if ammount%100==0:
        print("Withdrawal Successful")
    else:
        print("Enter Ammount in Multiple of 100")
else:
    print("Insufficient Balance: ")

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
if attendance>75:
    if marks > 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")

type = input("Enter account type: ")
balance = int(input("Enter balance: "))
if type == "saving":
    if balance>1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported account")

ammount = int(input("Enter order ammount: "))
methord = input("Enter Payment methord:  ")
if ammount>500:
    if type == "card":
        print("Card Payment Acceped")
    elif type == "UPI":
        print("UPI Payment Accepeted")
    else:
        print("Unsuported Payment Methord")
else:
    print("Minimum Order Ammount Not Reached")

year = int(input("Ente your collage year: "))
attendance = int(input("Enter your attendance: "))
if year == 2 or year == 3 or year ==4:
    if attendance > 75:
        print("Room Eligible")
    else:
        print("Attandance Too Low")
else:
    print("Not Eligible By year")

plan = input("Enter your current internet plan: ")
usage = int(input("Enter your usages in Gbps: "))
if plan=="Basic":
    if usage>100:
        print("Recommend Upgrade")
    else:
        print("Basic plan is sufficient")
else:
    print("Already on the Higher Plan")

