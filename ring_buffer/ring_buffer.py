class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.length = 0
        self.tail = None # may delete
        self.oldest = None

    def append(self, item):
        node = Node(item)
        # if not capacity
        if self.head is None and self.tail is None and self.capacity > self.length:  #or self.tail is None: #may delete tail
            self.length += 1
            self.head = node
            self.tail = node
            self.oldest = node
        elif self.head and self.tail and self.capacity > self.length:
            self.length += 1
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.oldest = self.head #REDUNDANT CAN DELETE AFTER TESTING
        # if capacity
        elif self.head and self.tail and self.capacity == self.length:
            # breakpoint()
            if self.oldest == self.head:
                self.head.next.prev = node
                node.next = self.head.next
                self.head = node
                self.oldest = self.head.next
            elif self.oldest != self.tail:
                self.oldest.prev.next = node
                self.oldest.next.prev = node
                node.next = self.oldest.next
                node.prev = self.oldest.prev
                self.oldest = node.next
            else: #when oldest = tail
                self.tail.prev.next = node
                node.prev = self.tail.prev
                self.tail = node
                # self.oldest = self.tail #just changed!!!
                self.oldest = self.head

            
            # node.next = self.oldest.next
            # self.oldest = self.oldest.next
            # self.head = node
        else: #todo: catch edge cases here
            pass
            



    def get(self):
        # TODO: edge case if ring buffer is empty
        val = []  
        vals = []  
        current_node = self.head
        if self.head is not None:
            print('h: ', self.head.value)
            print('o: ', self.oldest.value)
            print('t: ', self.tail.value)
            # print()
        while current_node is not None:
            # print('hello')
            vals.append('a')
            val.append(current_node.value)
            current_node = current_node.next
        return val
        






class Node:
    def __init__(self, value, next=None, prev = None):
        self.value = value 
        self.next = next
        self.prev = prev

    # method to get the value of the node 
    def get_value(self):
        return self.value
        
    # method to get the node's `next`
    def get_next(self):
        return self.next
        
    # method to update the node's `next` to the input node 
    def set_next(self, new_next):
        self.next = new_next



# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# print(buffer.get())   
# print()
# buffer.append('b')
# print(buffer.get())   
# print()

# buffer.append('c')
# print(buffer.get())   # should return ['a', 'b', 'c']
# print()

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')
# print(buffer.get())   # should return ['d', 'b', 'c']
# print()

# buffer.append('e')
# print(buffer.get())   # should return ['d', 'b', 'c']
# print()

# buffer.append('f')
# print(buffer.get())   # should return ['d', 'e', 'f']

# """
# buffer = RingBuffer(5)
# for i in range(6):
#     buffer.append(i)
# print(buffer.get())

# buffer = RingBuffer(5)
# for i in range(7):
#     buffer.append(i)
# print(buffer.get())

# buffer = RingBuffer(5)
# for i in range(8):
#     buffer.append(i)
# print(buffer.get())

# buffer = RingBuffer(5)
# for i in range(9):
#     buffer.append(i)
# print(buffer.get())
# # breakpoint()
# """