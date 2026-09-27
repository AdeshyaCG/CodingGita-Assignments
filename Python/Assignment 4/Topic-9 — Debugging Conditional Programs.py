# Q69. Debug the Condition
# Find and correct the error:

# age = input("Enter age: ")

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")
# The program should correctly compare the entered age as a number.

# Test Cases
# 20 → Eligible
# 15 → Not Eligible
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Q70. Debug the Nested Condition
# Find and correct the error:

# marks = int(input("Enter marks: "))

# if marks >= 40:
#     if marks >= 90:
#         print("A")
#     elif marks >= 75:
#         print("B")
# else:
#     print("Fail")
# Test the program for marks 95, 80, 50, and 30.

# Explain why the current program does not give the correct result for every passing range, then correct it.

# Test Cases
# 95 → A
# 80 → B
# 50 → Pass
# 30 → Fail

marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")