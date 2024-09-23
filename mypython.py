

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))