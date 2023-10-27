def AssessedValue(county):
  if county == "Cook":
    percent = 0.90
    return percent
  if county == "DuPage":
    percent = 0.80
    return percent
  if county == "McHenry":
    percent = 0.75
    return percent
  if county == "Kane":
    percent = 0.60
    return percent
  else:
    percent = 0.7
    return percent

suma = 0
summ = 0
avalue = 0

r = input("Do you want to run this program? ")
while r == "yes":
  mvalue = float(input("Enter market value: "))
  county = input("House county: ")
  percent = (AssessedValue(county))
  avalue = percent * mvalue
  print("The market value is: $", mvalue)
  print("The assessed value is: $", avalue)
  r = input("Do you want to run this program again? ")
  suma = suma + avalue
  summ = summ + mvalue
print("Assessed value sum: $", suma)
print("Market value sum: $", summ)
