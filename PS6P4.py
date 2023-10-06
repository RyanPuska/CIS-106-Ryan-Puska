sumgpay = 0
employnum = 0
print("Would you like to participate in this program? ")
response = input()
while response == "yes":
    print("Enter last name: ")
    lname = input()
    print("Enter hours worked: ")
    hours = float(input())
    print("Enter rate of pay:")
    ratepay = float(input())
    if hours >= 40:
        gpay = 40 * ratepay + (hours - 40) * 1.5 * ratepay
    else:
        gpay = ratepay * hours
    print("Gross pay: $", gpay)
    sumgpay = sumgpay + gpay
    employnum = employnum + 1
    print("Would you like to enter again?")
    response = input()
avgpay = sumgpay / employnum
print("Sum of all gross pay: $" , sumgpay)
print("Number of employees entered: ",employnum)
print("Average gross pay: $", avgpay)
