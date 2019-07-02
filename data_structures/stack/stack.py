class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty stack')
        else:
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]


if __name__ == '__main__':
    stack = Stack()

    for i in range(10):
        stack.push(i)

    assert stack.top() == 9

    for i in range(10):
        assert stack.pop() == (9 - i)
