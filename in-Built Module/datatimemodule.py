import datetime   # add/

# my_var = datetime.datetime()


# 1.now : 
# current_data = datetime.datetime.now()  # date and Time 
# print(current_data)

# 2. today
today =  datetime.datetime.today()
# print(today)

# print(datetime.datetime.now().date())
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().year)

# print(datetime.datetime.now().time())
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)


# input : MM - DD  - YYYY
# 12-1-1 

# your_date = datetime.datetime(2000,2,1)


# print(your_date)

# today = datetime.datetime.now()
# print(today)

# today = datetime.date.today()
# 2026-09-08

print(today.strptime("02/26","%m/%y"))


#   dd : mm : yy    26
#   dd : mm : yyyy  2026


# 1/12
# class xyz:

#     def all(self):
#         pass


# xyz.all()

# x = xyz()


# timezone = datetime.timezone(datetime.timedelta())


# print(timezone)

# 