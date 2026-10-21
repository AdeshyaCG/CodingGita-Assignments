# Q46
n = int(input("Enter a number: "))
last_digit = n%10
print(last_digit)
first_digit = n
while first_digit>=0:
    first_digit = first_digit//10
print(first_digit)

# Q47
n = int(input("Enter a number: "))
count = 0
if n == 0:
    print(1)
else:
    while n>0:
        current = n%10
        if current%2==0:
            count +=1
        n = n//10
    print(count)

# Q48
n = int(input("Enter a number: "))
count = 0
while n>0:
    current = n%10
    if current%2 != 0:
        count +=1
    n = n//10
print(count) 

# Q49
n = int(input("Enter a number: "))
sum = 0
while n>0:
    current = n%10
    if current%2 == 0:
        sum = sum+n%10
    n = n//10
print(sum)

# Q50
n = int(input("Enter a number: "))
largest = 0
while n>0:
    current = n%10
    if largest<current:
        largest = current
    n = n//10
print(largest)

# Q51
n = int(input("Enter a number: "))
smallest = 9
while n>0:
    current = n%10
    if smallest > current:
        smallest = current
    n = n//10
print(smallest)

# Q52
n = int(input("Enter a number: "))

original = n
rev = 0

while n > 0:
    t = n % 10
    rev = rev * 10 + t
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q53
n = int(input("Enter a number: "))
target = int(input("Enter the target number: "))
count = 0
if n == 0 and target == 0:
    print(1)
else:  
    while n >0:
        current = n%10
        if target == current:
            count +=1
        n = n//10
    print(count)

# # Q54
# n = int(input("Enter a number: "))
# while n>0:
    
# Q55
n = int(input("Enter a number: "))
original = n
last_digit = original%10
sum = 0
if n>100:
    while original>=10:
        first_digit = original//10
        original = original//10
print(f"First digit: {first_digit}, Last Digit: {last_digit}, Sum of first and last digit are: {first_digit+last_digit}")
if n>100:
    while n>0:
        sum = sum+n%10
        n = n//10
print(f"Sum of the middle term: {sum-first_digit-last_digit}")

# 56
