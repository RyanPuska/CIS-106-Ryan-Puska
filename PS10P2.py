def computePoints(s1, s2, s3):
  total = s1+s2+s3
  return total

lname = input("Enter last name: ")
s1 = int(input("Enter score 1: "))
s2 = int(input("Enter score 2: "))
s3 = int(input("Enter score 3: "))
total = computePoints(s1, s2, s3)
average = total/3

print("Last name: ", lname)
print("Total: ", total)
print("Average of scores:", average)