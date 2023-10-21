def CompTuit(code):
  if code == "I":
    price = 250
    return price
  if code == "O":
    price = 550
    return price
  else:
    price = 0
    return price

price = 0
totaltuit = 0
tuit = 0

r = input("Do you want to compute tuition? ")
while r == "yes":
  lname = input("Enter last name: ")
  code = input("Enter district code: ")
  hrs = float(input("Enter number of credit hours: "))
  price = CompTuit(code)
  print("Price: $", price, "per credit hour")
  tuit = (price * hrs)
  print("Tuition owed: $", tuit)
  r = input("Do you want to compute tuition? ")
  totaltuit = totaltuit + tuit

print("Total tuition owed: $", totaltuit)