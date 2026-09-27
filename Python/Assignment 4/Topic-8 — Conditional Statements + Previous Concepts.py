id = input("Enter your ID: ")
degree,year,branch,roll_number = id.split("-")
if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


email = input("Enter Your Email adress: ")
name,extension = email.split("@")
if extension == "gamil.com":
    print("Gmail User")
else:
    print("Other Email Provider")

# Q60 name = input("Enter your full name: ")



num = int(input("Enter a positive integer: "))
if num/10<1:
    print("One Digit number")
elif num/100<1:
    print("Two Digits")
elif num/1000<1:
    print("Three Digits")
else:
    print("Four or More Digits")


price = int(input("Enter Price: "))
quantity = int(input("Enter quantity: "))
subtotal = price*quantity
if subtotal>=5000:
    print(f"Subtotal: {subtotal}, Discount: 20%, Final: {subtotal-(subtotal*(20/100))}")
elif subtotal>=2000:
    print(f"Subtotal: {subtotal}, Discount: 10%, Final: {subtotal-(subtotal*(10/100))}")
else:
    print(f"Subtotal: {subtotal}, Discount: 0%, Final: {subtotal}")


units = int(input("Enter number of units consumed: "))
if units<=100:
    print(f"Units: {units}, Rate: 5Rs, Bill: {units*5}Rs")
elif units<=300:
    print(f"Units: {units}, Rate: 7Rs, Bill: {units*7}Rs")
else:
    print(f"Units: {units}, Rate: 10Rs, Bill: {units*10}Rs")


choice = int(input("Enter your choice: "))
balance = 10000
match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        deposit = int(input("Enter your deposit ammount: "))
        print(f"{deposit} Diposit Successful, Balance: {balance+deposit}")
    case 3:
        withdraw = int(input("Enter the withdraw ammount: "))
        if withdraw<balance:
            print(f"{withdraw}, Withdrawal Successful, Balance: {balance-withdraw}")
        else:
            print(f"{withdraw}, Insufficient Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")


choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Pizza")
        pizza = 250
        pizza_quantity = int(input("Enter no of pizza: "))
        pizza_total = (pizza*pizza_quantity)
        if pizza_total>=500:
            print(f"Pizza Quantity:{pizza_quantity}, Total: {pizza_total}, Discount: {pizza_total*(10/100)}, Final: {pizza_total-(pizza_total*(10/100))}")
        else:
            print(f"Pizza Quantity:{pizza_quantity}, Total: {pizza_total}, Discount: 0.00, Final: {pizza_total}")
    case 2:
        print("Burger")
        burger = 150
        burger_quantity = int(input("Enter no of burger: "))
        burger_total = (burger*burger_quantity)
        if burger_total>500:
            print(f"Burger Quantity: {burger_quantity},Total: {burger_total}, Discount: {burger_total*(10/100)}, Final: {burger_total-(burger_total*(10/100))}")
        else:
            print(f"Burger Quantity: {burger_quantity}, Total: {burger_total},  Discount: 0.00, Final: {burger_total}")
    case 3:
        print("Pasta")
        pasta = 200
        pasta_quantity = int(input("Enter the quantity of pasta: "))
        pasta_total = (pasta*pasta_quantity)
        if pasta_total>500:
            print(f"Pasta Quantity: {pasta_quantity}, Total: {pasta_total}, Discount: {pasta_total*(10/100)}, Final: {pasta_total-(pasta_total*(10/100))}")
        else:
            print(f"Pasta Quantity: {pasta_quantity},Total: {pasta_total}, Discount: 0.00, Final: {pasta_total}")
    case 4:
        print("Sandwich")
        sandwich = 120
        sandwich_quantity = int(input("Enter number of sandwich quantity: "))
        sandwich_total = sandwich*sandwich_quantity
        if sandwich_total > 500:
            print(f"Sandwitch Quantity: {sandwich_quantity}, Total: {sandwich_total},  Discount: {sandwich_total*(10/100)} Final: {sandwich_total-(sandwich_total*(10/100))}")
        else:
            print(f"Sandwitch Quantity: {sandwich_quantity}, Total: {sandwich_total},  Discount: 0.00 Final: {sandwich_total}")
    case _:
        print("Choice is not in the menu")


maths = int(input("Enter maths marks: "))
pyhton = int(input("Enter Python Marks"))
english = int(input("Enter emglish Marks: "))
total = maths+pyhton+english
attendance = int(input("Enter your attendance: "))
if attendance>=75:
    if total>=90:
        print("Outstanding")
    elif total>=75:
        print("Very Good")
    elif total>=60:
        print("Good")
    elif total>40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


distance = int(input("Enter your distance in km: "))
type = input("Enter your ride type: ")
if distance>20:
    match type:
        case "Normal":
            print(f"Fare: {distance*15 + ((distance*15)*(10/100))}")
        case "Premium":
            print(f"Fare: {distance*25 + ((distance*25)*(10/100))}")
else:
    match type:
            case "Normal":
                print(f"Fare: {distance*15}")
            case "Premium":
                print(f"Fare: {distance*25}")


score = int(input("Enter your Entrance Exam Score: "))
twelth = int(input("Enter your 12th percentage: "))
category = input("Enter your cetegory: ")
match category:
    case "General":
        if score>=80:
            if twelth >=75:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")
    case "obc":
        if score>=70:
            if twelth >=70:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")
    case "sc":
        if score>=65:
            if twelth>=65:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")


