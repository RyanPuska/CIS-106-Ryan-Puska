def CompForecast(month):
  if month == "Jan" or month == "Feb" or month == "Mar":
    percent = 0.10
    return percent
  if month == "Apr" or month == "May" or month == "Jun":
    percent = 0.15
    return percent
  if month == "Jul" or month == "Aug" or month == "Sep":
    percent = 0.20
    return percent
  if month == "Oct" or month == "Nov" or month == "Dec":
    percent = 0.25
    return percent
  else:
    percent = 0
    return percent

percent = 0
nextsales = 0

r = input("Do you want to run the program? ")
while r == "yes":
  lname = input("Enter last name: ")
  month = input("Enter month: ")
  sales = float(input("Enter sales: $"))
  nextsales = sales * (CompForecast(month) + 1)
  percent = CompForecast(month)
  print("Forecast percent: ", percent)
  print("Next month's sales: $", nextsales)
  r = input("Do you want to run the program? ")