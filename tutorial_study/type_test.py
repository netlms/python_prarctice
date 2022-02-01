# simple 'type' test

# number
print(type(1))          # int
print(type(1.1))        # float
print(type(1+2j))       # complex

print()

# sequence
print(type('str is string'))                # str
print(type(['this', 'is', 1, 'list']))      # list
print(type(('this', 'is', 1, 'tuple')))     # tuple

print()

# str slicing
str = 'this is string'

piece = str[0:6]        # piece = 'this i'
print(f'piece = str[0:6] : \'{piece}\'')
piece = str[4:2]        # piece = ''
print(f'piece = str[4:2] : \'{piece}\'')
piece = str[4:4]        # piece = ''
print(f'piece = str[4:4] : \'{piece}\'')
piece = str[:6]         # piece = 'this i'
print(f'piece = str[:6] : \'{piece}\'')
piece = str[-8:]        # piece = 's string'
print(f'piece = str[-8:] : \'{piece}\'')
piece = str[-8:-2]      # piece = 's stri'
print(f'piece = str[-8:-2] : \'{piece}\'')
piece = str[-4:-7]      # piece = ''
print(f'piece = str[-4:-7] : \'{piece}\'')
piece = str[:]          # piece = 'this is string'
print(f'piece = str[:] : \'{piece}\'')
piece = str[::-1]       # piece = 'gnirts si siht'
print(f'piece = str[::-1] : \'{piece}\'')
piece = str[0::-1]       # piece = 't'
print(f'piece = str[0::-1] : \'{piece}\'')
piece = str[5::-1]       # piece = 'i siht'
print(f'piece = str[5::-1] : \'{piece}\'')
piece = str[-1::-1]       # piece = 'gnirts si siht'
print(f'piece = str[-1::-1] : \'{piece}\'')
piece = str[-3::-1]       # piece = 'irts si siht'
print(f'piece = str[-3::-1] : \'{piece}\'')
piece = str[::-2]       # piece = 'git ish' (GnIrTs' 'sI SiHt)
print(f'piece = str[::-2] : \'{piece}\'')
piece = str[::-3]       # piece = 'gr  h' (GniRts' 'si' 'siHt)
print(f'piece = str[-3::-1] : \'{piece}\'')

print()

# dict
dic = ({'one' : 1, 'two' : 2, 'three' : 3})
print(type(dic))

print()

# bool
print(type(True))
print(type(1 < 2))
print(type(1 == True))

print()

# set
st = {1, 'two', 3, 'four', 5}
print(st)                   # {1, 3, 5, 'two', 'four'}
# set contains no duplicated elements and elements have no order 
st = {1, 'two', 3, 'four', 5, 1, 'four'}
print(st)                   # {1, 3, 5, 'two', 'four'}