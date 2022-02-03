# file, text control

# read contents from 'C:\Users\MSL\git\python_prarctice\tutorial_study\file_test.txt'
f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt')
r = f.read()

print(r, '\n')

# write on 'file_test.txt'
f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt', 'w')       # second argument 'w' in open() allows to write new info to the file
f.write('I write this line by write(a, \'w\')')                                             # write() writes new info to the file. the existing info would be replaced
f.close()                                                                                   # the edited data saved when close() runs

f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt')
r = f.read()

print(r, '\n')

# to add new info to existing info, use 'a+' instead of 'w'
f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt', 'a+')
f.write('\nI write this line by write(a, \'a+\')')
f.close()

f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt')
r = f.read()

print(r, '\n')

# readline() returns line by line from the file
f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt', 'w')
f.write('a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn')
f.close()

f = open('C:\\Users\\MSL\\git\\python_prarctice\\tutorial_study\\file_test.txt')
r = f.readline()
print(r)

# use seek(x) to set the head of readline(), readlines() to x line
f.seek(0)

for i in range(5):
    print(f.readline())
    
# readlines() returns a list with elements from the text file. each line turns into a element
line = f.readlines()
print(line)

for i in line[-1:]:
    print(i)