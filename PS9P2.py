def CompSqFt(length, width, height):
  sqft = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
  return sqft

sqft = 0
gal = 0

r = input("Do you want to run the program? ")
while r == "yes":
  length = float(input("Enter length: "))
  width = float(input("Enter width: "))
  height = float(input("Enter height: "))
  sqft = CompSqFt(length, width, height)
  print("Square footage of the room: ", sqft)
  gal = sqft / 50
  print("Gallons of paint needed: ", gal)
  r = input("Do you want to run the program? ")