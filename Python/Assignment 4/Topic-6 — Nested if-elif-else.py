num1 = int(input("Enter 1st number: "))
num2 = int(input("Enrer 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1>num2:
    if num1>num3:
        print("A is Greatest")
    elif num1==num3:
        print("A amd C are Equal amd Greatest")
    else:
        print("C is the Greatest")
elif num1==num2:
    if num1 > num3:
        print("A and B are equal and greatest ")
    elif num1==num3:
        print("All are Equal")
    else:
        print("C is Greatest")
else:
    if num2>num3:
        print("B is the greatest")
    elif num2==num3:
        print("B and C are Equal and Greatest")
    else:
        print("C is the Greatest")

marks = int(input("Enter your marks: "))
attendance = int(input("Enter Your attendance"))
if attendance >= 75:
    if marks>90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=40:
        print("D")
    else:
        print("F")
else:
    print("Not Eligible")

salary = int(input("Enter your selary: "))
performance = int(input("Enter the performance: "))
if salary>=30000:
    if performance == 5:
        print("20%")
    elif performance == 4:
        print("15%")
    elif performance == 3:
        print("10%")
    else:
        print("5%")
else:
    print("Not Eligible For Bonus")

age = int(input("Enter your age: "))
distance = int(input("Enter your distance: "))
if age<5:
    print("Free")
elif age<=60:
    if distance<=10:
            print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
else:
    print("Senior")

stock = int(input("Enter the no if produce in the stock avilable: "))
payment = input("Enter the status of the payment: ")
if stock>0:
    if payment=="paid":
        print("Order Confirmed")
    elif payment=="Payment Pending":
        print("Payement Pending")
    else:
        print("Invalid Payenent Status")
else:
    print("Out of Stock")

age = int(input("Enter your age: "))
type = input("Enter your ticket type: ")
if age<5:
    print("Free Teavel")
elif age<=59:
    if type == "AC":
        print("AC Ticket")
    elif type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
else:
    print("Senior Passenger")

