class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #langlah 1
        new = Node(data)

        #langkah 2
        if self.root == None:
            self.root = new
            return
        
        #langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q != None and new.data != P.data:
            #langkah 5
            P = Q

            #langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        #langkah 7
        if new.data == P.data:
            print("DATA SAMA")
            return
        
        #langkah 8
        if new.data < P.data:
            P.left = new
        else:
            P.right = new

        #selesai

bst = BinarySearchTree()
            
bst.insert(12)
bst.insert(32)
bst.insert(77)
bst.insert(5)
bst.insert(9)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

in_order(bst.root)



        