def mutliply_num(*args):
    mutliply = 1

    for  i in args:
        mutliply *=i

    return mutliply


print(mutliply_num(1,2,3,4))