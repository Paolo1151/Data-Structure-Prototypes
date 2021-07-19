class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def set_next(self, next):
        self.next = next 

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, val):
        self.head = Node(val, self.head)
        self.size += 1

    def search(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.val is val:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, val):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.val is val:
                prev_node.next = current_node.next
                self.size -= 1
                break
            prev_node = current_node
            current_node = current_node.next
        return

    def size(self):
        return self.size


    