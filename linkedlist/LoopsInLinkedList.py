#  oq aconteceu aqui?
# o fast pula duas casas sendo assim uma hora ou outra ele vai encontrar o slow 
# essa solucao apenas usa uma variavel a menos e e boa msm nao sendo 100% performantica
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def add(self,new_node):
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def hasCyclo(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            print(fast.value, slow.value)
            if(fast == slow):
                return True
        return False

lista = LinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node7 = Node(7)

lista.add(node1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node7
node7.next = node4
print(lista.hasCyclo())