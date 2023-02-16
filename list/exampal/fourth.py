#Defite a function wich will take list containg  num as define value 1 to 10
number = list(range(1,11))

def squre_num(l):
    squre  = []
    for i in l:
        squre.append(i**2)
    return squre

print(squre_num(number))
