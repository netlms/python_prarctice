# simple set examples

# create set
st = {'a', 2, 'c'}

print(type(st))
print(st)
# set elements don't have order
# set doesn't allow duplicated elements

# add() adds an element to set
st.add('d')

print(st)

# create empty set
st2 = set()
print(type(st2))

# fill st2
st2 = {'mon', 'tue', 'wed'}

print(st2)

# set operations &, |, -
st = {'a', 'b', 'c', 'd'}
st2 = {'c', 'd', 'e', 'f'}

print(st & st2)
print(st | st2)
print(st - st2)