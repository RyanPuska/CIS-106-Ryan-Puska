def CompBatAvg(hits, bats):
  batavg = hits/bats
  return batavg

count = 0

r = input("Do you want to compute batting average? ")
while r == "yes":
  lname = (input("Enter last name: "))
  hits = float(input("Enter hits: "))
  bats = float(input("Enter bats: "))
  batavg = CompBatAvg(hits, bats)
  print("Batting Average: ", batavg)
  r = input("Do you want to compute batting average? ")
  count = count + 1
  
print("Number of players entered: ", count)