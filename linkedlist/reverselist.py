class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def addNewNode(self,value):
        new_node = Node(value)
        if(self.head == None):
            
            self.head = new_node
        else:
            new_node.next = self.head
   
            self.head = new_node
    

    def showLinkedList(self):
        p = self.head
        
        while p != None:
            print(f" ({p.value})")
            p = p.prev
    
    def reverse(self):
        new_list = None
        # nova lista vira o ponteiro
        while self.head != None:
            nextx = self.head.next
        
            #  guardo o next do head pq o novo next vai ser a new list
            self.head.next = new_list 
            
            new_list = self.head
            # nova lista recebe o head
            self.head = nextx
            # agora o head e o next
        self.head = new_list
        # o nextx virou none e pra nao perder o head transformei ele no new_list

lista = LinkedList()

lista.addNewNode(1)
lista.addNewNode(2)
lista.addNewNode(3)
lista.addNewNode(4)

lista.reverse()
lista.showLinkedList()
# print(lista.head.value)
