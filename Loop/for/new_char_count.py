#wap to print sum of Num 
#5 = 1+2+3+4=10
num = int(input("Enter A Num:"))
total = 0
for i in range(num):
    total +=int(i)
print(total,end=" ")