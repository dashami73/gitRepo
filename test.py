import random
import pdb

breakpoint()
def square():
    x = range(1, 4)
    for n in x:
        yield n**2
            
for y in square():
    print(y)

print(dir(pdb))
print(help(pdb))
print(dir(random))
print(help(random))
