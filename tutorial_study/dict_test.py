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
