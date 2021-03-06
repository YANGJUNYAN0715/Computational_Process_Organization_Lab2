import unittest

import hypothesis.strategies as st
from hypothesis import given, settings

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
    """
    add one to x

    :param x:
    :return:
    """
    return x + 1


def mul_two(x):
    """
    multiply two with x

    :param x:
    :return:
    """
    return x * 2


class TestUnrolledLinkedList(unittest.TestCase):
    def test_api(self) -> None:
        empty = UnrolledLinkedList()
        l1 = cons(cons(empty, 3), 1)
        l2 = cons(cons(empty, 1), 3)
        l3 = cons(cons(empty, 1), 2)
        l4 = cons(cons(empty, 2), 1)
        self.assertEqual(str(empty), "{}")
        self.assertEqual(str(l1), "{[3, 1]}")
        self.assertEqual(str(l2), "{[1, 3]}")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(str(l1), str(cons(cons(empty, 3), 1)))
        self.assertEqual(len(empty), 0)
        self.assertEqual(len(l1), 2)
        self.assertEqual(len(l2), 2)
        self.assertFalse(empty.member(None))
        self.assertTrue(l1.member(1))
        self.assertTrue(l2.member(1))
        self.assertFalse(l1.member(2))
        self.assertEqual(l3.to_list(), [1, 2])
        self.assertEqual(str(l3), str(l3.from_list([1, 2])))
        self.assertEqual(str(l3.concat(l4)), str(l3.from_list([1, 2, 2, 1])))
        self.assertEqual(str(l3.filter(is_even)), "{[2]}")
        self.assertEqual(str(l3.filter(is_odd)), "{[1]}")
        self.assertEqual(str(l3.map(add_one)), "{[2, 3]}")
        self.assertEqual(str(l3.map(mul_two)), "{[2, 4]}")

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


class unrolled_linked_list_test(unittest.TestCase):
    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers())
    def test_PBT(self, a, b):
        empty = UnrolledLinkedList()
        l1 = cons(cons(empty, a), b)
        l2 = cons(cons(empty, b), a)
        l3 = cons(cons(empty, None), a)
        self.assertEqual(str(empty), "{}")
        self.assertEqual(str(l1), "{[%d, %d]}" % (a, b))
        self.assertEqual(str(l2), "{[%d, %d]}" % (b, a))
        self.assertEqual(str(l3), "{[None, %d]}" % a)
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(str(l1), str(cons(cons(empty, a), b)))
        self.assertEqual(str(l3), str(cons(cons(empty, None), a)))
        self.assertEqual(len(empty), 0)
        self.assertEqual(len(l1), 2)
        self.assertEqual(len(l2), 2)
        self.assertFalse(empty.member(None))
        self.assertTrue(l3.member(None))
        self.assertTrue(l2.member(a))
        self.assertTrue(l1.member(b))
        self.assertEqual(l1.to_list(), [a, b])
        self.assertEqual(str(l1), str(l1.from_list([a, b])))
        self.assertEqual(str(l1.concat(l2)), str(l1.from_list([a, b, b, a])))
        self.assertEqual(str(l1.map(add_one)), "{[%d, %d]}" % (a + 1, b + 1))
        self.assertEqual(str(l1.map(mul_two)), "{[%d, %d]}" % (a * 2, b * 2))
        self.assertEqual(str(l3.__delitem__(1)), "None")
