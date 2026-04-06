'''*
*****************************************
Assignment No:2
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj for Ternary
******************************************
'''
age = int(input("Enter the age"))
if age >= 18 :
    pro = input("Enter your Subcription plan:")
    if pro:
        print ("Full Access Provided")
    else :
        print("Only Read Acces Given")
else :
    print("For Junior No Access will be Given")

status = "adult" if age >= 18 else("Minor")
print(status)