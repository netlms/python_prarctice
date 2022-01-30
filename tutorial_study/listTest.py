"""
list practice
"""

# create list
arr = ['a', 'b', 'c']
print(arr)

# get list len
print(len(arr))

# get list element
print(arr[0])

# remove list element
arr.remove('a')
print(arr)
# "remove" function takes only one parameter each time

# what happen if there are more than two same elements in a list?
arr1 = ['a', 'b', 'c', 'a', 'd', 'c']
arr1.remove('a')
print(arr1)
# the result is "['b', 'c', 'a', 'd', 'c']". remove only the first element 

