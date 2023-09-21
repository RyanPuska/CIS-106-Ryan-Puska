item = input("Item A or B?: ")
qty = float(input("Quantity: "))

if item == "A":
    unit = 10
else:
    unit = 20
  
extprice = qty * unit

print("Item: " + item)
print("Unit price: $", unit)
print("Extended price: $", extprice)
