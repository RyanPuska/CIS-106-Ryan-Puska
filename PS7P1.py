response = input("Do you want to run this program? ")
while response == "yes":
  pamt = float(input("Enter principle amount: "))
  intrate = float(input("Enter interest rate: "))
  totint = 0.0
  print("Year     Beginning Balance      End Balance")

  for x in range(1,6,1):
    anint = pamt * intrate
    totint = totint + anint
    endbal = pamt + anint
    print(x, "      ", pamt, "              ", endbal)
    pamt = endbal

  print("Accumulated interest: $", totint)
  response = input("Do you want to run this program again? ")