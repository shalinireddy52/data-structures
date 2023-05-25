class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 2:
            self._resize(self.capacity // 2)
        return value

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1
                return
        raise ValueError(f"Value {value} not found")

    def clear(self):
        self.array = [None] * self.capacity
        self.size = 0

    def display(self):
        return self.array[:self.size]
