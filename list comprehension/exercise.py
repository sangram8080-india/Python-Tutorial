#define a functions that take list of string 
#using list comprehension revers of every string 
#l =['abc','tuv','xyz']

#simpal 
#def revers_str(l):
#    new_list =[]
#    for name in l:
#        new_list.append(name[::-1])
#    return new_list
#print(revers_str(l))

def revers_str(l):
    return [name[::-1] for name in l]
print(revers_str(['abc','tuv','xyz']))

