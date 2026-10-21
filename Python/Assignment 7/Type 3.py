# Q41
n = int(input("Enter a number: "))
count = 0
while n>0:
    n = n//10
    count = count+1
print(count)

# Q42
n = int(input("Enter a number: "))
sum = 0
while n>0:
    sum = sum+n%10
    n = n//10
print(sum)

# Q43
n = int(input("Enter a number: "))
current = 0
while n>0:
    current = current*10 + n%10
    n = n//10
print(current)

# Q44
n = int(input("Enter a number: "))
prod = 1
current =0
while n>0:
    current = n%10
    prod = prod*current
    n = n//10
print(prod)

# Q45
n = int(input("Enter a number: "))
while n>0:
    rev = n%10
    n = n//10
    print(rev)

# Q46
