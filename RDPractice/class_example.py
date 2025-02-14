class Person:
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname

    def printname(self):
        print(self.fname)
        print(self.lname)


x  = Person("Raghavendra","D")
x.printname()
