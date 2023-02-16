#d = {
#    'name':'unknown',
#    'age':'unknown',
#    'hight':'unknwon'

#}

#d =dict.fromkeys(['name','age','hight'],'unknown') or same output

d = dict.fromkeys(('name','age','hight'),'unknown')
print(d)