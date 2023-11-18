def displayArray(lname):
  for i in range (0,10):
    print(lname[i])

def reverseArray(lname):
  lname.reverse()
  for i in range (0,10):
    print(lname[i])

lname = ["Alex", "Bach", "Charles", "Dean", "Edwards", "Fox", "Glenn", "Henry", "Ivey", "Johnson"]

displayArray(lname)
reverseArray(lname)