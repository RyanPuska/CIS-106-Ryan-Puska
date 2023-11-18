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

def searchName(lname,score,sname):
  foundsub = -1
  for i in range (0,10):
    if lname[i] == sname:
      foundsub = i
  if foundsub == -1:
    print(sname + " not found.")
  else:
    print(lname[foundsub], " has a batting average of ", score[foundsub], ".")

lname = []
score = []
txtArray(lname, score)

response=input("Do you want to search for a last name? (y/n) ")
while response == "y":
  sname = input("Enter a last name: ")
  searchName(lname,score,sname)
  response=input("Do you want to search for a last name? (y/n) ")
