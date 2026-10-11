# 45
word = input("Enter a string: ")
middle = len(word)//2
print(word[middle])

# 46
word = input("Enter a string: ")
first = ""
second = ""
for i in range(len(word)):
    if i < len(word)//2:
        first = first + word[i]
    else:
        second = second + word[i]
print(f"First Half: {first}")
print(f"Second Half: {second}")

# Q47
word = input("Enter a string: ")
first = ""
second = ""
middle = ""
for i in range (len(word)):
    if len(word)%2==0:
        if i < len(word)//2:
            first = first + word[i]
        else:
            second = second + word[i]
    else:
        if i<len(word)//2:
            first = first+word[i]
        elif i ==len(word)//2:
            middle = middle + word[i]
        else:
            second = second + word[i]
print(f"First Half: {first}")
print(f"Middle: {middle}")
print(f"Second Half: {second}")

# Q48
word = input("Enter a string: ")
first = ""
second = ""
for i in range(len(word)):
    if i < len(word)//0:
        first = first + word[i]
    else:
        second = second + word[i]
if first == second:
    print("Equal Halves")
else:
    print("Different Halves")

# Q49


# Q50
word = input("Enter a string: ")
even = ""
for i in range(len(word)):
    if i%2==0:
        even = even+word[i]
print(even)

# Q51
word = input("Enter a string: ")
even = 0
odd =  0
for i in range(len(word)):
    if i%2==0:
        even = even+1
    else:
        odd = odd+1
print(f"Even Index = {even}, Odd Index = {odd}")

# Q52
word = input("Enter a string: ")
new = ""

for i in range(0, len(word), 2):
    new = new + word[i + 1] + word[i]

print(new)

