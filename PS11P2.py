def displayArray(lname, score):
  for i in range (0,10):
    print(lname[i])
    print(score[i])

def reverseArray(lname, score):
  for i in range (9,-1,-1):
    print(lname[i])
    print(score[i])

lname = ["Alex", "Bach", "Charles", "Dean", "Edwards", "Fox", "Glenn", "Henry", "Ivey", "Johnson"]
score = [88, 87, 93, 69, 98, 76, 83, 90, 90, 72]

displayArray(lname, score)
reverseArray(lname, score)