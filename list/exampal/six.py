#define a function which will take list as a arguments and list function 
#will return a reversed list

#[1,2,3,4]------>[4,3,2,1]

numbers = list(range(1,11))
#print(numbers[::-3])
def revers_num(l):
    revers = []

    for i in l:
        revers.append(numbers[-i])
    return revers
print(revers_num(numbers))