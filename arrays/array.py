class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity  # initial size of the array
        self.size = 0  # the number of elements in the array
        self.array = [None] * self.capacity  # array is initially filled with None

    def _resize(self, new_capacity):
        """
        Resize the internal array to a new capacity.
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Resized array to new capacity: {self.capacity}")

    def append(self, value):
        """
        Add an element to the end of the array.
        If the array is full, resize it to double its current size.
        """
        if self.size == self.capacity:
            self._resize(self.capacity * 2)  # Double the size if the array is full

        self.array[self.size] = value
        self.size += 1

    def get(self, index):
        """
        Retrieve an element at a given index.
        """
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def remove(self, value):
        """
        Remove an element by value.
        """
        for i in range(self.size):
            if self.array[i] == value:
                # Shift all elements after the removed element to the left
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None  # Clear the last element
                self.size -= 1
                return
        raise ValueError(f"Value {value} not found in the array")

    def display(self):
        """
        Display the current elements in the array.
        """
        return self.array[:self.size]

# Example usage
if __name__ == "__main__":
    dynamic_array = DynamicArray()

    # Append elements
    dynamic_array.append(10)
    dynamic_array.append(20)
    dynamic_array.append(30)  # This will trigger a resize
    dynamic_array.append(40)
    print("Array after appends:", dynamic_array.display())

    # Get element at index 2
    print("Element at index 2:", dynamic_array.get(2))

    # Remove element by value
    dynamic_array.remove(20)
    print("Array after removing 20:", dynamic_array.display())

    # Try to access an out-of-bounds index
    try:
        print("Element at index 5:", dynamic_array.get(5))
    except IndexError as e:
        print(e)

    # Final array
    print("Final array:", dynamic_array.display())
