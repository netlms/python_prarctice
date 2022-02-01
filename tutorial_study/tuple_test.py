# simple tuple examples

# format
t = ('this', 'is', 'tuple')
u = 'this', 'is', 'tuple'       # brackets are optional with elements
p = 'tuple',                    # one element ends with comma means a tuple with only one element
l = ()                          # empty brackets means tuple with no element

print(t)
print(u)
print(p)
print(l)

# variadic argument (*a) example
def example(a, *b):
    print(a, b)

example(1, 2, 3, 4, 5)
# variadic argument has tuple format

# tuple needs slicing for edition
t = (1, 2, 3, 4, 5)
u = t[1:]
p = t[:2],'three', t[3:]
l = t[:2],('three'), t[3:]
e = t[:2] + ('three',) + t[3:]

print(u)
print(p)
print(l)
print(e)

# tuple-list type casting
t = ('this', 'is', 'tuple')

print(list(t))
t = list(t)
print(tuple(t))