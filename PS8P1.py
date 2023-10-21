def CompExtPrice(qty, unitprice):
  extprice = qty*unitprice

  if extprice > 10000:
    discamt = extprice*0.10
  else:
    discamt = 0.0
    
  return extprice

totalextprice = 0.0
r = input("Do you want to compute extended price? ")
while r == "yes":
  qty = float(input("Enter quantity: "))
  unitprice = float(input("Enter unit price: "))
  extprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extprice
  print("Extended Price is $", extprice)
  r = input("Do you want to compute extended price? ")

print("Total Extended Price is $", totalextprice)