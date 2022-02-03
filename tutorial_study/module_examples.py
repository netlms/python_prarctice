# serveral modules examples

# 'pickle' example

import pickle

family_height = {'father' : 181, 'mother' : 165, 'son' : 179, 'grandfather' : 172}

f = open('.\\tutorial_study\\pickle_module_example', 'wb')              # 'wb' means to write data in byte form

pickle.dump(family_height, f)              # dump() record dict 'family_height' data in the file 'f'

f.close()

f = open('.\\tutorial_study\\pickle_module_example', 'rb')              # 'rb' means to read data in byte form

d = pickle.load(f)              # pickle.load(file) loads data from file

print(d)
# pickle can write any data generated from python to files

# os.path.exists()
import os

print(os.path.exists('.\\tutorial_study\\pickle_module_example'))       # os.path.exists(file_path) return True when the file or directory exists in file_path

# glob module
from glob import glob

print(glob('*'))            # glob(path_name) returns the list of files with path_name, in current directory
print(glob('tutorial_study\\module*'))

# os.path module

from os.path import isdir               # isdir(path) returns True when path is a directory

for i in glob('tutorial_study\\*'):
    if isdir(i):
        print(i, 'is a diresctory')
    else:
        print(i, 'is a file')