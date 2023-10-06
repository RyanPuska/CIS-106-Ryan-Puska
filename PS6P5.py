numorders = 0
sumdiscamt = 0
print("Do you want to calculate total order with discount? ")
response = input()
while response == "yes":
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: $"))
    extprice = qty * price
    if extprice > 10000:
        discamt = extprice * 0.25
    else:
        discamt = extprice * 0.1
    totalorder = extprice - discamt
    sumdiscamt = sumdiscamt + discamt
    numorders = numorders + 1
    print("Extended price is: $", extprice)
    print("Discount amount: $", discamt)
    print("Total order amount: $" , totalorder)
    print("Do you want to enter another order? ")
    response = input()
print("Total discounts given: $", sumdiscamt)
print("Number of orders: " , numorders)
