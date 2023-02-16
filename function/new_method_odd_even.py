#new Method odd Even Check
def number(num):
    if num%2 == 0:
        return "Even"
    return "Odd"
n = int(input("Enter The Num:"))
total = number(n)
print(total)