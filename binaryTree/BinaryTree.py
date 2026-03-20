
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Tree :
    def __init__(self):
        self.root = None
    
    def add(self,value,current = None):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        
        if current == None:
            current = self.root
        if current.value < value:
            if current.right != None:
                current = current.right
                self.add(value,current)
            else:
                current.right = new_node
                
        else:
            if current.left != None:
                current = current.left
                self.add(value,current)
            else:
                current.left = new_node
        
