# Zip and UnZip :

# my_list1  = ["Mobile","Laptop","Phone"]
# my_list2 =  [20000,40000,2000] 

# zip

# new_data = zip(my_list1,my_list2)
# print(new_data)
# print(tuple(new_data))
# new_list = list(tuple(new_data))
# print(new_list)


# print(dict(new_data))


# set ,list ,dict, tuple
# my_data =  (('Mobile', 20000,3), ('Laptop', 40000,10), ('Phone', 2000,2))


# print(tuple(zip(*my_data)))


# import datetime 


# data = datetime.datetime.now()
# print(data)



from datetime  import datetime,date
# from datetime import timedelta



date1 = datetime.now()

# date2 = date(2022,12,31)
# print(date1.date())
# print(date1.date().strftime("%d-%m-%y"))
# print(date1.date().strftime("%d-%m-%Y"))
# print(date1.date().strftime("%d-%Y"))

print(date1.date().strftime("%A %d %m %Y"))


# print(date1.strftime("%d-%m-%y"))
# print(date1.day)
# print(date1.month)
# print(date1.year)

# output =  date1 - date2

# print(output)
# print(timedelta(days=10))

# print(date1 + timedelta(days=30))

# print(date1 - timedelta(weeks=1))


# Date diff




# Current Age : 
# import datetime

# today =  datetime.now().date()
# dob = date(2015,3,1)

# print(today.year - dob.year)


# from datetime  import time,timedelta

# time1= time(12,30,45)
# time2= time(18,40,10)


# print(time1.hour)
# print(time1.minute)
# print(time1.second)


# day hours ,min ,sec

# print(time1 + timedelta(hours=10))

# print(type(timedelta(hours=10)))

# print(time1 + timedelta(hours=10))

# import datetime 

# today = datetime.datetime.now()
# t_delta = datetime.timedelta(hours=1)
# print(today.time())

# output = today - t_delta

# print(output.time())


# %M %H %S


