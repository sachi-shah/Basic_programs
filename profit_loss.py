'''Program implementing 5 concepts of OOP
1.Class
2.data abstraction
3.Inheritance
4.abstract class
5.objects'''

from abc import ABC


class Business1(ABC):
    def Profit():
        pass


class _Business:
    _cp = int(input("Enter cost price of product:"))
    _price = int(input("Enter the products price:"))
    _profit2 = _price - _cp
    _profit = _cp + _profit2


class Profit(Business1, _Business):
    def Profit(self):

        _cp = self._cp
        _price = self._price

        if(self._price < self._cp):
            print("No Profit")
        else:
            (self._price <= self._cp)
            self.profit1 = self._price - self._cp
            print("Profit is of Rs", self.profit1)


class Loss(_Business):
    def Loss(self):

        if self._cp <= self._price:
            print("No loss")
        else:
            self.loss = -(self._price - self._cp)
            print("Loss is of Rs", self.loss)


class betterdeal (_Business):
    def deal(self):
        _profit = self._profit

        self.cal = self._cp * 45 / 100
        self.deal = self._cp + self.cal
        if self._profit >= self.deal:
            print("Good deal")
        else:
            print("The best deal could be  of Rs", self.deal)
            print("Here profit is of Rs", self.cal)


c = _Business()

a = Profit()
a.Profit()
c1 = Loss()
c1.Loss()
d = betterdeal()
d.deal()
