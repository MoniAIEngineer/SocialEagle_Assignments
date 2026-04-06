'''
******************************************
Assignment No:1
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj for Elif
******************************************
'''
Score=int(input("Emter exam Mark:"))
if 90 <= Score <= 100 :
    print("A+")
elif 80 <= Score <= 89 :
    print("B")
elif 50 <= Score <= 79 :
    print("C")
elif Score < 50 :
    print("Fail")
else:
    print("Invalid Number")
