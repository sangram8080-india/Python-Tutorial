#wap To print of Rever value for Three Value 
#input Throungh The Keyboard

num= int(input("Enter The value of Any Threee Digit Num:"))
rev=0

temp = int(num)%10  #temp = 123%10 = 3
num =  int(num)/10   #num = 123 /10 = 12
rev =  int(rev)*10+int(temp) #num =0+3 = 3

temp  = int(num)%10
num = int(num)/10
rev = int(rev)*10+int(temp)

temp = int(num)%10 
rev = int(rev)*10+int(temp)


print("rever Value of The Num:"+str(rev))