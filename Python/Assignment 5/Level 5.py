# Q37
word = input("Enter a string: ")
for i in range(len(word)):
    print(i,word[i])

# Q38
word = input("Enter a string: ") 
count = 0
for i in range(len(word)):
    count = count+1
print(count)

# Q39
word = input("Enter a string: ")
even = 0
consonent = 0
space = 0
for i in range(len(word)):
    match word[i]:
        case "a" | "e" | "i"| "o" | "u" :
            even = even+1
        case " ":
            space = space + 1
        case _:
            consonent = consonent+1
print(f"Vovels = {even}")
print(f"Consonents = {consonent}")

# Q40
word = input("Enter a number: ")
target = input("Enter your target word: ")
count = 0
for i in range(len(word)):
    if target == word[i]:
        count = count+1
print(count)

# Q41
word = input("Enter a string: ")
target = input("Enter a target word: ")
position = 0
for i in range(len(word)):
    if target == word[i]:
        position = i
        break
else:
    print("Not Found")
print(position)

# Q42
word = input("Enter a string: ")
upper = 0
lower = 0
for i in range(len(word)):
    if word[i] == word[i].upper():
        upper +=1
    else:
        lower +=1
print(f"Uppercase = {upper}, Lowercase = {lower}")

# Q43
word = input("Enter a string: ")
for i in range(len(word)):
    print(word[i], ord(word[i]))

# Q44
word = input("Enter a string: ")
new = ""
for i in range(len(word)):
    if word[i] != "a"or"e"or"i"or"o"or"u":
        new = new + word[i]
print(new)

