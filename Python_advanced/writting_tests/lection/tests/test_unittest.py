import unittest
from unittest import TestCase

from ..main import summarize, get_list, get_dict, multiply


SOME_NUMBER = 30


class TestSummarize(TestCase):
    def test_with_2_nums(self):
        x = 10
        y = 15
        res = summarize(x, y)
        expected = 25
        self.assertEqual(res, expected)

    def test_with_2_negative_nums(self):
        x = -20
        y = -29
        res = summarize(x, y)
        expected = -45
        self.assertGreater(res, expected)

    def test_result_in_range(self):
        x = 10
        y = 25
        range1 = range(35, 50)
        res = summarize(x, y)
        self.assertIn(res, range1)

    def test_something(self):
        x, y = 19, 21
        res = summarize(x)
        expected = 40
        self.assertEqual(res, expected)

    @unittest.expectedFailure
    def test_failure_unittest(self):
        x, y = 19, 21
        res = summarize(x, y)
        self.assertFalse(res % 10 == 0)

    @unittest.skipIf(SOME_NUMBER < 25, 'Too big value')
    def test_smth(self):
        x, y = 20, 21
        res = multiply(x, y)
        expected = 420
        self.assertEqual(res, expected)


class TestEtc(TestCase):
    #regex
    def test_regex(self):
        pattern = '\d{2}-\d{2}-\d{4}'
        test_date1 = '25-06-2023'
        test_data2 = '28.09.2025'
        self.assertRegex(test_date1, pattern, 'Date is in wrong format')
        self.assertRegex(test_data2, pattern, 'Date is in wrong format')

    #количество элементов в списке? элементы должны быть равны, но могут быть в разном порядке
    def test_list_length(self):
        list1 = [4, 3, 2, 1]
        res = get_list()
        self.assertCountEqual(res, list1)

    #равенство словарей
    def test_dict(self):
        a = {'name': 'Ivan', 'city': 'Moscow', 'age': 29}
        res = get_dict()
        self.assertDictEqual(res, a)
