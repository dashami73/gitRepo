
'''
    getattr(object, attribute, default)
    hasattr(object, attribute)
    setattr(object attribute)
    delattr(object, attribute)
'''

class Employee:
    'common base class for all employee'
    num_emp = 0
    raise_amt = 1.04
    def __init__(self, first, last, salaty):
        self.first = first
        self.last = last
        self.salary =salaty
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_emp += 1
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return True
        else:
            return False
        

    def display(self):
        print(f'first name :{self.first}, last name: {self.last} , email : {self.email} and salary {self.salary}')

class Developer(Employee):
    def __init__(self, first, last, salaty, lang):
        super().__init__(first, last, salaty)
        #Employee.__init__(self, first, last, salaty)
        self.lang = lang


class Manager(Employee):
    def __init__(self, first, last, salaty, employess = None):
        super().__init__(first, last, salaty)
        if employess is None:
            self.employess = []
        else:
            self.employess = employess
    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)
    def print_emp(self):
        for emp in self.employess:
            print('-->', emp.fullName())
            

dev_1 = Developer('brook', 'ashami', 60000, 'python')
dev_2 = Developer('Robel', 'Ashami', 50000, 'C++')

mgr_1 = Manager('Brook', 'Ashami', 90000, [dev_1])

print(mgr_1.email)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
'''
print(dev_1.email)
print(dev_2.lng)
#print(help(Developer))

emp_str_1 = 'Brook-Ashami-70000'
emp_str_2 = 'Robel-Ashami-60000'
emp_str_3 = 'Amy-Ashami-50000'

first, last, pay = emp_str_1.split('-')

emp3 = Employee(first, last, pay)
print(emp3.email)
print(emp3.salary)

emp4 = Employee.from_string(emp_str_3)
print(emp4.email)
print(emp4.salary)


import datetime
my_date = datetime.date(2023, 7, 10)
print(Employee.is_weekday(my_date))

emp1.display()

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
'''