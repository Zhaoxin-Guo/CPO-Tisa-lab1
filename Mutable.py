class Node:
    def __init__(self, capacity=4):
        self.next = None
        self.numElements = 0  # The number of elements in the node
        self.elements = [None] * capacity
        self.cap = capacity  # Node capacity


class UnrolledLinkedList:
    def __init__(self):
        self.total_size = 0  # The total number of elements
        self.head, self.tail = Node(-1), Node(-1)  # Sentinel node
        node = Node()
        self.head.next = node
        node.next = self.tail

    def __str__(self):
        """for str() implementation for printing"""
        return " : ".join(map(str, self.to_list()))

    def __iter__(self):
        return self

    def __next__(self):
        if self.head.numElements == 0:
            raise StopIteration
        else:
            count = self.head.next.numElements
            while count is not 0:
                for i in range(0, self.head.next.numElements):
                    count = count - 1
                    tmp = self.head.next.elements[i]
                    return tmp
            self.head = self.head.next

    def size(self):
        return self.total_size

    def from_list(self, lst):
        if len(lst) == 0:
            self.head.next = None
            return
        cur = self.head.next
        for e in reversed(lst):
            self.set(0, e)

    def to_list(self):
        res = []
        cur = self.head.next
        while cur is not None:
            for i in range(0, cur.numElements):
                res.append(cur.elements[i])
            cur = cur.next
        return res

    def set(self, idx, obj):
        if idx < 0 or idx > self.total_size:
            return

        # Find the insertion node and position
        cur = self.head.next
        while idx >= cur.numElements:
            if idx == cur.numElements:
                break
            idx -= cur.numElements
            cur = cur.next

        if cur.numElements == cur.cap:
            # If the insert node is full, create a new node
            node = Node()
            next = cur.next
            cur.next = node
            node.next = next

            # Move the element of the inserted node to the new node
            move_idx = cur.numElements // 2
            for i in range(move_idx, cur.numElements):
                node.elements[i - move_idx] = cur.elements[i]
                cur.elements[i] = None
                cur.numElements -= 1
                node.numElements += 1

            # Update the insert position
            if idx >= move_idx:
                idx -= move_idx
                cur = node

        # Insert element
        for i in range(cur.numElements - 1, idx - 1, -1):
            cur.elements[i + 1] = cur.elements[i]
        cur.elements[idx] = obj

        cur.numElements += 1
        self.total_size += 1

    def remove(self, idx):
        if idx < 0 or idx >= self.total_size:
            return

        # Find the node and position of the removed element
        cur = self.head.next
        while idx >= cur.numElements - 1:
            if idx == cur.numElements - 1:
                break
            idx -= cur.numElements
            cur = cur.next

        # Delete element
        for i in range(idx, cur.numElements - 1, 1):
            cur.elements[i] = cur.elements[i + 1]
        cur.elements[cur.numElements - 1] = None
        cur.numElements -= 1

        if cur.next.cap != -1 \
                and cur.cap >= cur.numElements + cur.next.numElements:
            # Merge the next node to the current node
            next = cur.next
            for i in range(0, next.numElements):
                cur.elements[cur.numElements + i] = next.elements[i]
            cur.numElements += next.numElements
            cur.next = next.next

        self.total_size -= 1

    def get(self, idx):
        if idx < 0 or idx >= self.total_size:
            return None

        cur = self.head.next
        while idx >= cur.numElements:
            idx -= cur.numElements
            cur = cur.next
        return cur.elements[idx]

    def is_member(self, member):
        cur = self.head.next
        count = 0
        while cur is not None:
            for i in range(0, cur.numElements):
                count = count + 1
                if member == cur.elements[i]:
                    index = count - 1
                    return index
            return -1

    def filter(self, f):
        cur = self.head.next
        for i in range(0, cur.numElements):
            cur.elements[i] = f(cur.elements[i])
        return self.to_list()

    def map(self, f):
        cur = self.head.next
        while cur is not None:
            for i in range(0, cur.numElements):
                cur.elements[i] = f(cur.elements[i])
            cur = cur.next

    def reduce(self, f, initial_state):
        state = initial_state
        cur = self.head.next
        while cur is not None:
            for i in range(0, cur.numElements):
                state = f(state, cur.elements[i])
            cur = cur.next
        return state
