import unittest
from chernovPz3 import calculator

class TestCalc(unittest.TestCase):
    def test_calc(self):
        a = 15
        b = 30
        should_ans = 40  # считаем руками, здесь намеренно ошибка
        res = calculator()
        self.assertEqual(res, should_ans)

if __name__ == '__main__':
    unittest.main()
