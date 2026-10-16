price = int(input("Enter the price: "))
initial = price
quantity = int(input("Enter the quantity: "))
count = 0
total = price*quantity
while price<total:
    count+=1
    price = price+ initial
print(price)