lname = input("Last name: ")
salary = float(input("Salary: "))
joblvl = int(input("Job level: "))

if joblvl >= 10:
    brate = 0.25
else:
    if joblvl > 4:
        brate = 0.2
    else:
        brate = 0.1
      
bonus = salary * brate

print(lname)
print("$", bonus)
