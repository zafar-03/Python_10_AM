class Person:
    def __init__(self):
        print("Created")

    def __del__(self):
        print("Deleted")

p1 = Person()
# num = 1
# while(num == 1 ):
#     num = int(input("Enter The Value of N :"))
#     print("Program Continue")
#     if(num==2):
#         del p1

# print("hello")