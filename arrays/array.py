class Array:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)

    def display(self):
        return self.array
