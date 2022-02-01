# simple list practice

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

# what happens if there are more than two same elements in a list?
arr1 = ['a', 'b', 'c', 'a', 'd', 'c']
arr1.remove('a')
print(arr1)
# the result is "['b', 'c', 'a', 'd', 'c']". remove only the first element 

# append() adds parameter as a new element to the end of list
d = 'd'

print(f'append \'{d}\' to {arr} : ', end='')
arr.append(d)
print(arr)

# if the parameter is a list, the list itself is added as a element
ef = ['e', 'f']

print(f'append list {ef} to {arr} : ', end='')
arr.append(ef)
print(arr)

# if you want to add the element from list to list by one by one, use extend()
arr = ['a', 'b', 'c', 'd']

print(f'add elements of the list {ef} to {arr} : ', end='')
arr.extend(ef)
print(arr)

# sort() sorts elements of list in ascending order
num = [1, 6, 2, 5, 4, 3]

print(f'sort the list {num} :', end='')
num.sort()
print(num)

# sort() has parameter 'reverse'. if reverse==True, sort the list in descending order
num = [1, 6, 2, 5, 4, 3]

print(f'sort the list {num} :', end='')
num.sort(reverse=True)
print(num)

# sorted() creates a new list by the parameter list with sorting. unlike sort(), sorted() can take any iterable(include dict) more than just list
print(sorted([1, 6, 2, 5, 4, 3]))
print(sorted([1, 6, 2, 5, 4, 3], reverse=True))

# insert(index, element) adds parameter to the index of list
arr = ['b', 'c', 'd']

print(f'add \'a\' to the list {arr} : ', end='')
arr.insert(0, 'a')
print(arr)

# if the parameter is a list, the list itself is added as a element like sort()
ef = ['e', 'f']

print(f'add \'{ef}\' to the list {arr} : ', end='')
arr.insert(4, ef)
print(arr)

# del is a python keyword (ex. if, for, or, and). removes elements from the list
arr = [1, 2, 3, 4, 5]

del arr[0]
print(arr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del arr[3:7]
print(arr)

# pop(index) removes a element in the index of list. it returns removed value
arr = ['a', 'b', 'c', 'd', 'e']

print(arr.pop(2))

# del is the fastest among del, pop(), remove()

# list in the list
arr = ['a', 'b', ['c1', 'c2', 'c3'], 'd', ['e1', 'e2'], 'f']

print(arr)
print(arr[0])
print(arr[2])
print(arr[2][1])
print(arr[4][0])

# matrix in list form

mat = [['(0,0)', '(0,1)', '(0,2)'], ['(1,0)', '(1,1)', '(1,2)'], ['(2,0)', '(2,1)', '(2,2)']]

print(mat[0][0])
print(mat[0][1])
print(mat[1][1])
print(mat[1][2])
print(mat[2][0])
print(mat[2][2])

