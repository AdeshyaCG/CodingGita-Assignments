import math

# Q23
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
count = 0
for i in range(0,len):
    count+=1
print(count)


# Q24
num = int(input("Enter a number: "))
str = str(num)
sum = 0 
for i in range(0, len(str)):
    sum = sum + int(str[i])
print(sum)

# meth 2
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
sum = 0
for i in range(0,len):
    sum = sum+num%10
    num=num//10
print(sum)

# Q25
num = int(input("Enter a number: "))
str = str(num)
prod = 1
for i in range(0, len(str)):
    prod = prod * int(str[i])
print(prod)

# 26
num = int(input("Enter a number: "))
str = str(num)
even = 0
for i in range(0, len(str)):
    if int(str[i])%2==0:
        even = even+1
print(even)

# 27
num = int(input("Enter a number: "))
str = str(num)
sum = 0
for i in range(0, len(str)):
    if int(str[i])%2==0:
        sum = sum + int(str[i])
print(sum)

# 28
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
largest = 0
for i in range(0,len):
    digit = num%10
    if largest < digit:
        largest=digit
        num = num//10
print(largest)

# 29
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
smallest = 9
for i in range(0,len):
    digit = num%10
    if smallest > digit:
        smallest = digit
    num = num // 10
print(smallest)

# Q30
num = int(input("Enter a numebr: "))
len = int(math.log10(num))+1
reverse = 0
for i in range(len):
    digit = num%10
    reverse = reverse*10+digit
    num = num//10
print(reverse)

# Q31
num = int(input("Enter a numebr: "))
original = num
len = int(math.log10(num))+1
reverse = 0
for i in range(len):
    digit = num%10
    reverse = reverse*10+digit
    num = num//10
if reverse == original:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q32
num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
count = 0
len = int(math.log10(num))+1
for i in range(len):
    number = num%10
    if number == digit:
        count = count+1
    num = num//10
print(count)

# 33
num = int(input("Enter a number: "))
len = int(math.log10(num))
for i in range(len):
    num = num//10
print(num)

# 34
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
largest = 0
smallest = 9
for i in range(len):
    digit = num%10
    if largest < digit:
        largest = digit
    elif smallest > digit:
        smallest = digit 
    num = num//10
print(largest-smallest)

# 35
num = int(input("Enter a number: "))
len = int(math.log10(num))+1
for i in range (0, len):
    digit = num%10
    print(digit,i)
    num = num//10

# Q36
num = int(input("Enter a number: "))
original = num
len = int(math.log10(num))+1
sum = 0
for i in range(0,len):
    digit = num%10
    sum = sum+digit**len
    num = num//10
final = sum
if final == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")



