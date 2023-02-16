#wap to check True and False //Boolean value 
#even = True and Odd = Flase

def t_f_odd_even(num):
    if num%2 == 0:
        return True
    return False

n = int(input("Enter The Num:"))

temp = t_f_odd_even(n)
print(temp)