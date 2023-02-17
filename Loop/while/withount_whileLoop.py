#wap to print without whilel loop using python 
#using string indexing 

num = input("Please Enter Any Digites Num:")

#sum of digites

total=0


lenght = len(num)

print(f"Lenght of Digites:{lenght}")


lenght = int(lenght)
while lenght<=1:
    total = int(num[i])+total

    lenght = lenght-1
print(f"Sum of The Num:{total}")

    
