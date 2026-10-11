# Q7
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
sum=0
for i in range(num1, num2+1):
    sum = sum+i
print(sum)

# Q8
num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if i % 3 == 0:
        count += 1
print(count)

# Q9
num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if i % 4 == 0:
        count += i
print(count)

# Q10
num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        count+=1
print(count)

# Q11
num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    if i % 3 != 0:
        count = count+i
print(count)

# Q12
num = int(input("Enter a number: "))
even = 0
odd = 0
for i in range(1, num+1):
    if i%2==0:
        even +=1
    else:
        odd +=1
print(f"Even = {even}, Odd = {odd}") 

# Q13
num = int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
    sum = sum+i
    print(sum)

# Q14
num = int(input("Enter a number: "))
product = 1
for i in range(1, num+1):
    product = product*i
    print(product)