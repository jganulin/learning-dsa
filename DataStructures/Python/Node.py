# Represents a node for use in a singly or doubly linked list
# Contains value, and pointers to previous and next nodes
class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_prev_node(self):
        return self.prev_node

    def get_next_node(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

