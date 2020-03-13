# python example to show working of
# multiple inheritance


class Base1(object):
    def __init__(self):
        self.str1 = 'Hello'
        print(self.str1)
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = 'Hi'
        print(self.str2)
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


derivedobject = Derived()
derivedobject.printStrs()
