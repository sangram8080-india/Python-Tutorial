#wap to print default parameters

#def user_info(frist_name,last_name,age):
#but

def user_info(frist_name,last_name='unknow',age='none'):
    print(f"You Frist Name:{frist_name}")
    print(f"You Last Name:{last_name}")
    print(f"You Age:{age}")


N= input("Enter The Frist Name of User:")
L= input("Enter The Last Name of User:")
A = input("Enter The User Age:")
user_info(N,L,A)

