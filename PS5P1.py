qty = float(input("Quantity of widgets: "))

if qty > 10000:
    price = 10
else:
    if qty > 5000:
        price = 20
    else:
        price = 30
      
extprice = qty * price
tax = extprice * 0.07
total = extprice + tax

print("Extended price: $", extprice)
print("Tax: $", tax)
print("Total: $", total)