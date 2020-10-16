import unittest

from triple import make, get1, get2, get3

class TestTriple(unittest.TestCase):

    def test_triple(self):
        triple = make(1, 2, 3)
        self.assertEqual(get1(triple), 1)
        self.assertEqual(get2(triple), 2)
        self.assertEqual(get3(triple), 3)
        print('test_triple is Ok!')

    def test_triple_in_triple(self):
        triple1 = make(1, 2, 3)
        triple2 = make(13, 22, triple1)
        self.assertEqual(get1(triple2), 13)
        self.assertEqual(get2(triple2), 22)
        self.assertEqual(get3(triple2), triple1)
        print('test_triple_in_triple is Ok!')

    def test_triple_string(self):
        triple = make("hello", 44, None)
        self.assertEqual(get1(triple), "hello")
        self.assertEqual(get2(triple), 44)
        self.assertEqual(get3(triple), None)
        print('test_triple_string is Ok!')

a = TestTriple()
a.test_triple()
a.test_triple_in_triple()
a.test_triple_string()