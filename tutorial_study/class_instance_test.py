# simple class & instance examples

# easy example

class people():
    cl = 'people'
    name = 'name'
    age = 0
    height = 0
    weight = 0
    def print_people(self):             # func defined in class is called 'method'. 'self' points the object of the class (instance)
        print(f'class : {self.cl}')
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')

john = people()               # 'john' object is the instance of the class 'family'

john.name = 'John'
john.age = 50
john.height = 180
john.weight = 70

john.print_people()
print()

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
