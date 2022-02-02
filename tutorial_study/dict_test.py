# simple dictionary examples

# create dict
dic = {1 : 'one', 2 : 'two', 3 : 'three'}

print(dic[1])
# elements have 'x : y" form. x is key and y is value. elements have no order

keys = list(dic.keys())         # return all keys in the dict in iterable type
values = list(dic.values())     # return all values in the dict in interable type

print(f'keys : {keys}')
print(f'values : {values}')

del dic[3]              # remove key and value
print(dic.keys())
print(dic.values())

print((1 in dic))       # return True if the argument exist in the dict as a key. else, return false
print((2 in dic))
print((3 in dic))


# update(dict) adds elements of dict to another dict. if the key already exists, it changes value to new one
dic1 = {1 : 'one', 2 : 'too'}
dic2 = {2 : 'two', 3 : 'three', 4 : 'four'}

dic1.update(dic2)

print(dic1)