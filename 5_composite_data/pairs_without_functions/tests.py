import unittest
import pairs

class TestPairs(unittest.TestCase):

    values = [
        [pairs.cons(0, 0), 1],
        [pairs.cons(1, 2), 18],
        [pairs.cons(2, 1), 12],
        [pairs.cons(5, 8), 209952],
    ]

    cars = [
        [pairs.cons(0, 0), 0],
        [pairs.cons(1, 2), 1],
        [pairs.cons(2, 1), 2],
        [pairs.cons(5, 8), 5],
    ]

    cdrs = [
        [pairs.cons(0, 0), 0],
        [pairs.cons(1, 2), 2],
        [pairs.cons(2, 1), 1],
        [pairs.cons(5, 8), 8],
    ]

    def test_selectors(self):
        for exeptation, argument in self.values:
            self.assertEqual(exeptation, argument)
        for exeptation, argument in self.cars:
            self.assertEqual(pairs.car(exeptation), argument)
        for exeptation, argument in self.cdrs:
            self.assertEqual(pairs.cdr(exeptation), argument)
        print('test_selectors is Ok!')

    def test_pair_transit(self):
        pair = pairs.cons(0, 0)
        transit = pairs.cons(1, 1)
        self.assertEqual(pair, 1)
        self.assertEqual(pairs.car(pair), 0)
        self.assertEqual(pairs.cdr(pair), 0)
        self.assertEqual(pairs.car(transit), 1)
        self.assertEqual(pairs.cdr(transit), 1)
        print('test_pair_transit is ok!')

a = TestPairs()
a.test_selectors()
a.test_pair_transit()