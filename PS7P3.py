f = open("data.txt", "r")
totbonus = 0
lastname = f.readline()
while lastname != "":
  salary = f.readline()
  print()
  print("Employee last name: ", lastname)
  print("Employee salary: $", float(salary))
  if float(salary) >= 100000:
    bonus = float(salary) * 0.20
    print("Employee bonus: $", float(bonus))
  elif float(salary) == 50000:
    bonus = float(salary) * 0.15
    print("Employee bonus: $", float(bonus))
  else:
    bonus = float(salary) * 0.10
    print("Employee bonus: $", float(bonus))
  totbonus = totbonus + bonus  
  lastname = f.readline()
print()
print("Total bonuses: $", totbonus)
