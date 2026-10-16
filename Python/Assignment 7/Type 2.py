# Q21
n = int(input("Enter a number: "))
i = 0
while n>=i:
    print(i)
    i += 1
# Q22
num = int(input("Enter a number: "))
while num>=1:
    print(num)
    num -=1

# Q23
n = int(input("Enter a number: "))
i = 2
if n%2==0:
    while n>=i:
        print(i)
        i+=2
else:
    while n>i:
        print(i)
        i+=2

# Q24
n = int(input("Enter a number: "))
i = 1
if n%2==0:
    while n>i:
        print(i)
        i+=2
else:
    while n>=i:
        print(i)
        i+=2

# Q25
K = int(input("Enter first number: "))
N = int(input("Enter second number: "))
current = K
while current <= N:
    print(current, end=" ")
    current += K

# Q26
num = int(input("Enter a number: "))
i = 1
while i<=10:
    print(f"{num} X {i} == {num*i}")
    i +=1

# Q27
start = int(input("Enter a number: "))
step = int(input("Enter step number: "))
result = start
i = 1
while i<=5:
    print(result)
    i +=1
    result = result+step

# Q28
N = 5
total = 0
current = 1
while current <= N:
    total += current
    current += 1

print(total)

# Q29
num = int(input("Enter a number: "))
current = 2
if num%2==0:
    i = 2
    sum = 0
    while current<=num:
        sum = sum+current
        current= current+2
    print(sum)
else:
    i = 2
    sum = 0
    while current<num:
        sum = sum+current
        current= current+2
    print(sum)

# Q30
num = int(input("Enter a number: "))
current = 2
if num%2!=0:
    i = 2
    sum = 0
    while current<num:
        sum = sum+current
        current= current+2
    print(sum)
else:
    i = 2
    sum = 0
    while current<=num:
        sum = sum+current
        current= current+2
    print(sum)

# Q31
price = int(input("Enter the price: "))
initial = price
quantity = int(input("Enter the quantity: "))
count = 0
total = price*quantity
while price<total:
    count+=1
    price = price+ initial
print(price)

# Q32
daily_saving = int(input("Enter daily saving: "))
days = int(input("Enter days: "))
total_saved = 0
day = 1
while day <= days:
    total_saved += daily_saving
    day += 1
print(total_saved)

# Q33
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = 1
count = 0
while count < power:
    result *= base
    count += 1
print(result)

# Q34
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Q35
start = int(input("Enter start: "))
end = int(input("Enter end: "))
total = 0
current = start
while current <= end:
    total += current
    current += 1
print(total)

# Q36
n = int(input("Enter a positive even number: "))
current = n
while current >= 2:
    print(current)
    current -= 2

# Q37
n = int(input("Enter a number: "))
current = n
while current > 0:
    current = current // 2
    print(current)

# Q38
n = int(input("Enter a number: "))
steps = 0
while n > 0:
    n -= 3
    steps += 1
print(steps)

# Q39
saved = int(input("Enter saved amount: "))
daily_amount = int(input("Enter daily amount: "))
target = int(input("Enter target amount: "))
days = 0
while saved < target:
    saved += daily_amount
    days += 1
print(days)

# Q40
