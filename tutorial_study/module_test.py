# simple module practice

# using 'math' module
import math
import tkinter

print(math.sqrt(2))
print(math.sqrt(4))
print(math.sqrt(6))
print(math.sqrt(8))
print(math.sqrt(9))

print(math.pi)
# 'pi' is a variable defined in 'math' module

# using 'calendar' module
import calendar

calendar.prmonth(2000, 1)

# using 'tkinter' module
from tkinter import *       # load certain contents from module (* to load all contents) 

tk = Tk()
win = Label(tk, text='hi python!')
win.pack()
tk.mainloop()

# using 'del' to remove module
del tkinter

# using 'importlib' to reload removed module
from importlib import reload
reload(calendar)
# the contents loaded from module overlap the original contents

# 'random' module provides options to generate random numbers
import random

print(random.random())          # random.random() returns random number between 0 ~ 1
print(random.randrange(1, 7))   # random.randrange(1, 7) returns integer between 1 ~ 6
seq = [1, 2, 3, 4, 5]
random.shuffle(seq)             # random.shuffle(seq) shuffles elements in the sequence
print(seq)
print(random.choice(seq))       # random.choice(seq) returns a random elements in the sequence

# 'sys' module controls shell options
import sys

# sys.ps1 = '>>> '. sys.ps1 shows the line indicator in interpreter
# sys.exit() closes python interpreter

# 'os' module controls OS options
import os

print(os.getcwd())              # os.getcwd() returns current working directory
print(os.listdir())             # os.listdir() returns the directories in cwd
os.chdir('tutorial_study')      # os.chdir(dir) changes cwd to dir
print(os.getcwd())              
os.chdir('..')                  # '..' means parent directory
print(os.getcwd())

# 'webbrowser' provides web browser control options
import webbrowser

webbrowser.open('www.google.com')

# 're' module provides control by regular expression 
import re, glob
p = re.compile('.*p.*n.*')
for i in glob.glob('*'):
    m = p.match(i)
    if m:
        print(m.group())
        
