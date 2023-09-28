principle = float(input("Principle amount:"))
mature = float(input("Year to maturity: "))

if principle > 100000 and mature == 5:
    intrate = 0.06
else:
    if principle > 50000 and mature == 10:
        intrate = 0.05
    else:
        if principle > 50000 and mature == 5:
            intrate = 0.04
        else:
            intrate = 0.02
          
intamt = principle * intrate

print(principle)
print(str(intrate * 100) + "%")
print(intamt)
