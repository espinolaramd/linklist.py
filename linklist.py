#Diego Espinola
#02.19.20
#create a link list and add to the head.

class   Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None

class linked_list:

    def __init__(self):
        self.head = None


    def add_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node




