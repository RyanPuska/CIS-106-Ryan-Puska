def CompPercent(make, model, ecode):
  if make + model == "Honda Accord":
    percent = 0.10
    return percent
  if make + model == "Toyota Rav4":
    percent = 0.15
    return percent
  if ecode == "Y":
    percent = 0.30
    return percent
  if ecode == "N":
    percent = 0.05
    return percent
  else:
    percent = 0
    return percent

percent = 0
off = 0
msrp = 0
sum = 0

r = input("Do you want to run the program? ")
while r == "yes":
  make = input("Enter car make: ")
  model = input("Enter car model: ")
  ecode = input("Enter electric vehicle code (Y or N): ")
  msrp = float(input("Enter car MSRP: $"))
  percent = CompPercent(make, model, ecode)
  off = msrp * percent
  newmsrp = msrp - off
  tax = newmsrp * .07
  total = newmsrp + tax
  sum = sum + total
  print("Percent off MSRP: ", percent)
  print("Total price: $", total)
  print("Sum: $", sum)
  r = input("Do you want to run the program? ")