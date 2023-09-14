fixedcost = float(input("Fixed costs: $"))
priceunit = float(input("Price per unit: $"))
costunit = float(input("Cost per unit: $"))

even = fixedcost/(priceunit-costunit)

print("Your break even point is:", even)