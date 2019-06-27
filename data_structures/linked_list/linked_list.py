class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node

    def insert_tail(self, data):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data)

    def pop_head(self):
        if self.empty():
            return None
        tmp = self.head.data
        self.head = self.head.next
        return tmp

    def pop_tail(self):
        if self.empty():
            return None
        tmp = self.head
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next
                tmp.next, temp = None, tmp.next
        return tmp.data

    def empty(self):
        return self.head is None

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


if __name__ == '__main__':
    A = LinkedList()
    print("Inserting 1st at Head")
    A.insert_head(20)
    print("Inserting 2nd at Head")
    A.insert_head(10)
    print("Print List : ")
    A.print()
    print("\nInserting 1st at Tail")
    A.insert_tail(30)
    print("Inserting 2nd at Tail")
    A.insert_tail(40)
    print("Print List : ")
    A.print()
    print("\nDelete Head")
    A.pop_head()
    print("Delete Tail")
    A.pop_tail()
    print("Print List : ")
    A.print()
    print("\nReverse Linked List")
    A.reverse()
    print("Print List : ")
    A.print()
