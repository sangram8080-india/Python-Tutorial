#wap to print N to M num of The Sum 

print("***N To M Num of The Sum***")

n = int(input("Enter The value of N:"))
m = int(input("Enter the value of M:"))
num =n
total = 0

for n in range(m+1):
    total=total+n
print(f"Sum of {num} To {m} : {total}")