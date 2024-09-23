ASTRIX ="*"
print('\n' + ASTRIX*60 + '\n')

#1. oop
class refrigerator:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
    def door(self):
        print('Open the refrigerator')

    def button(self):
        print('Set the refrigerator temperature to high ')
    def printInfo(self):
        print(f'Model ---> {self.model} Color  ---> {self.color} Price  ---> {self.price}')

frige1 = refrigerator('KBSD708MPS', 'white', 3399)
frige2 = refrigerator('JBSFS48NMX', 'Grey', 2145)
frige3 = refrigerator('RS36A72J1N', 'Siver', 5299)

frige1.printInfo()
frige2.printInfo()
frige3.printInfo()
frige2.button()
frige3.door()
print('\n' + ASTRIX*60 + '\n')

# 2. List

list_sport = []
for i in range(5):
    sport = input("Enter Sport type : ")
    list_sport.append(sport)
print(list_sport)

list_sport.insert(3, "Hiking")
print(list_sport[1:4])

list_sport.append('Cycling')
print(list_sport[-1])
print(len(list_sport))

print(f'Maximum ---> {max(list_sport)}')
print(f'Minimum ---> {min(list_sport)}')
print(tuple(list_sport))

print('\n' + ASTRIX*60 + '\n')

# 3. File

file_name = 'sport.txt'
file_handle = open(file_name, 'w')
for sport in list_sport:
     file_handle.write(sport + '\n')
file_handle.close()

with open(file_name, 'a') as fh:
    fh.write('Swimming' + '\n')
    fh.write('skiting' + '\n')
    fh.write('Snow boarding' + '\n')

with open(file_name, 'r') as fp:
    print(fp.read())

fp = open(file_name, 'r')
lines = len(fp.readlines())
print('\nTotal number of line :', lines)
fp.close()

print('\n' + ASTRIX*60 + '\n')

# 4. Dictionary

order_dict = {3901: 451.50, 1405: 310.45, 3026: 257.87, 6493: 46.60, 5949: 75.95}
salesperson_dict = {3901: 'Jose', 1405: 'Jesus', 3026: 'Pedro', 6493: 'Carlos', 5949: 'Paula'}
num_item_dict = {3901: 12, 1405: 8, 3026: 5, 6493: 2, 5949: 4}

list_keys = list(order_dict.keys())

while True:
    order_num = int(input('Enter the order number : '))
    if order_num in list_keys:
        break
    else:
        print('Invalid order number ... ')

print(f'\nTotal price :\t{order_dict[order_num]} \nSales Person name :\t{salesperson_dict[order_num]} \nNumber of item orderd :\t{num_item_dict[order_num]}\n')

print('\n' + ASTRIX*60 + '\n')

# 5. Set
sportset = {'swimming', 'skiing', 'skateboarding', 'hockey'}

print(sportset)
print(len(sportset))
sportset.update(set('red'))
print(sportset)

try:
    sportset.remove('v')
except:
    print(' An Exception occurred')

print('\n' + ASTRIX*60 + '\n')