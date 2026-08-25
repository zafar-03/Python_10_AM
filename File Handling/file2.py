# File Handling : 
# read Op(Mode) : (r)
#1. Text     2. Binary

# step : 1  file open. 
# fpt = open("C:\\Users\\rwr2m\\OneDrive\\Desktop\\Python_10_AM\\File Handling\\file2.txt")

# fpt = open("C:\\Users\\rwr2m\\OneDrive\\Desktop\\Python_10_AM\\File Handling\\file2.txt","r")

# 1.
# print(fpt.readline())

# 2. 
# print(fpt.readlines())  # List 

# 3.
# my_data = fpt.readlines()
# for data in my_data:
#     print(data,end="")

# print(data for data in fpt.readlines())

# 4.
# print(fpt.read())

# 5.
# with open("C:\\Users\\rwr2m\\OneDrive\\Desktop\\Python_10_AM\\File Handling\\file2.txt","r") as f:
#     print(f.read())

# fp = open("File Handling/file2.txt","r")

# Write (w)(Mode) :
# write new Data if File already Exist otherwise first create a New File then and New Data.
 #  remove  then new Data add

# fp = open("file2.txt","w")


# Append : (a) (Mode)
# fp = open("file2.txt","a")
# fp.write("New Data Added\n")

# fp.close()

# Create : (x)(Mode) : 
# fp = open("newfile3.txt","x")

# fp = open("newfile5.txt","a")


# fp.close()

# =====================
# File  : txt 

# binary : b
# File : png,mp4,mp3,pdf,py,.......

# fp =  open("home.png","rb")

# print(fp.read())

# fp.close()


# with open("home.png","rb") as filedata:
#     image_data = filedata.read()

# print(image_data)


# with open("newimage.png","wb") as f:
#     f.write(image_data)


#  .bin   .dat


# ============================
class Student :
    def __init__(self,id,sname,age):
        self.roll_no = id
        self.student_name = sname
        self.age = age


s1 = Student(1001,"Raj",13)
s2 = Student(1002,"Rajesh",12)
s3 = Student(1003,"Rajveer",10)


fp= open("studentsdata.txt","w")

fp.write(f"ID : {s1.roll_no}, StudentName :{s1.student_name}, Age :{s1.age}\n")
fp.write(f"ID : {s2.roll_no}, StudentName :{s2.student_name}, Age :{s2.age}\n")
fp.write(f"ID : {s3.roll_no}, StudentName :{s3.student_name}, Age :{s3.age}\n")




fp.close()

with open("studentsdata.txt") as d:
    print(d.read())