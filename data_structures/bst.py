
class Node:
    def __init__(self, data=None, right=None, left=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree:

    def __init__(self, root=Node()):
        self.root = root
    
    def insert(self, node):

        if not self.root:
            self.root = node
            return
        
        cur = self.root
        while cur:
            if node.data < cur.data:
                if not cur.left:
                    cur.left = node
                    node.parent = cur
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    node.parent = cur
                    return
                cur = cur.right

    def findMin(self, root="dummyValue"):
        if root == "dummyValue":
            root = self.root

        if not root:
            return None

        cur = root
        while cur.left:
            cur = cur.left

        return cur.data
    
    def findMax(self, root="dummyValue"):
        if root == "dummyValue":
            root = self.root
        
        if not root:
            return None

        cur = root
        while cur.right:
            cur = cur.right

        return cur.data

    def find(self, data):

        if not self.root:
            return None

        cur = self.root
        while cur:
            if cur.data == data:
                return cur
            elif cur.data < data:
                cur = cur.right
            else:
                cur = cur.left
        return None

    def delete(self, data):

        node = self.find(data) # Assuming no duplicates
        
        if not node:
            raise ValueError("Node not found")
        
        # If leaf
        if not node.left and not node.right:
            
            if node.data == self.root.data:
                self.root = None
            elif node.data <= node.parent.data:
                node.parent.left = None
            else:
                node.parent.right = None
            return
        
        # If has one child
        if not node.left or not node.right:

            if node.left:
                node.parent.right = node.left
            else:
                node.parent.right = node.right

            return
        
        # If has two children
        if node.left and node.right:
            minNode = self.findMin(root=node.right)

            node.data = minNode.data
            
            minNode.parent.left = minNode.right
