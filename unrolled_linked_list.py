class Node():
    def __init__(self):
        self.arr = []
        self.next = None


class UnrolledLinkedList():
    def __init__(self, max_node_capacity=4):
        """
        Initialize

        :param max_node_capacity: the maximum number of elements
        in each element's array
        """
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self.head = None
        self.tail = None

    def __delitem__(self, index: int):
        """
        Delete an element by index

        :param index: the index of element which you want to delete
        :return:
        """
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

    def __getitem__(self, index: int) -> int:
        """
        Get an element by index

        :param index: the index of element which you want to get
        :return:
        """
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

    def __setitem__(self, key: int, value: int):
        """
        Set an element's value by key(index)

        :param key: the index of element which you want to set
        :param value: the value of element which you want to assign
        :return:
        """
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
        """
        Make the structure iterable

        :return:
        """
        current = self.head
        while current is not None:
            for x in current.arr:
                yield x
            current = current.next

    def __str__(self) -> int:
        """
        Return the description of the object in string

        :return:
        """
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

    def __len__(self) -> int:
        """
        Return the length of the structure

        :return:
        """
        return self.length

    def __reversed__(self):
        """
        Reverse the original structure

        :return:
        """
        i = self.length - 1
        while i >= 0:
            yield self[i]
            i = i - 1

    def member(self, obj) -> bool:
        """
        Check if the given object is a member of this structure

        :param obj: the object you want to check
        :return:
        """
        for i in self:
            if i == obj:
                return True
        return False

    def to_list(self) -> list:
        """
        Transfer an UnrolledLinkedList type object into a List type

        :return:
        """
        res = []
        if self.head is None:
            return res
        else:
            for i in self:
                res.append(i)
            return res

    def from_list(self, a: list):
        """
        Transfer a List type object into an UnrolledLinkedList type

        :param a: the list which you want
        transfer into UnrolledLinkedList
        :return:
        """
        L = self.empty()
        for i in a:
            if L.head is None:
                L.head = Node()
                L.head.arr.append(i)
                L.tail = L.head
            elif len(L.tail.arr) < L.max_node_capacity:
                L.tail.arr.append(i)
            else:
                newNode = Node()
                middle = len(L.tail.arr) // 2
                newNode.arr = L.tail.arr[middle * -1:]
                L.tail.arr = L.tail.arr[:middle * -1]
                L.tail.next = newNode
                L.tail = newNode
                L.tail.arr.append(i)
            L.length = L.length + 1
        return L

    def filter(self, function):
        """
        Filter data structure by specific predicate

        :param function: the function which you want to use
        as the filter function
        :return:
        """
        L = UnrolledLinkedList()
        for i in self:
            if function(i):
                L = cons(L, i)
        return L

    def map(self, function):
        """
        Map every element by a specific function and
        return an UnrolledLinkedList to contain these
        elements

        :param function: the function which you would like
        to map all the elements
        :return:
        """
        L = UnrolledLinkedList()
        for i in self:
            L = cons(L, function(i))
        return L

    def concat(self, other):
        """
        Concatenate two UnrolledLinkedLists into one UnrolledLinkedList

        :param other: another UnrolledLinkedList
        :return:
        """
        temp = []
        temp += self.to_list()
        temp += other.to_list()
        res = self.from_list(temp)
        return res

    def empty(self):
        """
        Return an empty UnrolledLinkedList

        :return:
        """
        L = UnrolledLinkedList()
        return L

    def reduce(self, function, initial_state):
        """
        Reduce process elements and build a value by the
        function

        :param function: the function which you want to use
        :param initial_state: the initial_state
        :return:
        """
        state = initial_state
        currentNode = self.head
        while currentNode is not None:
            state = function(state, currentNode.arr)
            currentNode = currentNode.next
        return state


def cons(L: UnrolledLinkedList, data: int):
    """
    Append a new element

    :param L: the UnrolledLinkedList which you would like to append an element
    :param data: the data which you want to append
    :return:
    """
    # use function of concat
    newL = UnrolledLinkedList()
    newL = newL.concat(L)
    if newL.head is None:
        newL.head = Node()
        newL.head.arr.append(data)
        newL.tail = newL.head
    elif len(newL.tail.arr) < newL.max_node_capacity:
        newL.tail.arr.append(data)
    else:
        newNode = Node()
        middle = len(newL.tail.arr) // 2
        newNode.arr = newL.tail.arr[middle * -1:]
        newL.tail.arr = newL.tail.arr[:middle * -1]
        newL.tail.next = newNode
        newL.tail = newNode
        newL.tail.arr.append(data)
    newL.length = newL.length + 1
    return newL
