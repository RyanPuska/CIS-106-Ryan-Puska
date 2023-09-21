order = int(input("Books to order: "))
cost = float(input("Cost per book: $"))

total = order * cost

if total <= 50.0:
    fee = 25.0
else:
    fee = 0
  
print("Order total: $", total)
print("Shipping fee: $", fee)