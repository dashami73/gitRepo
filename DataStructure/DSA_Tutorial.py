from collections import deque
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def setNode(self, next):
        self.next = next
    def getNode(self):
        return self.next
    def getData(self):
        return self.data
class linkedList:
    def __init__(self, data=None):
        self.head = Node(self)

    def getHeadNode(self):
        return self.head

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.setNode(self.head)
        self.head = new_node


    def printData(self):
        p = self.head
        while p != None:
            print(p.data)
            p = p.next
''' 

def DSA_stack():
    stack = deque()
    stack.append('a')
    stack.append('b')
    stack.append('d')
    print(stack)
    print()

def main():
    DSA_stack()
    LList = linkedList()
    LList.head = Node("Mon")
    N2 = Node("Tue")
    N3 = Node("Wed")
    N4 = Node("Thr")
    N5 = Node("Fri")
    LList.head.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5
    LList.printData()
'''
def main():
    pass

if __name__=='__main__':
    main()