#wap to print 1 to 10 but not print for 5
#1,2,3,4,6,7,8,9,10

for i in range(1,11):
    if i == 5:
        continue
    print(i)