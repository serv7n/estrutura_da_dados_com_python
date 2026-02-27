class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self,value,current = None):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        
        if current == None:
            current = self.root
            # preciso ver em node esta se nao estiver em nenhum vai estar no raiz caso esteja em outro vai decer apartir dele
            # o current e a variavel que vai andar pela lista adicionando
      
      


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
    def show(self,current = None):
        if self.root == None:
            return None

        if current == None:
            current = self.root

        print(current.value)

        self._showLeft(current)
        self._showRight(current)
        
    def _showLeft(self,current):
        if current.left != None:
            current = current.left
            return self.show(current)
            
    def _showRight(self,current):
        if current.right != None:
            current = current.right
            return self.show(current)
        
t = Tree()
t.add(5)
t.add(3)
t.add(2)
t.add(6)
t.add(7)

t.show()