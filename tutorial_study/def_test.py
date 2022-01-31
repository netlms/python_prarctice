# simple 'def' examples

def print_list(arr):
    for i in arr:
        print(i)

# 'return' example

def add(a, b):
    return (a + b)

print(add(2, 4))
print(add('a', 'b'))

# 'True' or 'False'

def torf():
    ans = int(input('1 + 1 = '))
    return((1 + 1) == ans)

print(torf())