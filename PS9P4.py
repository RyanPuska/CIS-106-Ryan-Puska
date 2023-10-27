def TicketPrice(miles):
  if miles >= 30:
    ticket = 12
    return ticket
  if miles >= 20 and miles <= 29:
    ticket = 10
    return ticket
  if miles >= 10 and miles <= 19:
    ticket = 8
    return ticket
  else:
    ticket = 5
    return ticket

sum = 0
ticket = 0

r = input("Do you want to run this program? ")
while r == "yes":
  lname = input("Enter your last name: ")
  miles = int(input("How many miles from downtown Chicago? "))
  ticket = TicketPrice(miles)
  print("Your train ticket price is: $" + str(TicketPrice(miles)))
  r = input("Do you want to run this program again? ")
  sum = sum + ticket
print("Sum: $", sum)
