#watch Coco
#ask user's name start with ('a' or 'A') and age is above 10 then 
#print you watch coco movies
#else print sorry con't watch  Coco movies 

print("COCO Movies".center(17,"*"))
print("\n")

user_name = input("Enter your Name")
user_age  = int(input("Enter Your Age?"))

user_name = user_name.lower()
#user_name[0] == 'a'
#user_name = user_name[0]
#print(user_name)

if user_name[0] == 'a' and user_age >= 10:
    print("You Watch Coco Movies")
else:
    print("Sorry!!! Con't Watch Coco Movies")