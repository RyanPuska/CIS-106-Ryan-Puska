def average(s1,s2,s3,handicap):
  total = s1+s2+s3
  saverage = total/3
  haverage = (total+handicap)/3
  return saverage, haverage

lname = input("Enter last name: ")
s1 = float(input("Enter score 1: "))
s2 = float(input("Enter score 2: "))
s3 = float(input("Enter score 3: "))
handicap = float(input("Enter handicap: "))
saverage, haverage = average(s1,s2,s3,handicap)

print("Your last name: ", lname)
print("Average score: ", saverage)
print("Handicap average: ", haverage)
