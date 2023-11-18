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

  print(lname[hisub], " has the highest score of ", score[hisub], "%.")
  print(lname[lowsub], " has the lowest score of ", score[lowsub], "%.")
    

def displayArray(lname, score):
  for i in range (0,10):
    print(lname[i] + " has a score of " + str(score[i]) + "%.")

lname = []
score = []
txtArray(lname, score)
displayArray(lname, score)
hilow(lname, score)