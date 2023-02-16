def word_container(s):
    count ={}

    for char in s:
        count[char] = s.count(char)
    return count
print(word_container('manjay bharati '))
