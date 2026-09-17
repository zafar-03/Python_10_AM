# uuid : 

import uuid

# print(uuid.uuid4())

# print(type(uuid.uuid4()))

# my_id = str(uuid.uuid4())
# print(my_id,type(my_id))

students = [
    {
        "roll_no": str(uuid.uuid4()),
        "fname" : "Raj",
        "lname" : "shah"
    },
    {
        "roll_no": str(uuid.uuid4()),
        "fname" : "Raj",
        "lname" : "shah"
    }
]

print(students)