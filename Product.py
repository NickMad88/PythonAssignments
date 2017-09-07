
class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = "sold"
    def addTax(self, tax):
        self.cost = self.price + (self.price * tax)
    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.cost = self.price - (self.price * .20)

    def displayInfo(self):
        print 'Price: ' + str(self.price)
        print 'Item Name: ' + self.item_name
        print 'Weight: ' + str(self.weight) + ' lbs'
        print 'Brand: ' + self.brand 
        print 'Cost: ' + str(self.cost)
        print 'Status: ' + self.status

    


ketchup = Product(4.99, 'Ketchup', 1, 'Heinz', 4.99, 'new')
ketchup.displayInfo()
ketchup.addTax(.10)
ketchup.displayInfo()
ketchup.sell()
ketchup.displayInfo()
