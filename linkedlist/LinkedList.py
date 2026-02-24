class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNewNodeFront(self,value):
        new_node = Node(value)
        if(self.head == None):
            
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def addNewNodeEnd(self,value):
        new_node = Node(value)
        if(self.tail == None):
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def showLinkedList(self):
        p = self.head
        while p != None:
            print(f" ({p.value})")
            p = p.next
lista = LinkedList()

lista.addNewNodeFront(1)
lista.addNewNodeEnd(2)
lista.addNewNodeEnd(3)

lista.showLinkedList()

