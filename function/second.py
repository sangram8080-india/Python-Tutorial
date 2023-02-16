#wap to print sum of two num input through the Keyboard

#def add_two_num(a,b):
 #   return a+b
#total = add_two_num(4,10)
#print(f"sum of The Num:{total}")    
def add_two(num1,num2):
    return num1+num2

a= int(input("Enter The value of A:"))
b= int(input("Enter The value of B:"))

total = add_two(a,b)
print(f"Sum of Num:{a}+{b}={total}")