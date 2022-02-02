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
reload(tkinter)

# the contents loaded from module overlap the original contents
