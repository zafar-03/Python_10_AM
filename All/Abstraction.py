from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    pass
    # def sound(self):
    #     print("Barks")

d1 = Dog()
d1.sound()