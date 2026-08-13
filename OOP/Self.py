# self :  represent current Object


class Person:
    def __init__(self,fname):
        self.fname = fname 

    def display(self):
        print(self.fname)


p1 = Person("Rajesh")
p2 = Person("Sahil")


p1.display()
p2.display()