# python program showing method overloading


class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')


# create instance
obj = Human()

# call the method
obj.sayHello()

# call the method with a parameter
obj.sayHello('everyone')
