from Node import Node


# Doubly-linked list is a linked list with nodes containing both 'next' and 'previous' element pointers
# DLLs have head and tail properties
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def set_head(self, new_head):
        self.head = new_head

    def set_tail(self, new_tail):
        self.tail = new_tail

    def insert_head(self, value):
        new_node = Node(value, next_node=self.head)
        if self.head is not None:
            self.head.set_prev_node(new_node)
        else:
            self.set_tail(new_node)
        self.set_head(new_node)


    def insert_tail(self, value):
        new_node = Node(value, prev_node=self.get_tail())
        if self.get_tail() is not None:
            self.get_tail().set_next_node(new_node)
        else:
            # If the list is empty
            self.set_head(new_node)
        self.set_tail(new_node)


    def insert_after(self, where, value):
        pass

    def insert_before(self, where, value):
        pass

    def remove_first_occurrence(self, value):
        pass

    def __str__(self):
        res = ""
        current = self.get_head()
        while current:
            if current.get_value() is not None:
                res += str(current.get_value()) + ", "
            current = current.get_next_node()
        return res



if __name__ == "__main__":
    test = DoublyLinkedList()
    test.insert_tail(32)
    test.insert_tail(44)
    test.insert_head(101)
    print(test)
    print("Head", test.get_head().get_value())
    print("Tail", test.get_tail().get_value())
