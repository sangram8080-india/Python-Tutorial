#wap to print sum of Num input though the Keyboard 
#1+2+......+10
print("1 to M sum of The Num:")
num = int(input("Enter The value 1 to M:"))
total =0
for i in range(num+1):
    total = total+i
print(f"Sum of The Num:{total}")