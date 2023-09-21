qty = float(input("Quantity: "))

if qty >= 1000:
    up = 3.0
else:
    up = 5.0

extprice = qty * up
tax = extprice * 0.07
total = extprice + tax

print("Quantity Ordered: ", qty)
print("Unit Price $", up)
print("Extended Price is $",extprice)
print("Tax is $", tax)
print("Total Order $", total)
