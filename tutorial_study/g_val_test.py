# global variable example

def x_var():
    x = 'x'
    print(f'x is {x}')

x_var()
print(x)
# NameError: name 'x' is not defined. x only exists in 'x_var' function

x = 'X'

def x_var():
    print(f'x is {x}')

x_var()
print(x)
# x is X
# X
# "x = 'X'" in the first line is global variable. it can exit in inside of func or outside eider.
# if x is declared in func simultaneously, x in func is considered as local var and different var from outside one.

def x_var():
    global x
    x = 'x'
    print(f'x is {x}')

x_var()
print(x)
# using 'global' keyword in func can create global var inside of func