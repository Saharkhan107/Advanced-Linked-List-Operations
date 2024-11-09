# linkedlist.py

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = new_node

    def traverse(self):
        probe = self.head
        while probe:
            print(probe.data, end=" -> ")
            probe = probe.next
        print("None")

    def search(self, target):
        probe = self.head
        while probe:
            if probe.data == target:
                return True
            probe = probe.next
        return False

    def delete_at_position(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
        else:
            probe = self.head
            for _ in range(index - 1):
                if not probe or not probe.next:
                    print("Error: Index out of bounds")
                    return
                probe = probe.next
            if probe and probe.next:
                probe.next = probe.next.next

# Testing
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.traverse()  
    print(ll.search(20))  
    print(ll.search(40))  
    ll.delete_at_position(1)
    ll.traverse()  

