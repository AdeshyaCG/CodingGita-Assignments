import math

# Q53
num = int(input("Etner a number: "))
len = int(math.log10(num))+1
largest = 0
for i in range(num):
    digit = num%10
    if largest < digit:
        digit = largest
    num = num//10

# Q54
word = input("Enter a string: ")
word2 = word
current = 0
largest = 0
for i in word:
    if i in word2:
        current+=1
    current = largest
print (largest)