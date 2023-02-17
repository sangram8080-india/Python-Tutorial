num = list(range(1,11))

def negative_num(l):
    negative = []
    for i in num:
        negative.append(-i)
    return negative

print(negative_num(num))