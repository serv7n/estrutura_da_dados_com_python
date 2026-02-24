class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def add(self,value):
        new_node = Node(value)
        if(self.head == None):
            
            self.head = new_node
        else:
            new_node.next = self.head
   
            self.head = new_node

    def middle(self):
        fast = slow = self.head
        while fast and fast.next:
            # fast e o next existem entao posso continuar

            fast.next.next
            # fast pula duas vezes
            
            slow.next

        return slow
lista = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)

 
print(lista.middle().value)