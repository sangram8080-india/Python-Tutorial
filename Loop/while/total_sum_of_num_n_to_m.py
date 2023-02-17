#wap to print N to M sum of The num 

total =0

n = int(input("Enter The Value of N"))
m = int(input("Enter The Value of M"))

i = n

while i<=m:
    
    total = total+i

    i= i+1
print(f"Sum of The N to M Num:{total}")