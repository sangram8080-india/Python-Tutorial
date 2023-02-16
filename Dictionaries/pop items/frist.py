#wap to print pop items using python 

user_info ={
    'name':'sangram',
    'age':20,
    'fev_moves':['loco','kimi no na na'],
    'fev_tunnes':['awakening','fairy tale']
}

poppen_items = user_info.popitem()

print(poppen_items)
print(user_info)