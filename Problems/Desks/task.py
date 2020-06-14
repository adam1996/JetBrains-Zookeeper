import math

classroom_1_students = int(input())
classroom_2_students = int(input())
classroom_3_students = int(input())

total_desks = int(math.ceil(classroom_1_students / 2)) + int(math.ceil(classroom_2_students / 2)) + int(math.ceil(classroom_3_students / 2))

print(total_desks)
print(round(4.5))
