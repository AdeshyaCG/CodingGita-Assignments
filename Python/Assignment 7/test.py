# price = int(input("Enter the price: "))
# initial = price
# quantity = int(input("Enter the quantity: "))
# count = 0
# total = price*quantity
# while price<total:
#     count+=1
#     price = price+ initial
# print(price)

# n = int(input("Enter a number: "))
# sum = 0
# while n>0:
#     sum = sum+n%10
#     n = n//10
# print(sum)

# n = int(input("Enter a number: "))
# current = 0
# while n>0:
#     current = current*10 + n%10
#     n = n//10
# print(current)
# n = int(input("Enter a number: "))
# prod = 1
# current =0
# while n>0:
#     current = n%10
#     prod = prod*current
#     n = n//10
# print(prod)

# n = int(input("Enter a number: "))
# while n>0:
#     rev = n%10
#     n = n//10
#     print(rev)

# n = int(input("Enter a number: "))
# count = 0
# if n == 0:
#     print(1)
# else:
#     while n>0:
#         current = n%10
#         if current%2==0:
#             count +=1
#         n = n//10
#     print(count)

# n = int(input("Enter a number: "))
# count = 0
# while n>0:
#     current = n%10
#     if current%2 != 0:
#         count +=1
#     n = n//10
# print(count) 

# n = int(input("Enter a number: "))
# sum = 0
# while n>0:
#     current = n%10
#     if current%2 == 0:
#         sum = sum+n%10
#     n = n//10
# print(sum)

# n = int(input("Enter a number: "))
# largest = 0
# while n>0:
#     current = n%10
#     if largest<current:
#         largest = current
#     n = n//10
# print(largest)

# n = int(input("Enter a number: "))
# smallest = 9
# while n>0:
#     current = n%10
#     if smallest > current:
#         smallest = current
#     n = n//10
# print(smallest)
# n = int(input("Enter a number: "))

# original = n
# rev = 0

# while n > 0:
#     t = n % 10
#     rev = rev * 10 + t
#     n = n // 10

# if original == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# n = int(input("Enter a number: "))
# target = int(input("Enter the target number: "))
# original = n
# count = 0
# if n == 0 and target == 0:
#     print(1)
# else:  
#     while n >0:
#         current = n%10
#         if target == current:
#             count +=1
#         n = n//10
#     print(count)
# n = int(input("Enter a number: "))
# original = n
# last_digit = original%10
# sum = 0
# if n>100:
#     while original>=10:
#         first_digit = original//10
#         original = original//10
# print(f"First digit: {first_digit}, Last Digit: {last_digit}, Sum of first and last digit are: {first_digit+last_digit}")
# if n>100:
#     while n>0:
#         sum = sum+n%10
#         n = n//10
# print(f"Sum of the middle term: {sum-first_digit-last_digit}")

# n = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i<=n:
#     fact = fact*i
#     if n == fact:
#         print("Yes")
#         break
#     i +=1
# else:
#     print(n, "No")

n = int(input("Enter a number: "))
fact = 1
i = 1
while i<=n:
    fact = fact*i
    if fact<=n:
        print(i)
        break
    i +=1