class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty: cannot pop an empty stack")


class StackFullError(Exception):
    def __init__(self):
        super().__init__("Stack is full")


class stack():
    # ...

    def push(self, data):
        if self.isFull():
            raise StackFullError()
        self.data.append(data)
        return data

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError()
        item = self.data[len(self.data) -1]
        del self.data[len(self.data) -1]
        return item
        return len(self.items)