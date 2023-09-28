partno = int(input("Part number: "))
qty = float(input("Quantity: "))

if partno == 10 or partno == 55:
    unitprice = 1.0
else:
    if partno == 99:
        unitprice = 2.0
    else:
        if partno == 80 or partno == 70:
            unitprice = 3.0
        else:
            unitprice = 5.0
          
total = unitprice * qty

print(partno)
print(qty)
print(unitprice)
print(total)
