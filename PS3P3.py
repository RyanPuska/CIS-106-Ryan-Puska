total = float(input("Total meal price: $"))

tipA = total*.15
tipB = total*.18
tipC = total*.20
totalA = total+tipA
totalB = total+tipB
totalC = total+tipC

print("Total: $", total)
print("Tip: $", tipA)
print("Total with tip: $", totalA)
print("")
print("Total: $", total)
print("Tip: $", tipB)
print("Total with tip: $", totalB)
print("")
print("Total: $", total)
print("Tip: $", tipC)
print("Total with tip: $", totalC)
