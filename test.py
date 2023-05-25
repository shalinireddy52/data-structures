from arrays.array import Array
from linkedlist.linkedlist import LinkedList
from stack.stack import Stack
from queue.queue import Queue

def test_data_structures():
    # Test Array
    arr = Array()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print("Array after appending 1, 2, 3:", arr.display())

    # Test Linked List
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Linked List:")
    ll.display()

    # Test Stack
    stack = Stack()
    stack.push(5)
    stack.push(10)
    print("Stack after pushing 5 and 10:", stack.peek())
    stack.pop()
    print("Stack after popping:", stack.peek())

    # Test Queue
    queue = Queue()
    queue.enqueue(15)
    queue.enqueue(20)
    print("Queue after enqueuing 15 and 20:", queue.peek())
    queue.dequeue()
    print("Queue after dequeuing:", queue.peek())

test_data_structures()
