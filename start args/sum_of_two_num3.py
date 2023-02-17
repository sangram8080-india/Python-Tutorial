def add(a,b):

    return a+b

def all_total(*args):
    total = 0

    for num in args:
        total = total+num
    
    return total
print(all_total(3,4,5,56,5))