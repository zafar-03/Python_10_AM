# # Types of Inheritance : 

#1. Single Inheritance :  One child class inherits from one parent class.
"""
Class A (Parent)
    |
    |
    ↓ 
Class B    (child)  (inherit Class A)

"""
# class Person:
#     def greeting(self):
#         print("Hello Everyone")


# class Student(Person):
#     pass


# s1 = Student()
# s1.greeting()


# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

# class Student(Person):
#     def __init__(self,fname,lname,std):
#         # super().__init__(fname,lname)
#         Person.__init__(self,fname,lname)
#         self.standard = std
        
# s1 = Student("Raj","Shah",10)


# print(s1.standard)
# print(s1.firstname)


#2. Multiple Inheritance :  A child class inherits from multiple parent classes.
"""
Example 1 : 
Class A (Parent)
                |
                |-------------->Class C (Child)
                |
Class B (Parent)



Example 2 :
Class A (Parent)----|
                    |
                    |
                    |
Class B (Parent)----|-------------->Class C (Child)
                    |
                    |
                    |
Class D (Perent)----|
"""

#3. Multilevel Inheritance : A class inherits from another child class (forms a chain).

"""
Class A :     (Parent)
    |
    |
    ↓ 
Class B :    (Inherit Class A)
    |
    |
    ↓ 
Class C :      (Inherit Class B)

"""

#4. Hierarchical Inheritance :  Multiple child classes inherit from a single parent class.

"""
Example 1 : 
Class A (Child)
                |
                |-------------->Class C (Parent)
                |
Class B (Child)



Example 2 :
Class A (Child)----|
                    |
                    |
                    |
Class B (Child)----|-------------->Class C (Parent)
                    |
                    |
                    |
Class D (Child)----|
"""

#5. Hybrid Inheritance : A combination of different types of inheritance.
"""
Class A :     (Parent)-------------------
    |                                   |
    |                                   |
    ↓                                   |
Class B :    (Inherit Class A)          |
    |                                   |
    |                                   |
    ↓                                   |
Class C :      (Inherit Class B)        |
    |                                   |
    |                                   |
    ↓                                   |
Class D :<------------------------------|
"""