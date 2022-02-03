"""
다음은 tkinter를 활용해 그림과 같은 창을 띄우는 코드입니다. 빈칸을 채우세요.

import tkinter as tk

s = "Life is short\nUse Python"

root = tk.Tk()
t = tk.Text(root, height=█, width=██)
t.insert(tk.END, █)
t.pack()
tk.mainloop()
"""

import tkinter as tk

s = "Life is short\nUse Python"

root = tk.Tk()                              # define new window obj
t = tk.Text(root, height=2, width=13)       # create new text in root
t.insert(tk.END, s)                         # 'END' means the position of end of text
t.pack()
tk.mainloop()


# import tkinter as tk

# s = "Life is short\nUse Python"

# root = tk.Tk()
# t = tk.Text(root, height=2, width=13)
# t.insert(tk.END, s)
# t.pack()
# tk.mainloop()