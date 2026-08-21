accounts = [
    {"accountno":1234,"balance" : 1000},
    {"accountno":5678 , "balance" : 3000}
]


accountself = 5678
account_no = 1234
amount = 4000

for i in accounts:
    if accountself == i.get("accountno"):
        if(i.get("balance")>= amount):
            for j in accounts:
                if account_no == j.get("accountno"):
                    j.__setitem__("balance",j.get("balance")+amount)
                    break
            i.__setitem__("balance",i.get("balance")-amount)        
            break
        else:
            print("Invalid")

print(accounts)