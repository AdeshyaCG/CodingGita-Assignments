menu = int(input("Enter a menu number: "))
match menu:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")

num = int(input("Enter a number: "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter your operator: ")
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Invalid Operator")

color = input("Enter the color of the trafic light: ")
match color:
    case "red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case "purple":
        print("Invalid Signal")

grade = input("Enter your grade: ")
match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performamce")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Faild")
    case _:
        print("Invalid Grade")

service = int(input("Enter your service code: "))
match service:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Costomer Support")
    case _:
        print("Invalid Service")

month = int(input("Enter your month number: "))
match month:
    case 1:
        print("January")
    case 2:
        print("Febuary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

file_type = input("Enter your File Type: ")
match file_type:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")

