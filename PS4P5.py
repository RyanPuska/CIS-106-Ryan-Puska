lname = input("Enter last name: ")
gpay = input("Enter your gross income: ")
numdep = input("Enter number of dependents: ")

adjgross = float(gpay) - 12000*float(numdep)

if adjgross > 50000:
  tax = adjgross*.2
else:
  tax = adjgross*.1

if tax < 0:
  tax = 100

print(lname)
print("Gross income: $", gpay)
print("Number of dependents: ", numdep)
print("Adjusted gross: $", adjgross)
print("Income tax: $", tax)


  