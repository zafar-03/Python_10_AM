class Account:
    # bankname = "SBI"   # Public
    # _accountholdername = "Raj"  # private
    # __balance = 100000 # protected

    def __init__(self,d1,d2,d3):
        self.bankname = d1    # public
        self._accountholdername = d2 # private
        self.__balance = d3 # protected

        def checkbalance(self):
            print(self.__checkbalance)


a1 = Account("SBI","Rahul",12340)

a1.checkbalance()