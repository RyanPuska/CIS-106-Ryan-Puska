counter = 0
print("Do you want to compute your average score? ")
response = input()
while response == "yes":
    counter = counter + 1
    print("Enter last name: ")
    lname = input()
    print("Enter exam score 1: ")
    score1 = float(input())
    print("Enter exam score 2: ")
    score2 = float(input())
    avg = (score1 + score2) / 2
    print("Student " + lname + " has average of", avg)
    print("Do you want to compute your average score? ")
    response = input()
print("Number of students who entered data: ", counter)
