def compTotal(qty,price):
  global total
  global tax
  total = qty*price
  tax = total*0.07
  return total,tax

total = 0
tax = 0
qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))
total,tax = compTotal(qty,price)
print("Total:",total)
print("Tax:",tax)