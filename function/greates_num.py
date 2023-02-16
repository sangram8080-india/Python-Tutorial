#define a fun which takes two num as input and return Greatest of Two num .

def great(num1,num2):
    if num1>num2:
        return num1
    return num2

a= int(input("Enter the Frist Num:"))
b = int(input("Enter The Scond Num:"))

temp = great(a,b)

print(f"Greatest Num of {a},{b} = {temp}")