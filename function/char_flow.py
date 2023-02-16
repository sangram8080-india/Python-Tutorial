#wap to print char  devided for string 

def last_char(name):
    return name[-1]

name = input("Enter The Any Name By User:")
name_l = last_char(name)
print(f"Last char in string input the user:{name_l}")