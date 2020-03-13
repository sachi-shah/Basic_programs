# program showing the use of
# constructor and destructor


class rectangle:

    def __init__(self, length, breadth):
        print("I'm initializing the instances of rectangle class")
        self.length = length
        self.breadth = breadth

    def area(self):
        self.area = self.length * self.breadth
        print(self.area)

    def __del__(self):
        print("the instance destroyed")


c = rectangle(20, 10)
c.area()
c1 = rectangle(20, 30)
c1.area()
c.__del__()
c1.__del__()
