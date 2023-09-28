qty = int(input("Number of tickets: "))

if qty >= 25:
    tprice = 50.0
else:
    if qty > 9:
        tprice = 60.0
    else:
        if qty > 4:
            tprice = 70.0
        else:
            tprice = 75.0
          
total = qty * tprice

print(qty)
print("$", tprice)
print("$", total)
