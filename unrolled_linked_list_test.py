import unittest

from unrolled_linked_list import UnrolledLinkedList


class unrolled_linked_list_test(unittest.TestCase):
    def test_default_node_capacity(self):
        l = UnrolledLinkedList()
        self.assertEqual(l.max_node_capacity, 4)

    def test_custom_node_capacity(self):
        l = UnrolledLinkedList(4)
        self.assertEqual(l.max_node_capacity, 4)

        l = UnrolledLinkedList(15)
        self.assertEqual(l.max_node_capacity, 15)

    def test_empty(self):
        l = UnrolledLinkedList()
        self.assertEqual(str(l), "{}")
        l.append(1)
        del l[0]
        self.assertEqual(str(l), "{}")

    def test_delete_item(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        del l[1]
        self.assertEqual(str(l), '{[1, 3]}')

    def test_get_item(self):
        l = UnrolledLinkedList()
        l.append(2)
        l.append(3)
        self.assertEqual(l.__getitem__(1), 3)
        self.assertEqual(str(l[0]), '2')

    def test_set_item(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l[1] = 42
        self.assertEqual(str(l[1]), '42')

    def test_iteration(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        arr = []
        for i in l:
            arr.append(i)

        self.assertEqual(arr[0], l[0])
        self.assertEqual(arr[1], l[1])
        self.assertEqual(arr[2], l[2])

    def test_len(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(str(len(l)), '3')

        l.append(4)

        self.assertEqual(str(len(l)), '4')

    def test_reverse(self):
        testL = [3, 2, 1]
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        newL = []

        for x in reversed(l):
            newL.append(x)
        self.assertEqual(newL, testL)

    def test_contains(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(1 in l, True)
        self.assertEqual(42 in l, False)

    def test_node_variable(self):
        l = UnrolledLinkedList()
        l.append(1)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(1)
        l.append(7)
        l.append(8)
        self.assertEqual(str(l), '{[1, 3], [4, 5], [1, 7, 8]}')
