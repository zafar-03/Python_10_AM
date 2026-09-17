# Higher Order Functions (sorted(), map(), reduce() & filter())

# lambda Expression/Function : 

# lambda value : codition(value)


# sorted : 

# my_list = [11,3,56,34,6,23]
# print(my_list)
# my_list.sort()
# print(my_list)

# print(sorted(my_list))
# print(sorted(my_list,key=lambda x : x))
# print(sorted(my_list,key=lambda x : x,reverse=True))

# print(sorted(my_list,key=lambda x : x<20))


# print(my_list)


# print(list(filter(lambda x : x>30,my_list)))

# print(list(filter(lambda x : False,my_list)))


# print(list(map(lambda x : x*2,my_list)))
# print(list(map(lambda x : x<30,my_list,strict=True)))


# print((12,15)[1] < (14,12)[0])


# import time

# print("hello")
# time.sleep(1)
# print("34")

# print(dir(time))


my_list = [1,2,3,4,5]


# from functools import reduce

# print(my_list)


# print(reduce(lambda a,b : a + b,my_list))

# print(reduce(lambda a,b : a - b,my_list))
# print(reduce(lambda a,b : a / b,my_list))



# print(min(my_list))
# print(max(my_list))