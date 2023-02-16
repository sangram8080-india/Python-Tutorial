#wap to print 3 Ditiges of Greatest Num

def Greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c

num1 =int(input("Enter The Num1:"))
num2 = int(input("Enter The Num2:"))
num3 = int(input("Enter The Num3:"))

temp = Greatest(num1,num2,num3)

print(f"Greatest Num of {num1},{num2} and {num3} = {temp} ")