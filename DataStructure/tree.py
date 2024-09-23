
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.data is not None:
                    self.left.insert(data)
                else:
                    self.left.Node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)





def dataValue():
    root = Node(50)
    root.insert(20)
    root.insert(11)
    root.insert(15)
    root.insert(45)
    root.insert(30)
    root.insert(78)
    root.printTree()
def main():
    dataValue()

if __name__=='__main__':
    main()

