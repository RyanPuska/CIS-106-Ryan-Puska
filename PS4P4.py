appname = input("Name: ")
appcost = float(input("Cost of appliance: $"))

if appcost <= 1000:
  warcost = appcost * 0.05
else:
  warcost = appcost * 0.1
  
total = warcost + appcost

print("Appliance name: ", appname)
print("Appliance cost: $", appcost)
print("Warranty cost: $", warcost)
print("Total: $", total)