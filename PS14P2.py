class Car:
  def __init__(self, make, model, price, discprice):
    self.make = make
    self.model = model
    self.price = price
    self.discprice = discprice

  def fullname(self):
    return "{} {}".format(self.make, self.model)

class Sport(Car):
    def __init__(self, make, model, price, discprice, method, uprice):
      super().__init__(make, model, price, discprice)
      self.method = method
      self.uprice = uprice

    def apply_method(self, uprice):
      if self.method == "SportWheels":
        uprice = self.discprice + 1000
        return uprice
      elif self.method == "SportEngine":
        uprice = self.discprice + 3000
        return uprice
      elif self.method == "SportInterior":
        uprice = self.discprice + 2000
        return uprice

car_1 = Car("Pagani", "Huayra", 1400000, .90*1400000)
spo_1 = Sport("Pagani", "Huayra", 1400000, .90*1400000, "SportWheels", .90)


print(car_1.make)
print(car_1.model)
print(car_1.price)
print(car_1.discprice)
print(spo_1.apply_method(spo_1.uprice))