
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)

car1 = Car(12000, 55, 'a', 15)

