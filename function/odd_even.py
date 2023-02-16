#wap to print Odd Even using fun 

def number(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter The  Num:"))
temp = number(n)
print(temp)