from typing import List, Tuple, Dict
class rectangle:
    def __init__(self, w:int, h:int) -> None:
        self.width=w
        self.height=h
def area(r:rectangle) -> int:
    return r.width*r.height
r1=rectangle(10,20)
print('area = ', area(r1))


cities : List[str] = ['Mumbai', 'Addis Ababa', 'San Jose']
employee : Tuple[str, int, float] = ('Brook', 23, 10000.95)
marklist: Dict[str, int] = {'Brook': 26, 'Amy':5}

# how to handdle exception in python

def division(a:int, b:int) ->float:
    try: 
        result =  a/b
        return result
    except ZeroDivisionError:
        print("Error, Division by zero is not allowed.")
    except TypeError:
        print("Error, Invalid input types. Both argument must be number")
    else:
        print(f'Result : {result}')
    finally:
        print('Division operation completed')
 
fraction = division(10, 2)
print(fraction)
fraction = division(10, 2.1)
print(fraction)
fraction = division(10, '2')
print(fraction)
fraction = division(10.2, 2)
print(fraction)

# Raise / throw exeeption

user_id = input("Einter user id: ")
1if type(user_id) is not int:
    raise TypeError("only Intergers are allowed")

#lambda, map, filter, 

prices = [2, 3, 4, 5, 1, 2]
over_three_1 = [x for x in prices if x > 3]

over_three = list(filter(lambda price : (price > 3), prices))

print(over_three_1)
print(over_three)

add = lambda x, y : x + y

print(add(30, 50))

#unpacking/starred expression (*) to assign multiple values to a variable

def func():
    list1 = [1,2,3,4,5,6]
    return list1
a, b, *c, d = func()
print(a, b, c, d)