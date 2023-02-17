#ask user or input a num 
#coucting more than one digit 
#exam :- 1256
#calculate : 1+2+5+6

num = input("Please Enter The Any Digit:")
total = 0
lenght = len(num)
print(f"Count of Digite:{lenght}")

num = int(num)
while num>0:
    m=num%10
    total = int(total)+int(m)
    num = num/10
print(f"Sum of Digites:{total}")
    

