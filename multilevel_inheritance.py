# program for multilevel inheritance


class Student:     # base class

    # accepting general information of student
    def detail(self):

        print("The General information of srtudent")
        self._rollno = int(input("Enter Roll No. :"))
        self._class = input("Enter Class :")
        self._div = input("Enter Division :")
        self._sem = int(input("Enter Semester :"))


# derived class from base class
class Marks(Student):

    # accepting marks of student
    def accept_mark(self):

        self._oop = int(input("Enter OOP mark: "))
        self._wp = int(input("Enter WP mark: "))
        self._dm = int(input("Enter DM mark: "))
        self._dbms = int(input("Enter DBMS mark: "))
        self._pp = int(input("Enter PP mark: "))
        self._IT = int(input("Enter IT TOOL mark: "))


# derived class from already derived class Marks
class Result(Marks):

    # displaying total and percentage of student
    def percentage(self):

        self.total = self._oop + self._wp + self._dm + self._dbms + self._pp
        + self._IT
        self.percentage = (self.total / 600) * 100
        self.average = self.total / 6
        print("percentage is ", self.percentage)
        print("average is ", self.average)


# creating a object
mark = Result()
mark.detail()       # calling function through object
mark.accept_mark()
mark.percentage()
