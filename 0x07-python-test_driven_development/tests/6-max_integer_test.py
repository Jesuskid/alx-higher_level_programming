#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_float_numbers(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            501, 502, 503, 504, 505, 506, 507, 508, 509, 510,
            611, 612, 613, 614, 615, 616, 617, 618, 619, 620,
            719, 718, 717, 900, 715, 714, 713, 712, 711, 710]), 900)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer("1")

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
