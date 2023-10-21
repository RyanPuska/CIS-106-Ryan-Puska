def CompPayrate(code):
  if code == "L":
    payrate = 25
    return payrate
  if code == "A":
    payrate = 30
    return payrate
  if code == "J":
    payrate = 50
    return payrate
  else:
    payrate = 0
    return payrate

payrate = 0
totalgpay = 0
gpay = 0
ot = 0
otpay = 0

r = input("Do you want to compute pay rate? ")
while r == "yes":
  lname = input("Enter last name: ")
  code = input("Enter job code: ")
  hrs = float(input("Enter number of hours worked: "))
  ot = float(input("How many hours of overtime? "))
  otpay = ot * .5
  payrate = CompPayrate(code)
  print("Pay rate: $", payrate, "/hr")
  gpay = (payrate * hrs) + otpay
  print("Gross pay: $", gpay)
  r = input("Do you want to compute pay rate? ")
  totalgpay = totalgpay + gpay

print("Total gross pay: $", totalgpay)