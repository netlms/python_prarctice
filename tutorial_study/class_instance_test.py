# simple class & instance examples

# easy example
from asyncio.windows_events import NULL


class people():
    cl = 'people'
    name = 'name'
    age = 0
    height = 0
    weight = 0
    
    def __init__(self):                 # '__init__' method runs when the object is defined
        print('a new object is created')
        
    def print_people(self):             # func defined in class is called 'method'. 'self' points the object of the class (instance)
        print(f'class : {self.cl}')
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')
        
    def __repr__(self):                 # the return value of '__repr__' method is printed by 'print(object)'
        return (self.name)
        
    def __del__(self):                  # '__del__' method runs when the object is removed
        print('the object {} is removed'.format(self.name))

john = people()               # 'john' object is the instance of the class 'family'

john.name = 'John'
john.age = 50
john.height = 180
john.weight = 70

print(john)

john.print_people()
print()
# methods with the name '__*__' are called magic method.

# inheritance example
class family(people):           # 'family' class inherits attributes of the class 'people'
    cl = 'family'
    role = 'role'
    
    def print_family(self):
        self.print_people()
        print(f'role : {self.role}')
        
kate = family()
kate.name = 'Kate'
kate.age = 45
kate.height = 165
kate.weight = 50
kate.role = 'mother'

kate.print_family()
print()

# 
class calculation():
    
    def __init__(self, num):
        self.num = num
        print(f'new object created with num = {self.num}')
        
    def __add__(self, other):               # '__add__' method overloads '+' operation. when '{object} + {object}', it returns '__add__()' retrun value
        return (self.num + other.num)
    
    def __eq__(self, other):                # '__eq__' method overloads '==', '!=' operation
        if self.num == other.num:
            return True
        else:
            return False
    def __lt__(self, other):                # '__lt__' method overloads '>', '<' operation
        if self.num < other.num:
            return True
        else:
            return False
                
    def __del__(self):
        print('\'calculation\' object {} is removed'.format(self.num))
    
    
a = calculation(4)
b = calculation(5)

print(f'a + b = {a + b}')
print(f'a.__add__(b) = {a.__add__(b)}')         # 'a.__add__(b)' returns the value equal to 'a + b'
print(f'a == b = {a == b}')
print(f'a != b = {a != b}')
print(f'a < b = {a < b}')
print(f'a > b = {a > b}')

# examples of operation overloading methods
# __add__(self, other) : 이항 + 연산자(A + B, A += B)
# __sub__(self, other) : 이항 - 연산자(A - B, A -= B)
# __mul__(self, other) : 이항 * 연산자(A * B, A *= B)
# __truediv__(self, other) : 이항 / 연산자(A / B, A /= B)
# __floordiv__(self, other) : 이항 // 연산자(A // B, A //= B)
# __mod__(self, other) : 이항 % 연산자(A % B, A %= B)
# __pow__(self, other) : 이항 연산자(A B, pow(A, B))
# __lshift__(self, other) : 이항 << 연산자(A << B, A <<= B)
# __rshift__(self, other) : 이항 >> 연산자(A >> B, A >>= B)
# __and__(self, other) : 이항 & 연산자(A & B, A &= B)
# __xor__(self, other) : 이항 ^ 연산자(A ^ B, A ^= B)
# __or__(self, other) : 이항 | 연산자(A | B, A |= B)
# __not__(self) : 단항 ~ 연산자(~A)
# __abs__(self) : 단항 절대값 연산자(abs(A))

# __lt__(self, other) : < 연산자 - Less than(self가 other 미만인지)
# __le__(self, other) : <= 연산자 - Less than or equal to(self가 other 이하인지)
# __gt__(self, other) : > 연산자 - Greater than(self가 other 초과인지)
# __ge__(self, other) : >= 연산자 - Greater than or equal to(self가 other 이상인지)
# __eq__(self, other) : == 연산자 - Equal to(self와 other가 같은지)
# __ne__(self, other) : != 연산자 - Not equal to(self와 other가 다른지)

