shareprice = float(input("Price per share: $"))
stockprice = float(input("Current stock price: $"))
stockquant = float(input("Quantity of stock: "))

value = (stockprice-shareprice)*stockquant

if value < 0:
  print("You are losing money.")
else:
  print("You are gaining money.")