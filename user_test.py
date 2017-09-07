# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
# user1 = User("Anna Propas", "anna@anna.com")
# print user1.name
# print user1.logged
# print user1.email



class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
    def reverse(self):
        print "Reversing"
        self.miles -= 5

bike1 = Bike(200,500,0)
bike2 = Bike(100,501,2)
print bike1.miles
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()