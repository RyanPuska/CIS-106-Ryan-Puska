def computeDisc(qty, price, discrate): 
  total = qty * price
  discamt = total * discrate
  discprice = total - discamt
  return total, discamt, discprice

qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discrate = float(input("Enter discount rate: "))
discprice, discamt, total = computeDisc(qty, price, discrate)

print("Quantity: ", qty)
print("Price: $", price)
print("Discounted amount: $", discamt)
print("Discounted price: $", discprice)


  