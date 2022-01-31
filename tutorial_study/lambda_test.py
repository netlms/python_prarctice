# lambda examples

def add(a, b):
    return(a + b)

add(1, 2)
# and
(lambda a, b: a + b)(1, 2)
# both func above have same contents

print(list(map((lambda x: x * 2), range(1, 11))))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# map(func, list) runs func with each elements of the list and return the result as iterable. 

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 5)))
# 10 (((1 + 2) + 3) + 4)
# reduce(func, seq) applies func to each element of the sequence cumulatively. the result of 'x + y' would be the next x.
# seq : list, string, tuple

print(list(filter((lambda x: x >= 10), range(0, 21))))
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# filter(func, list) creates new list with elements of parameter list which return 'True' value in func parameter.fd