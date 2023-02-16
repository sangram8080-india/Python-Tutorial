#d = {'a':1,'b':2,'c':3,'a':4}
#print(d)

def word_count(s):
    count ={}

    for char in s:
        count[char]= s.count(char)

        return count

print(word_count('sangram'))
