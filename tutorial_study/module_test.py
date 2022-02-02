# simple module practice

# using 'math' module
import math

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

from tkinter import *

tk = Tk()
win = Label(tk, text='hi python!')
win.pack()
tk.mainloop()
