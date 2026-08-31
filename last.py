# num_1 =12
# num_2 = 0


# output = num_1/num_2   # infinite

# print(output)
# num_1 =12
# num_2 = 0

# try:            # Try Block 
#     output = num_1/num_2
# except:
#     print("Error")
# else:
#     print(output)





# try:            # Try Block 
    # output = num_1/num_2
    # print(data)
    # print(int("Raj"))
    # print("Raj" + 12)
    # output = True - 3
    # output = "12" * 2
    # output = [12,13] + 1
    # output = [14,12,13] - [14,15]
    # output = (1,2) - (3,4)
    # output = "Raj" * True

# except ZeroDivisionError:
#     print("division by zero")
# except TypeError:
#     print("Type Error")
# except ValueError:
#     print("Value Error")
# except NameError:
#     print("Variable Not Define")
# else:
#     print(output,type(output))


# print(0.1 + 0.2)
# print(0.5 + 0.25)


# Bugs : memory : 32/64  : binary : 0/1 :   1971  : 2038  18 jul ,2038



# num_1 =12
# num_2 = 3

# try:
#     output = num_1/num_2
#     # print(int("Raj"))
# except ZeroDivisionError:
#     print("Zero Division Error")
# except :
#     print("Error")
# else:
#     print(output)
# finally:
#     print("Final Block")


# raise keyword : 

# saving : 100000 ,50000, 2lac/

# custom Exeption 
class MyException(Exception):
    pass

balance = 10000

# def withdraw(balance,amount):
#     if(balance<amount):
#         raise MyException()
#     balance-=amount
#     print("Withdraw Successful : current balance :",balance)


# try:
#     withdraw(balance,12000)
# except MyException:
#     print("Not Possible")

# custom Exception 
# assert

#  global 
#  local  :::::


# Exception : 
# 1. Built in
# 2. Custom (user defined)

# =====================================================

# raise  keyword
# Custom exception
# assert keyword

# class AgeLimitError(Exception):
#     pass



# age =12

# if(age >=18):
#     print ("Voting")
# else:
#     raise AgeLimitError("Age must be Greater than or Equal to 18")

# print(12/0)

# try:
#     if(age >=18):
#         print ("Voting")
#     else:
#         raise AgeLimitError("Age must be Greater than or Equal to 18")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except AgeLimitError as error:
#     print(error)
# else:
#     print("try Block Successfully Executed")
# finally:
#     print("Completed")



# age = 12

# try:
#     assert age>=18
# except AssertionError:
#     print("Point Breakdown")
# else:
#     print(age)
# finally:
#     print("Completed")


# assert age>=18