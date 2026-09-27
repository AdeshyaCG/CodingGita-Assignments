grade = int(input("Enrter your grade: "))
if 100>=grade>=90:
    print("A")
elif 80<=grade<=89:
    print("B")
elif 70<=grade<=79:
    print("C")
elif 60<=grade<=69:
    print("D")
else:
    print("F")

temp = int(input("Enter Temperature in Celcius"))
if temp>40:
    print("Very Hot")
elif 30<=temp<=39:
    print("Hot")
elif 20<=temp<=29:
    print("Warm")
else:
    print("Cold")

signal = input("Enter signal color: ")
if signal == "red":
    print("Stop")
elif signal =="yellow":
    print("Wait")
elif signal=="green":
    print("go")
else:
    print("Invalid Signal")

usage = int(input("Enter the Usage of electricity: "))
if 0<=usage<=100:
    print("Low Usage")
elif 101<=usage<=300:
    print("Midium Usage")
elif 301<=usage<=500:
    print("High Usage")
else:
    print("Very High Usage")

age = int(input("Enter the age for the ticket category"))
if age<5:
    print("Free Ticket")
elif 5<=age<=12:
    print("Child Ticket")
elif 13<=age<=59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

bmi = float(input("Enter BMI Category: "))
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<=24.9:
    print("Normal")
elif 25<=bmi<=29.9:
    print("Overwaight")
else:
    print("Obese")

month = int(input("Enter month number: "))
match month:
    case 1|3|5|7|8|10|12:
        print("31 Days")
    case 4|6|9|11:
        print("30 Days")
    case 2:
        print("28 or 29 Days")
    case _:
        print("Invalid Month")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter operaor: ")
if operator =="+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)

day = int(input("Enter day number: "))
if day == 1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day")

performance = int(input("Enter your score: "))
if performance>=90:
    print("Excelent")
elif 75<=performance<=89:
    print("Very Good")
elif 60<=performance<=74:
    print("Good")
elif 40<=performance<=59:
    print("Average")
else:
    print("Needs Improvement")

