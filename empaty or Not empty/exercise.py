#Empaty and Not Empaty in Using python 

name = input("Please Type Any Name")

name =name.lstrip()
if name:
    print(f"Your Type Name is: {name}")
else:
    print("You Didn't Type Any Type (Try Again?)")