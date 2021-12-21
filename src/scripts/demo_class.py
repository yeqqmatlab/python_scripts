class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + '' +self.make + '' + self.model
        return long_name.title()

    def update_odometer(self,x):
        if x >= self.odometer_reading:
            self.odometer_reading = x
        else:
            print(" you can not roll back an odometer!")




car = Car('china','A',2021)
print(car.year)

class BigCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def update_num(self):
        print(" test -> big_car ")

big_car=BigCar("A","B",222)
print(big_car.update_num())