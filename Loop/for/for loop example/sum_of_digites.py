#wap to print sum of digites
#12345 
#1+2+3+4+5

num = int(input("Enter The Any Digites Num:"))
total = 0

for i in range(num):
    m=num%10
    total = int(total)+int(m)
    num = num/10
print(f"Sum of Digites:{total}")

