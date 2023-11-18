def txtArray(lname, score):
  f = open("file.txt", "r")
  for i in range (0,10):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lname.append(ln)
    s = f.readline()
    s = s.rstrip("\n")
    score.append(float(s))
  f.close()

def hilow(lname, score):
  hiscore = 0.0
  hisub = 0
  lowscore = 999.999
  lowsub = 0
  for i in range (0,10):
    if score[i] > hiscore:
      hiscore = score[i]
      hisub = i
    elif score[i] < lowscore:
      lowscore = score[i]
      lowsub = i

  print(lname[hisub], " has the highest batting average of ", score[hisub], ".")
  print(lname[lowsub], " has the lowest batting average of ", score[lowsub], ".")

def searchName(lname,score,sname):
  foundsub = -1
  for i in range (0,10):
    if lname[i] == sname:
      foundsub = i
  if foundsub == -1:
    print(sname + " not found.")
  else:
    print(lname[foundsub], " has a batting average of ", score[foundsub], ".")

def displayArray(lname, score):
  for i in range (0,10):
    print(lname[i] + " has a batting average of " + str(score[i]) + ".")

lname = []
score = []
txtArray(lname, score)
displayArray(lname, score)
hilow(lname, score)

response=input("Do you want to search for a last name? (y/n) ")
while response == "y":
  sname = input("Enter a last name: ")
  searchName(lname,score,sname)
  response=input("Do you want to search for a last name? (y/n) ")
  