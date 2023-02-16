#wap to print 0 1 1 2 3 5 8 13 21
#using dependence 
def fibonaticci_squ(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a,b) #a,b, 0,1
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c= a+b
            a=b
            b=a+b
            print(b,end=" ")
fibonaticci_squ(10)