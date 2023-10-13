f = open("data.txt", "r")
c = 0
totaltuition = 0.0

lastname = str(f.readline().rstrip('\n'))

while lastname != "":
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())
  
  if dcode == "I":
    costpercredit = 250.0
  else:
    costpercredit = 500.0

  tuition = costpercredit * credits
  c = c + 1
  totaltuition = totaltuition + tuition

  print("Student: ", lastname)
  print("Credits taken: ", credits)
  print("Tuition owed: $", tuition)
  print("")

  lastname = str(f.readline().rstrip('\n'))
f.close()
print("Number of students: ", c)
print("Total tuition owed: ", totaltuition)
  