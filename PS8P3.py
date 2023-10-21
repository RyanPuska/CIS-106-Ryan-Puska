def CompMpg(miles, gallons):
  mpg = miles/gallons
  return mpg

count = 0

r = input("Do you want to compute miles per gallon? ")
while r == "yes":
  city = (input("Enter destination city: "))
  miles = float(input("Enter number of miles: "))
  gallons = float(input("Enter number of gallons: "))
  mpg = CompMpg(miles, gallons)
  print("Miles per gallon: ", mpg)
  r = input("Do you want to compute miles per gallon? ")
  count = count + 1

print("Number of entries made: ", count)