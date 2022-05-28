import unittest

from unrolled_linked_list import UnrolledLinkedList, cons


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 == 1


def _sum(state, x: list):
    for i in range(len(x)):
        state += x[i]
    return state


def add_one(x):
    return x + 1


def mul_two(x):
    return x * 2


class TestUnrolledLinkedList(unittest.TestCase):
    def test_api(self):
        empty = UnrolledLinkedList()
        l1 = cons(cons(empty, None), 1)
        l2 = cons(cons(empty, 1), None)
        l3 = cons(cons(empty, 1), 2)
        l4 = cons(cons(empty, 2), 1)
        self.assertEqual(str(empty), "{}")
        self.assertEqual(str(l1), "{[None, 1]}")
        self.assertEqual(str(l2), "{[1, None]}")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(str(l1), str(cons(cons(empty, None), 1)))
        self.assertEqual(len(empty), 0)
        self.assertEqual(len(l1), 2)
        self.assertEqual(len(l2), 2)
        self.assertEqual(str(l1.__delitem__(1)), "None")
        self.assertFalse(empty.member(None))
        self.assertTrue(l1.member(None))
        self.assertTrue(l2.member(1))
        self.assertFalse(l1.member(2))
        self.assertEqual(l3.to_list(), [1, 2])
        self.assertEqual(str(l3), str(l3.from_list([1, 2])))
        self.assertEqual(str(l3.concat(l4)), str(l3.from_list([1, 2, 2, 1])))
        self.assertEqual(str(l3.filter(is_even)), "{[2]}")
        self.assertEqual(str(l3.filter(is_odd)), "{[1]}")
        self.assertEqual(str(l3.map(add_one)), "{[2, 3]}")
        self.assertEqual(str(l3.map(mul_two)),"{[2, 4]}")

        buf = []
        for e in l3:
            buf.append(e)
        self.assertEqual(buf, [1, 2])

        lst = l3.to_list() + l4.to_list()
        for e in l3:
            lst.remove(e)
        for e in l4:
            lst.remove(e)
        self.assertEqual(lst, [])
