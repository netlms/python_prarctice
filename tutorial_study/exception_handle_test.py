# try-except examples

# error examples
# print(1/0)                  # cannot divide by 0. 'ZeroDivisionError: division by zero'
# print('fdf' * 'as')         # wrong type for the operation. 'TypeError: can't multiply sequence by non-int of type 'str''

# exception handling example
def division(a, b):
    try:
        return (a / b)
    
    except ZeroDivisionError:           # runs when 'ZeroDivisionError' occur
        return ('cannot divide by 0!')
    
    except TypeError:                   # runs when 'TypeError' occur
        return ('argument must be number type!')
    
    except:                             # runs when any kind of error occur
        return ('Error!')
        
print(division(5, 0))
print(division('fdf', 'as'))