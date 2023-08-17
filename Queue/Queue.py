class Queue:
    def __init__(self, initial_capacity=2):
        self.queue = [None] * initial_capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = initial_capacity

    def enqueue(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 2:
            self._resize(self.capacity // 2)
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def _resize(self, new_capacity):
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.front = 0
        self.rear = self.size
        self.queue = new_queue
        self.capacity = new_capacity

    def clear(self):
        self.queue = [None] * self.capacity
        self.front = self.rear = self.size = 0

    def display(self):
        return [self.queue[(self.front + i) % self.capacity] for i in range(self.size)]
