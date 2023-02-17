def mutliply(*args):
    mutliply = 1

    print(args)

    for i in args:
        mutliply *= i
    
    return  mutliply 

num = [2,3,4]

print(mutliply(*num))  #unpacking