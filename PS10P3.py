def report(sales):
  percent = 0
  if sales > 100000:
    percent = 0.10
  elif sales <= 100000:
    percent = 0.05   
  com = sales*percent
  ny = sales * 1.05
  return com, ny

lname = input("Enter last name: ")
sales = float(input("Enter sales: "))
com,ny = report(sales)
print("Last name: ", lname)
print("Your commission: $", com)
print("Next year's target: $", ny)
