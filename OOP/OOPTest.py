
'''
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def get_full_name(self):
        return f'{self.fname} {self.lname}'
    
    
    def introduce(self):
        return f"Hi I'am {self.fname} {self.lname}. I'm {self.age} is old"
    @classmethod    
    def create_anonymous(cls, cls_str):
        f_name, l_name, age = cls_str.split('-')
        return cls(f_name, l_name, age)
    
    @classmethod
    def create_anonymous1(cls):
        return Person('Tersit', 'Tafesse', 34)
    
    
    
    
person = Person('Brook', 'Ashami', 40)

print(Person.__dict__)

print('\n----------------------------------------------------------------------------------------------------\n')
print(person.introduce())
print(person.get_full_name())
print(person.__dict__)

name_str = 'John-Doe-45'
per = Person.create_anonymous(name_str)
print(per.get_full_name())

an = Person.create_anonymous1()
print(an.introduce())

'''


'''
    1. Assigninh Function to variable
    2. Defining function inside other function
    3. Passing function as argument to other function
    4. Function returning other function
    5. Nested function have access to the enclosing function's variable scope
    6. Creating Decorators   

'''
def plus_one(number):
    return number + 1
add_one = plus_one
print(add_one(4))
#*******************************************
def plus_one1(number):
    def add_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(5))
#*****************************************************

def plus_one2(number):
    return number + 1

def function_call(function):
    num_to_add = 6
    return function(num_to_add)
print(function_call(plus_one))
#*******************************************************

def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi
hello = hello_function
print(hello())

#************************************************
def print_message(message):
    def message_sender():
        print(message)
    message_sender()
print_message("Some Random Message")
#***********************************************
