
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # is there a left child
            if self.left: # same as self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else: # go right
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
                    