from Node import Node


# Stack is FILO data structure supporting pop, push,
# and peek operations backed by linked list or array of nodes
class Stack:
    def __init__(self, limit=None):
        self.size = 0
        self.limit = limit
        self.head = None

    def push(self, value):
        if self.size == self.limit:
            print("Stack Overflow")
            return -1

        if self.size == 0:
            self.head = Node(value)
        else:
            new_node = Node(value, next_node=self.head)
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Stack Underflow")
            return None

        node_to_remove = self.head
        self.head = self.head.get_next_node()
        self.size -= 1
        return node_to_remove.get_value()

    def peek(self):
        return self.head

    def __str__(self):
        res = ""
        if self.size == 0:
            return "Empty Stack"
        current = self.head
        while current:
            if current.get_value() is not None:
                res += str(current.get_value()) + ", "
            current = current.get_next_node()
        return res


if __name__ == "__main__":
    test = Stack(4)
    print(test)
    test.push(1)
    test.push(2)
    test.push(3)
    print(test)
    test.push(4)
    test.push(5)
    print(test)
    print("removing", test.pop())
    print("removing", test.pop())
    print(test)
