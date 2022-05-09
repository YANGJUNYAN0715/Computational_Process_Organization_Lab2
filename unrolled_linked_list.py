class Node():
    def __init__(self):
        self.arr = []
        self.next = None


class UnrolledLinkedList():
    def __init__(self, max_node_capacity=4):
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self.head = None
        self.tail = None

    def __delitem__(self, index):
        if index < 0:
            absIndex = self.length + index
        else:
            absIndex = index

        if index > self.length - 1:
            raise IndexError(str(index) + ' out of range. ')
        elif absIndex < 0:
            raise IndexError(str(index) + ' out of range. ')

        currentNode = self.head
        currentIndex = 0

        while len(currentNode.arr) - 1 + currentIndex < absIndex:
            currentIndex = currentIndex + len(currentNode.arr)
            currentNode = currentNode.next

        arrIndex = absIndex - currentIndex
        del currentNode.arr[arrIndex]
        self.length = self.length - 1

        nextNode = currentNode.next
        while nextNode:
            if len(currentNode.arr) < self.max_node_capacity // 2 \
                    and nextNode is not None:
                numberToTransfer = self.max_node_capacity // 2 \
                                   - len(currentNode.arr) + 1
                currentNode.arr = (currentNode.arr +
                                   nextNode.arr[:numberToTransfer])
                nextNode.arr = nextNode.arr[numberToTransfer:]

                if len(nextNode.arr) < self.max_node_capacity // 2:
                    currentNode.arr = currentNode.arr + nextNode.arr
                    currentNode.next = nextNode.next
                    del nextNode
            currentNode = currentNode.next
            if currentNode:
                nextNode = currentNode.next
            else:
                nextNode = None

    def __getitem__(self, index):
        if index < 0:
            absIndex = self.length + index
        else:
            absIndex = index

        if index > self.length - 1:
            raise IndexError(str(index) + 'out of range.')
        elif absIndex < 0:
            raise IndexError(str(absIndex) + 'out of range.')

        currentNode = self.head
        currentIndex = 0

        while len(currentNode.arr) - 1 + currentIndex < absIndex:
            currentIndex = currentIndex + len(currentNode.arr)
            currentNode = currentNode.next

        arrIndex = absIndex - currentIndex
        return currentNode.arr[arrIndex]

    def __setitem__(self, key, value):
        index = key
        if index < 0:
            absIndex = self.length + index
        else:
            absIndex = index

        if index > self.length - 1:  # Over the max
            raise IndexError(str(index) + ' out of range.')
        elif absIndex < 0:  # Below 0
            raise IndexError(str(index) + 'out of range.')

        currentNode = self.head
        currentIndex = 0
        while len(currentNode.arr) - 1 + currentIndex < absIndex:
            currentIndex = currentIndex + len(currentNode.arr)
            currentNode = currentNode.next

        arrIndex = absIndex - currentIndex
        currentNode.arr[arrIndex] = value

    def __iter__(self):
        current = self.head
        while current is not None:
            for x in current.arr:
                yield x
            current = current.next

    def __str__(self):
        if self.length == 0:
            return '{}'

        result = '{'
        current = self.head
        while current is not None:
            result = result + '['
            for i in range(0, len(current.arr)):
                result = result + str(current.arr[i])
                if i < len(current.arr) - 1:
                    result = result + ', '
            result = result + ']'
            if current.next is not None:
                result = result + ', '
            current = current.next
        result = result + '}'
        return result

    def __len__(self):
        return self.length

    def __reversed__(self):
        i = self.length - 1
        while i >= 0:
            yield self[i]
            i = i - 1

    def member(self, obj):
        for i in self:
            if i == obj:
                return True
        return False

    def to_list(self):
        res = []
        if self.head is None:
            return res
        else:
            for i in self:
                res.append(i)
            return res

    def from_list(self, a):
        L = self.empty()
        for e in a:
            L.cons(e)
        return L

    def cons(self, data):
        L = UnrolledLinkedList()
        L = L.concat(self)
        if L.head is None:
            L.head = Node()
            L.head.arr.append(data)
            L.tail = L.head
        elif len(L.tail.arr) < L.max_node_capacity:
            L.tail.arr.append(data)
        else:
            newNode = Node()
            middle = len(L.tail.arr) // 2
            newNode.arr = L.tail.arr[middle * -1:]
            L.tail.arr = L.tail.arr[:middle * -1]
            L.tail.next = newNode
            L.tail = newNode
            L.tail.arr.append(data)
        L.length = L.length + 1
        return L

    def filter(self, function):
        L = UnrolledLinkedList()
        for i in self:
            if function(i):
                L.cons(i)
        self = L
        return self

    def concat(self, other):
        temp = []
        if len(self.to_list()) == 0:
            return other
        if len(other.to_list()) == 0:
            return self

        temp += self.to_list()
        temp += other.to_list()
        temp.sort()
        res = self.from_list(temp)
        self = res
        return self

    def empty(self):
        L = UnrolledLinkedList()
        return L

    def reduce(self, function, initial_state):
        state = initial_state
        currentNode = self.head
        while currentNode is not None:
            state = function(state, currentNode.arr)
            currentNode = currentNode.next
        return state
