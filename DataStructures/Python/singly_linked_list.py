from Node import Node


# Represents a singly-linked list consisting of Nodes
# Supports operations like:
# Traversal: To traverse all the nodes one after another.
# Insertion: To add a node at the given position.
# Deletion: To delete a node.
# Searching: To search an element(s) by value.
# Updating: To update a node.
# Sorting: To arrange nodes in a linked list in a specific order.
# Merging: To merge two linked lists into one.
class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def set_head(self, new_head):
        self.head = new_head

    # Insets at the head of the list
    def insert_beginning(self, value):
        if self.get_head() is None:
            self.set_head(Node(value))
        else:
            new_node = Node(value, next_node=self.get_head())
            self.set_head(new_node)

    # Inserts after first node matching value
    def insert_after(self, where, value):
        current = self.get_head()
        while current:
            if current.get_value() == where:
                new_node = Node(value, next_node=current.get_next_node())
                current.set_next_node(new_node)
                return
            current = current.get_next_node()

    # Inserts before the first node matching value
    def insert_before(self, where, value):
        current = self.get_head()
        if current.get_value() == where:
            self.insert_beginning(value)
        else:
            while current.get_next_node():
                if current.get_next_node().get_value() == where:
                    new_node = Node(value, next_node=current.get_next_node())
                    current.set_next_node(new_node)
                current = current.get_next_node()

    # Removes the first occurrence of the node with specified value
    def remove_first_of_value(self, value):
        current = self.get_head()
        if current.get_value() == value:
            new_head = self.get_head().get_next_node()
            self.get_head().set_next_node(None)
            self.set_head(new_head)
        else:
            while current.get_next_node() and current.get_next_node().get_value():
                if current.get_next_node().get_value() == value:
                    the_node = current.get_next_node()
                    current.set_next_node(the_node.get_next_node())
                    the_node.set_next_node(None)
                current = current.get_next_node()

    def __str__(self):
        res = ""
        current = self.get_head()
        while current:
            if current.get_value() is not None:
                res += str(current.get_value()) + " "
            current = current.get_next_node()
        return res


if __name__ == "__main__":
    test = LinkedList()
    test.insert_beginning(5)
    test.insert_before(5, 9)
    test.insert_after(5, 62)
    print(test)
    test.remove_first_of_value(9)
    print(test)
