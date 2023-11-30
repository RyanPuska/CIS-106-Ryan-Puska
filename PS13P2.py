class Student:
  def __init__(self, first, last, district, credit):
    self.first = first
    self.last = last
    self.district = district
    self.credit = credit

  def fullname(self):
    return "{} {}".format(self.first, self.last)

  def tuition(self, rate):
    if self.district == "I":
      tuition = self.credit * 250
    else:
        tuition = self.credit * 500
    return tuition * float(rate)

stu_1 = Student("Corey", "Schafer", "I", 15)
stu_2 = Student("Test", "User", "O", 17)

print(stu_1.credit)
print(stu_1.first)
print(stu_1.last)
print(stu_1.district)
print(stu_1.tuition(1))
