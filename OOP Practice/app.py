from abc import ABC,abstractmethod
from datetime import datetime



# Base Class
class Person:
    def __init__(self,uname,age,address):
        self.name = uname
        self.age = age
        self.address = address

    def display(self):
        print("{0}\n{1}\n{2}".format(self.name,self.age,self.address))
        

# Inherit 
class Customer(Person):
    def __init__(self, uname, age, address,customer_id):
        super().__init__(uname, age, address)
        self.customer_id = customer_id

    # method

# Abstract Class
class Account(ABC):
    __total_accounts = 0   
    def __init__(self,account_number, account_holder,balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self.transiction = []
        Account.__total_accounts +=1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        self.__balance = amount

    def deposit(self,amount):
        self.balance += amount
        self.transiction.append("{0} | deposit | {1}".format(datetime.now(),amount))

    @abstractmethod
    def withdraw(self):
        pass

    @staticmethod
    def get_total_accounts(self):
        return Account.__total_accounts

# 20/08

class SavingsAccount(Account): 

    def __init__(self,account_number, account_holder,balance,interest_rate):
        super().__init__(account_number, account_holder,balance)
        self.interest_rate = interest_rate

    def withdraw(self,amount):
        if self.balance < amount : 
            pass 
        else :
            self.balance-=amount
            self.transiction.append("{0} | Withdraw | {1}".format(datetime.now(),amount))
            
        
    def add_interest(self):
        interestamount = self.balance * self.interest_rate / 100
        self.balance+=interestamount
        self.transiction.append("{0} | interest | {1}".format(datetime.now(),interestamount))

    def account_type(self):
        return "saving"




class CurrentAccount(Account):

    def __init__(self,account_number, account_holder,balance,overdraft_limit):
        super().__init__(account_number, account_holder,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if self.balance > amount : 
            self.balance-=amount
            self.transiction.append("{0} | Withdraw | {1}".format(datetime.now(),amount))
        else:
            if(self.balance() + self.overdraft_limit > amount):
                self.balance-=amount
                self.transiction.append("{0} | Withdraw | {1}".format(datetime.now(),amount))
                self.overdraft_limit = self.overdraft_limit + self.balance()
            else :
                print()

    def account_type(self):
        return "current"



class Bank:
    customers = []
    accounts = []
    # def __init__(self,bname):
    #     self.bankname = bname
        

    def add_customer(self,customer):
        self.customers.append(customer)

    def add_account(self,account):
        self.accounts.append(account)


    def transfer(self,accountself,account_num,amount):
       
        pass

    def __len__(self):
        return len(self.customers)

    def count_no_accounts(self):
         print(Account.get_total_accounts(self))

    # def __str__(self):
    #     pass

    def add_account_type(self):
        pass


bank1 = Bank()
# c1 = Customer("Raj",12,"Rajkot",1234)
# c2 = Customer("Rahul",22,"Rajkot",1235)



# print(bank1.customers)
# bank1.add_customer(c1)
# bank1.add_customer(c2)
# print(bank1.__len__())
# print(bank1.customers)


a1 = SavingsAccount(1234567890,"Rajesh Shah",10000,7)
# a2 = SavingsAccount(12354334567890,"Rajesh Shah",10300,7)

# a1.withdraw(2000)
# a1.deposit(5000)
# print(a1.transiction)
# print(a1.balance)

bank1.add_account(a1)
# bank1.add_account(a2)
# print(Account.get_total_accounts(bank1))
bank1.count_no_accounts()

"""
while(1):
    print("===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Print Statement")
    print("7. View Total Accounts (classmethod)")
    print("8. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1 :
        pass
    elif choice == 2 :
        pass
    elif choice == 3 :
        pass
    elif choice == 4 :
        pass
    elif choice == 5 :
        pass
    elif choice == 6 :
        pass
    elif choice == 7 :
        pass
    elif choice == 8 :
        pass
    else:
        pass
"""
