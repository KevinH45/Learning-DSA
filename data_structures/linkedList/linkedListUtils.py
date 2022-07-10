from linkedList import LinkedList

def reverseLinkedList(ls):

    cur = ls.head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    ls.head = prev
    ls.setTail()

    return ls
