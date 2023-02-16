#Show ticket pricing
#1 to 3 (free)
#4 to 10 (150)
#11 to 60(250)
#above 60(200)

print("SRS Cinema Ticket".center(23,"*"))


age = int(input("Please Enter Your Age?"))
if age == 0 or age <0:
    print("Try Again?")
elif 0<age<=3:
    print("Your Ticket Price: Free")
elif 3<age<=10:
    print("Your Ticket Price:150")
elif 10<age<=60:
    print("Your Ticket Price:250")
else:
    print("Your Ticket Price:200")