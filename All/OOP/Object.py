# Object : instance of Class

# Create a Single Object : 
# class Student:
#     studentname = "Rahul"

#     def displaydata(self):
#         print(self.studentname)

# # Object 
# s1 = Student()
# s2 = Student()

# s1.displaydata()
# s2.displaydata()


# Create Object Using Class with Constructor :
# We can Create Multiple Objects


class Person:
    institutename = "Red & White.."

    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        print('First Name : {0} \nLastname : {1} \nInstitute name : {2}'.format(self.firstname,self.lastname,self.institutename))

person1 = Person("Raj","Shah")
person2 = Person("Sahil","Sharma")

person1.display()

person2.display()