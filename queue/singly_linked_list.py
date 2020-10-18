class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        self.length += 1
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            self.length -= 1
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            self.length -= 1
            value = self.head.value
            self.head = self.head.next
            return value

    def remove_tail(self):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            self.length -= 1
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        else:
            self.length -= 1
            value = self.tail.value
            current = self.head
            while current:
                if current.next is self.tail:
                    self.tail = current
                current = current.next
            return value
