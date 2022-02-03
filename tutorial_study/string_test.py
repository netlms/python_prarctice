# simple string examples

str = 'this is string'

print(f'str : {str}')
print(f'str[0] : {str[0]}')
print(f'str[0:0] : {str[0:0]}')
print(f'str[0:1] : {str[0:1]}')
print(f'str[0:2] : {str[0:2]}')
print(f'str[0:3] : {str[0:3]}')
print(f'str[:0] : {str[:0]}')
print(f'str[:1] : {str[0:1]}')
print(f'str[:2] : {str[:2]}')
print(f'str[:3] : {str[:3]}')
print(f'str[0:] : {str[0:]}')
print(f'str[1:] : {str[1:]}')
print(f'str[2:] : {str[2:]}')
print(f'str[3:] : {str[3:]}')
print(f'str[3:12] : {str[3:12]}')

# ! cannot change values in string. ex) str[0] = 'x' doesn't work.
# if string values have to be changed, use the method below

# str = 'string' and it has to be changed into 'Ptring'. then....

str = 'string'

str = 'P' + str[1:]

print(str)

# or 'PtrinGs

str = str[:5] + 'Gs'

print(str)

# find() returns the index of parameter in the list

index = 'hi python'.find('y')
print(index)

# if there are duplicate letters, then return the index of the first letter

index = 'abcdefcg'.find('c')
print(index)

# strip(), lstrip(), rstrip() remove letters which are same as the one given as parameter from the string.
# lstrip() works from the left of the string, rstrip() works from the right and strip() from both ways
# if there is no parameter given, remove spaces

str = '   a1b2c3d4e5f6g7   '

print(str.lstrip(' a1b2c'))
print(str.lstrip('abc12 '))
print(f'\'{str.lstrip()}\'')
print(str.rstrip('5f6g7 '))
print(str.rstrip(' fg567'))
print(f'\'{str.rstrip()}\'')
print(str.strip(' a1b26g7 '))
print(str.strip('7621gba '))
print(f'\'{str.strip()}\'')

# split() splits string by parameter and return as list. if there is no parameter, splits by space

str = 'this is string'

sp = str.split()

print(sp)
print(f'\'{sp[0]}\' \'{sp[1]}\' \'{sp[2]}\'')

sp = str.split('s')

print(sp)
print(f'\'{sp[0]}\' \'{sp[1]}\' \'{sp[2]}\'')