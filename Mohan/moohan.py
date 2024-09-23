import os
from zipfile import ZipFile
import csv

import pandas

df = pandas.read_csv("data.csv")

df["Age"] = "24"
df.head()

print(df)

with open("data.csv", 'r') as file:
     csvreader = csv.reader(file)
     for row in csvreader:
         print(row)

'''
directory = 'C:/workspace/python/Mohan/'
allZipFile = [f for f in os.listdir(directory) if f.endswith('.zip')]

foreach zipf in allZipFile:
    print(zipf)
    with ZipFile(zipf, 'r') as shard:
        shard.extractall()

'''
'''
class Moohan_Dir:

    def ___init__(self):
        pass
    def FirstMethod(self):
        path = os.path.dirname('C:/workspace/python/')

        print(path)

        strPath = os.path.realpath(__file__)
        print(strPath)

        listFolder = strPath.split(os.path.sep)
        print(listFolder)

        dirList = [f for f in os.listdir() if os.path.isdir(f)]


        print(dirList)
        print(dirList[0])
        for s in dirList:
            print(str(s[5:]))
        
def main():
    moohanDir = Moohan_Dir()
    moohanDir.FirstMethod()
 
 
if __name__ == __"__main__:
     main()
    
'''
