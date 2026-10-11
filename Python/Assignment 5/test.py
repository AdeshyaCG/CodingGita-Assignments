# # num = int(input("Enter a number: "))
# # count = 0
# # for i in range(1, num+1):
# #     if i % 3 != 0:
# #         count = count+i
# # print(count)
# num = int(input("Enter a number: "))
# even = 0
# odd = 0
# for i in range(1, num+1):
#     if i%2==0:
#         even +=1
#     else:
#         odd +=1
# print(f"Even = {even}, Odd = {odd}") 
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1,num+1):
#     sum = sum+i
#     print(sum)
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact*i
#     print(f"{i}! = {fact}")
# num = int(input("Enter a number: "))
# mult = 1
# for i in range(2, num+1):
#     if i % 2 ==0:
#         mult = mult*i
# print(mult)
# num = int(input("Enter a number: "))
# mult = 1
# for i in range(2, num+1):
#     if i % 2 !=0:
#         mult = mult*i
# print(mult)
# num = int(input("Enter a number: "))
# mult = 1
# for i in range(num,1,-2):
#     if i%2==0:
#         mult = mult*i
# print(mult)
# num = int(input("Enter a number: "))
# square = 0
# add = 0
# for i in range(1,num+1):
#     square = square + i**2
# print(square)
# num = int(input("Enter a number: "))
# cube = 0
# for i in range(1, num+1):
#     cube = cube+(i**3)
# print(cube)
# num = int(input("Enter a number: "))
# fact = 1
# add = 0
# for i in range(1, num+1):
#     fact = fact*i
#     add = add + fact
# print(add)
# num = int(input("Enter a number: "))
# str = str(num)
# sum = 0 
# for i in range(0, len(str)):
#     sum = sum + int(str[i])
# print(sum)

# num = int(input("Enter a number: "))
# count = 0
# for i in range(100):
#     num = num // 10
#     count = count + 1
# print(count)
# num = int(input("Enter a number: "))
# str = str(num)
# sum = 0
# for i in range(0, len(str)):
#     if int(str[i])%2==0:
#         sum = sum + int(str[i])
# print(sum)
import math
# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# sum = 0
# for i in range(0,len):
#     sum = sum+num%10
#     num=num//10
# print(sum)
# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# largest = 0
# for i in range(0,len):
#     digit = num%10
#     if largest < digit:
#         largest=digit
#         num = num//10
# print(largest)

# num = int(input("Enter a numebr: "))
# len = int(math.log10(num))+1
# reverse = 0
# for i in range(len):
#     digit = num%10
#     reverse = reverse*10+digit
#     num = num//10
# print(reverse)

# num = int(input("Enter a numebr: "))
# original_val=num
# len = int(math.log10(num))+1
# reverse = 0
# for i in range(len):
#     digit = num%10
#     reverse = reverse*10+digit
#     num = num//10
# print(reverse,num)
# if reverse == num = int(input("Enter a numebr: "))
# len = int(math.log10(num))+1
# reverse = 0
# for i in range(len):
#     digit = num%10
#     reverse = reverse*10+digit
#     num = num//10
# if reverse == num:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# num = int(input("Enter a number: "))
# digit = int(input("Enter a digit: "))
# count = 0
# len = int(math.log10(num))+1
# for i in range(len):
#     number = num%10
#     if number == digit:
#         count = count+1
#     num = num//10
# print(count)
# num = int(input("Enter a number: "))
# len = int(math.log10(num))
# for i in range(len):
#     num = num//10
# print(num)
# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# largest = 0
# smallest = 0
# for i in range(len):
#     digit = num%10
#     if largest < digit:
#         largest = digit
#         print(largest)
#     elif smallest > digit:
#         digit = smallest
#         print(smallest)
# print(largest-smallest)

# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# largest = 0
# smallest = 9
# for i in range(0,len):
#     digit = num%10
#     if largest < digit:
#         largest=digit
#     if smallest > digit:
#         smallest = digit
#     num = num // 10
# print(largest-smallest)

# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# largest = 0
# smallest = 9
# for i in range(len):
#     digit = num%10
#     if largest < digit:
#         largest = digit
#     if smallest > digit:
#        smallest = digit 
#     num = num//10
# print(largest,smallest)
# print(largest-smallest)

# num = int(input("Enter a number: "))
# len = int(math.log10(num))+1
# for i in range (1, len+1):
#     digit = num%10
#     print(digit,i)
#     num = num//10
# num = int(input("Enter a number: "))
# original = num
# len = int(math.log10(num))+1
# sum = 0
# for i in range(0,len):
#     digit = num%10
#     sum = sum+digit**len
#     num = num//10
# final = sum
# if final == original:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
# word = input("Enter a string: ")
# for i in range(len(word)):
#     print(i,word[i])
# word = input("Enter a string: ") 
# count = 0
# for i in range(len(word)):
#     count = count+1
# print(count)
# word = input("Enter a string: ")
# even = 0
# consonent = 0
# space = 0
# for i in range(len(word)):
#     match word[i]:
#         case "a" | "e" | "i"| "o" | "u" :
#             even = even+1
#         case " ":
#             space = space + 1
#         case _:
#             consonent = consonent+1
# print(f"Vovels = {even}")
# print(f"Consonents = {consonent}")
# word = input("Enter a number: ")
# target = input("Enter your target word: ")
# count = 0
# for i in range(len(word)):
#     if target == word[i]:
#         count = count+1
# print(count)
# word = input("Enter a string: ")
# target = input("Enter a target word: ")
# position = 0
# for i in range(len(word)):
#     if target == word[i]:
#         position = i
#         break
# else:
#     print("Not Found")
# print(position)
# word = input("Enter a string: ")
# upper = 0
# lower = 0
# for i in range(len(word)):
#     if word[i] == word[i].upper():
#         upper +=1
#     else:
#         lower +=1
# print(f"Uppercase = {upper}, Lowercase = {lower}")
# word = input("Enter a string: ")
# for i in range(len(word)):
#     print(word[i], ord(word[i]))
# word = input("Enter a string: ")
# new = ""
# for i in range(len(word)):
#     if word[i] not in "aeiou":
#         new = new + word[i]
# print(new)
# word = input("Enter a string: ")
# middle = len(word)//2
# print(word[middle])
# word = input("Enter a string: ")
# first = ""
# second = ""
# for i in range(len(word)):
#     if i < len(word)//2:
#         first = first + word[i]
#     else:
#         second = second + word[i]
# print(f"First Half: {first}")
# print(f"Second Half: {second}")
# word = input("Enter a string: ")
# first = ""
# second = ""
# middle = ""
# for i in range (len(word)):
#     if len(word)%2==0:
#         if i < len(word)//2:
#             first = first + word[i]
#         else:
#             second = second + word[i]
#     else:
#         if i<len(word)//2:
#             first = first+word[i]
#         elif i ==len(word)//2:
#             middle = middle + word[i]
#         else:
#             second = second + word[i]
# print(f"First Half: {first}")
#     print(f"Middle: {middle}")
#     print(f"Second Half: {second}")
# word = input("Enter a string: ")
# first = ""
# second = ""
# for i in range(len(word)):
#     if i < len(word)//2:
#         first = first + word[i]
#     else:
#         second = second + word[i]
# if first == second:
#     print("Equal Halves")
# else:
#     print("Different Halves")
# word = input("Enter a string: ")
# first =""
# second = ""
# for i in range(len(word)//2):
#     first = first+word[i]
# for j in range(len(word), (len(word)//2)-1,-1):
#     second = second + word[j]
# print(first)
# print(second)
# word = input("Enter a string: ")
# even = ""
# for i in range(len(word)):
#     if i%2==0:
#         even = even+word[i]
# print(even)

# word = input("Enter a string: ")
# new = ""

# for i in range(0, len(word), 2):
#     new = new + word[i + 1] + word[i]

# print(new)

word = input("Enter a string: ")
word2 = 'qwertyuiopasdfghjklzxcvbnm'
l = []
wo = []
current = 0
largest = 0
for i in word:
    wo.append(i)
print(wo)

for i in wo:
    if i in word2:
        current +=1
        l.append(current)
print(l)
# if current > largest:
    # current = largest
# print (largest)