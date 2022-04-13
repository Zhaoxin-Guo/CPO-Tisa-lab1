import unittest
from hypothesis import given
from Mutable import *
import hypothesis.strategies as st
class TestMutableUnrolled_linked_list(unittest.TestCase):

    def test_size(self):
        lst = UnrolledLinkedList()
        self.assertEqual(lst.size(), 0)
        lst.set(0, 'a')
        self.assertEqual(lst.size(), 1)
        lst.set(1, 'b')
        self.assertEqual(lst.size(), 2)

    def test_from_list(self):
        # 每次测试都得初始化一遍，要不然上一次的结果还在
        lst = UnrolledLinkedList()
        lst.from_list([])
        self.assertEqual(lst.to_list(), [])
        lst = UnrolledLinkedList()
        lst.from_list(['a'])
        self.assertEqual(lst.to_list(), ['a'])
        lst = UnrolledLinkedList()
        lst.from_list(['a', 'b'])
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_to_list(self):
        lst = UnrolledLinkedList()
        self.assertEqual(UnrolledLinkedList().to_list(), [])
        lst.set(0, 'a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.set(1, 'b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_set(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.set(1, 'b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_get(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        lst.set(1, 'b')
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')

    def test_remove(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        lst.set(1, 'b')
        lst.set(2, 'c')
        lst.remove(2)
        self.assertEqual(lst.to_list(), ['a', 'b'])
        lst.remove(1)
        self.assertEqual(lst.to_list(), ['a'])
        lst.remove(0)
        self.assertEqual(lst.to_list(), [])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = UnrolledLinkedList()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)


    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = UnrolledLinkedList()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))