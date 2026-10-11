# Q15
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)

# Q16
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
    print(f"{i}! = {fact}")

# Q17
num = int(input("Enter a number: "))
mult = 1
for i in range(2, num+1):
    if i % 2 ==0:
        mult = mult*i
print(mult)

# Q18
num = int(input("Enter a number: "))
mult = 1
for i in range(2, num+1):
    if i % 2 !=0:
        mult = mult*i
print(mult)

# Q19
num = int(input("Enter a number: "))
mult = 1
for i in range(num,1,-2):
    if i%2==0:
        mult = mult*i
print(mult)

# Q20
num = int(input("Enter a number: "))
square = 0
for i in range(1,num+1):
    square = square + i**2
print(square)

# Q21
num = int(input("Enter a number: "))
cube = 0
for i in range(1, num+1):
    cube = cube+(i**3)
print(cube)

# Q22
num = int(input("Enter a number: "))
fact = 1
add = 0
for i in range(1, num+1):
    fact = fact*i
    add = add + fact
print(add)

