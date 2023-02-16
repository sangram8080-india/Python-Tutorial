#Defite a function wich will take list containg  num as input
number = [1,2,5,6,7,8]

def squre_num(l):
    squre  = []
    for i in l:
        squre.append(i**2)
    return squre

print(squre_num(number))
