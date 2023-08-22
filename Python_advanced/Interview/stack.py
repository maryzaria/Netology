class Stack:
    def __init__(self, data=None):
        if isinstance(data, (str, int, tuple, set, dict)):
            self.__stack = list(data)
        elif isinstance(data, list):
            self.__stack = data[:]
        else:
            self.__stack = []

    def isEmpty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.__stack[-1]
        return 'stack is empty'

    def size(self):
        return len(self.__stack)
