import unittest
from pz import calc

class TestCalc(unittest.TestCase):
    def test_calc_add_1(self):
        a = 999
        b = 1
        should_ans = 1000
        res = calc(a, b, '+')
        self.assertEqual(res, should_ans)

    def test_calc_add_2(self):
        a = 1
        b = 999
        should_ans = 1000
        res = calc(a, b, '+')
        self.assertEqual(res, should_ans)

    def test_calc_add_3(self):
        a = 5
        b = 5
        should_ans = 10
        res = calc(a, b, '+')
        self.assertEqual(res, should_ans)

    def test_calc_add_4(self):
        a = -225
        b = 300
        should_ans = 75
        res = calc(a, b, '+')
        self.assertEqual(res, should_ans)

    def test_calc_sub_1(self):
        a = 999
        b = 1
        should_ans = 998
        res = calc(a, b, '-')
        self.assertEqual(res, should_ans)

    def test_calc_sub_2(self):
        a = 1
        b = 999
        should_ans = -998
        res = calc(a, b, '-')
        self.assertEqual(res, should_ans)

    def test_calc_sub_3(self):
        a = 5
        b = 5
        should_ans = 0
        res = calc(a, b, '-')
        self.assertEqual(res, should_ans)

    def test_calc_sub_4(self):
        a = -5
        b = -5
        should_ans = 0
        res = calc(a, b, '-')
        self.assertEqual(res, should_ans)

    def test_calc_div_1(self):
        a = 333
        b = 3
        should_ans = 111
        res = calc(a, b, '/')
        self.assertEqual(res, should_ans)

    def test_calc_div_2(self):
        a = 3
        b = 333
        should_ans = 0
        res = calc(a, b, '/')
        self.assertEqual(res, should_ans)

    def test_calc_div_3(self):
        a = 25
        b = 25
        should_ans = 1
        res = calc(a, b, '/')
        self.assertEqual(res, should_ans)

    def test_calc_div_4(self):
        a = -666
        b = -6
        should_ans = 111
        res = calc(a, b, '/')
        self.assertEqual(res, should_ans)

    def test_calc_mult_1(self):
        a = 222
        b = 4
        should_ans = 888
        res = calc(a, b, '*')
        self.assertEqual(res, should_ans)

    def test_calc_mult_2(self):
        a = 4
        b = 222
        should_ans = 888
        res = calc(a, b, '*')
        self.assertEqual(res, should_ans)

    def test_calc_mult_3(self):
        a = 5
        b = 5
        should_ans = 25
        res = calc(a, b, '*')
        self.assertEqual(res, should_ans)

    def test_calc_mult_4(self):
        a = -5
        b = -5
        should_ans = 25
        res = calc(a, b, '*')
        self.assertEqual(res, should_ans)

if __name__ == '__main__':
    unittest.main()
