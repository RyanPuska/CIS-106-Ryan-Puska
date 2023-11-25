def dl1(mylist):
  n = int(input("Number of items for your list: "))
  for n in range(0,n,1):
    s = int(input("Enter an integer: "))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)


mylist = []
mylist = dl1(mylist)
displaylist(mylist)
print(mylist)

mylist.insert(0,99)
print(mylist)

mylist[0] = 100
print(mylist)

mylist2 = [500, 600, 700, 800, 900]
print(mylist2)
mylist.extend(mylist2)
print(mylist)

mylist.remove(800)
print(mylist)

mylist.remove(mylist[3])
print(mylist)

grades = ["A", "B", "C", "A", "A", "C"]
print(grades)
print("Count of A's in the list: ", grades.count("A"))

print("B's position in the list: ", grades.index("B"))

print("Count of F's in the list: ", grades.count("F"))
if "F" not in mylist:
  print("F is not found.")

for item in mylist2:
  if item in mylist:
      mylist.remove(item)
print(mylist)
#print(mylist.remove(mylist2))

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players.sort()
print(players)

players2 = players.copy()
print(players2)

players2.reverse()
players.extend(players2)
print(players)