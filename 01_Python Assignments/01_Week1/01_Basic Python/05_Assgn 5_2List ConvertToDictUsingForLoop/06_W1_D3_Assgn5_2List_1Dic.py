'''
******************************************
Assignment No:6 - Read 2 List data and Convert 
as Dictionary using For Loop
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj for Elif
******************************************
'''
keys = ["name", "age", "course"]
values = ["Bob", 22, "Mathematics"]

student_dict = {}

for i in range(len(keys)):
    student_dict[keys[i]] = values[i]

print(student_dict)