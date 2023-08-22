from stack import Stack


def balanced_sequence(data):
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    seq = Stack()
    if len(data) % 2:
        return False
    for item in data:
        if item in brackets:
            if seq.isEmpty() or brackets[item] != seq.pop():
                return False
        else:
            seq.push(item)
    return seq.isEmpty()


if __name__ == '__main__':
    print(balanced_sequence('[([])((([[[]]])))]{()}(){}'))


