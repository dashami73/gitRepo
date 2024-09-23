class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def listprint(self):
        if self.head == None:
            raise ValueError("List is empty")
        printval = self.head
        while printval is not None:
            print(printval.data, end=" ")
            printval = printval.next
        print('\n')
    def search(self, head, data, index):
        if head.data == data:
            print(index)
        else:
            if head.next:
                return self.search(head.next, data, index+1)
            else:
                raise ValueError("Node not in linked list")
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while(current):
            size+=1
            current = current.next
        return size
    def addAtBegining(self, data):
        tmp = Node(data)
        tmp.next =self.head
        self.head = tmp

    def AddAtEnd(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next=tmp

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def insertNode(self, node, data):
        if node is None:
            return
        cur = Node(data)
        cur.next = node.next
        node.next = cur

    def delete(self, remKey):
        headval = self.head
        if headval is not None:
            self.head = headval.next
            headval = None
            return
        while headval is not None:
            if headval.data == remKey:
                break
            prev = headval
            headval = headval.next
        if(headval == None):
            return
        prev.next = headval.next
        headval = None

def testLinkedList():
    l1 =LinkedList()
    l1.head = Node('Mon')
    e1 = Node('Tue')
    e2 = Node('Wed')
    l1.head.next =e1
    e1.next = e2

    l1.addAtBegining('sun')
    l1.AddAtEnd('Fri')
    l1.insertNode(l1.head.next.next.next, 'Thr')
    l1.removeNode('Fri')
    l1.listprint()

def main():
    testLinkedList()

if __name__=='__main__':
    main()