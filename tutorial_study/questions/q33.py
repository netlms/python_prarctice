"""
2021년 3월의 달력을 표시하는 창을 띄우는 코드를 작성하세요.
"""

from calendar import *
from tkinter import *

if __name__ == '__main__': 
    cal = TextCalendar()
    c = cal.formatmonth(2021, 3)
    
    line = 0
    for i in c:
        if i == '\n':
            line += 1
    
    tk = Tk()
    win = Text(tk, height=line, width=21)
    win.insert(END, c)
    win.pack()
    mainloop()
    
# import calendar
# import tkinter as tk

# c = calendar.TextCalendar()
# m = c.formatmonth(2021, 3)

# root = tk.Tk()
# t = tk.Text(root, height=7, width=20)
# t.insert(tk.END, m)
# t.pack()
# tk.mainloop()