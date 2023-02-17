#scope 
#deffrence b\w local var and Global var 

x =5 #global var
def fun():
    x=7  #local Var 
    return x
#def fun2():
#   print(x)  not using Global Var

#fun2()
#but 
print(fun()) #using Global var
print(x)