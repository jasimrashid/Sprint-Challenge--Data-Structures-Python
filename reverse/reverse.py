class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        ll_new = LinkedList()
        current_node = self.head
        while current_node is not None:
            ll_new.add_to_head(current_node.value)
            current_node = current_node.next_node
        self.head = ll_new.head



# Testing
# ll = LinkedList()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.add_to_head(4)
# ll.add_to_head(5)
# print(ll.head.value)
# ll.reverse_list(ll.head, None)
# print(ll.head.value)
# # breakpoint()

