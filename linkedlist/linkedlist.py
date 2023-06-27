class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        prev = None
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError(f"Value {value} not found")

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next
