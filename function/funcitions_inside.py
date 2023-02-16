#multi functions using python
#wap to print greater Num  in three Digites

def greater(a,b):
    if a>b:
        return a
    else:
        return b 

    def  greatest(a,b,c):
        if a>b and a>c:
            return a
        
        elif b>a and b>c:
            return b
        else:
            return c
    
    def new_greatest(a,b,c):
        bigger = greater(a,b)
        return greatest(bigger,c)
    
    num1= int(input("Enter The value of Num1:"))
    num2 = int(input("Enter The value of Num2:"))
    num3 = int (input("Enter The value of Num3:"))

    great = new_greatest(num1,num2,num3)

    print(f"Greater Num of {num1},{num2} and {num3}:{great}")