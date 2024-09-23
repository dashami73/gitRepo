import argparse,string, random
import math
TEXT = string.ascii_letters + string.digits + string.punctuation
MYDICT = {"Brook": 50}
num2 = 10

parser = argparse.ArgumentParser(prog='parseClarg', usage='whoa use: %(prog)s [options] number',description='print random number of character', epilog="if it were green it would be like the matrix")

parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--Height', type=int, metavar='', required=True, help='Height of Cylinder')
parser.add_argument("-m", "--mydict", action="store", required=False, type=dict, default=MYDICT)

group1 = parser.add_argument_group('group1', 'group1 description')
group1.add_argument('num', type=int)



groupe = parser.add_mutually_exclusive_group()
groupe.add_argument('-q', '--quiet', action='store_true', help='print quiet')
groupe.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args(num2)

def strprint(number):
    for _ in range(number):
        content = [random.choice(TEXT) for _ in range(20)]
        print('  '.join(content))
def volume_cylinder(radius, height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ == '__main__':
    strprint(args.num)
    print(args.mydict)
    volume = volume_cylinder(args.radius, args.Height)
    if(args.quiet):
        print(volume)
    elif(args.verbose):
        print("Volume of cylinder with radius %s and  height %s is %s" % (args.radius, args.Height, volume))
    else:
        print("Volume of cylinder is %s " % (volume))