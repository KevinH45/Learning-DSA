
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None, tail=None):
        
        # Keeping track of tail so we can have O(1) append
        self.head = head
        self.tail = tail

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        self.setTail()
        return
    
    def setTail(self):
        cur = self.head
        while cur:
            self.tail = cur
            cur = cur.next
        return
    
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print()
