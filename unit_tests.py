import unittest
import sys
from exam import is_palindrome
from exam import get_most_frequent_value
from exam import is_prime
from exam import Human


class TestGetSkills(unittest.TestCase):

    def test_palindrom_1(self):
        in_str = "Шалаш"
        res = is_palindrome(in_str)
        exp = True
        self.assertEqual(res, exp)

    def test_palindrom_2(self):
        in_str = "А роза упала на лапу Азора"
        res = is_palindrome(in_str)
        exp = True
        self.assertEqual(res, exp)

    def test_palindrom_3(self):
        in_str = ""
        res = is_palindrome(in_str)
        exp = False
        self.assertEqual(res, exp)

    def test_palindrom_4(self):
        in_str = "Это не палиндром!"
        res = is_palindrome(in_str)
        exp = False
        self.assertEqual(res, exp)

    def test_most_frequent_value_1(self):
        max_val = 300
        list_of_val = [1,2,3,4,5,6,5,5,5,5,5]
        res = get_most_frequent_value(max_val,list_of_val)
        exp = 5
        self.assertEqual(res, exp)

    def test_most_frequent_value_2(self):
        max_val = 300
        list_of_val = [301,2,3,4,5,6,5,5,5,5,5]
        with self.assertRaises(ValueError) as e1:
            get_most_frequent_value(max_val, list_of_val)

    def test_is_prime_1(self):
        val = 7
        res = is_prime(val)
        exp = True
        self.assertEqual(res, exp)

    def test_is_prime_2(self):
        val = 8
        res = is_prime(val)
        exp = False
        self.assertEqual(res, exp)

    def test_is_prime_3(self):
        val = 'Not int'
        res = is_prime(val)
        self.assertRaises(TypeError)

    def test_human_1(self):
        exp_name = 'alex'
        exp_weight = 60
        exp_age = 20
        alex = Human(exp_name, exp_weight, exp_age)
        res_name = alex.name
        res_weight = alex.weight
        res_age = alex.age
        self.assertEqual(res_name, exp_name)
        self.assertEqual(res_age, exp_age)
        self.assertEqual(res_weight, exp_weight)

    def test_human_2(self):
        exp_name = 'alex'
        exp_weight = 60
        exp_age = 20
        alex = Human(exp_name, exp_weight, exp_age)
        alex.happy_birthday()
        res_age = alex.age
        self.assertEqual(res_age, exp_age+1)

    def test_human_3(self):
        exp_name = 'alex'
        new_exp_name = 'artem'
        exp_weight = 60
        exp_age = 20
        alex = Human(exp_name, exp_weight, exp_age)
        alex.change_name(new_exp_name)
        res_name = alex.name
        self.assertEqual(res_name, new_exp_name)

    def test_human_4(self):
        exp_name = 'alex'
        new_exp_weight = 360
        exp_weight = 60
        exp_age = 20
        alex = Human(exp_name, exp_weight, exp_age)
        alex.add_weight(300)
        res_weight = alex.weight
        self.assertEqual(res_weight, new_exp_weight)

    def test_human_5(self):
        exp_name = 'alex'
        new_exp_weight = 0
        exp_weight = 60
        exp_age = 20
        alex = Human(exp_name, exp_weight, exp_age)
        alex.add_weight(-300)
        res_weight = alex.weight
        self.assertEqual(res_weight, new_exp_weight)

    def test_human_6(self):
        exp_name = 'alex'
        exp_weight = 60
        exp_age = -20
        new_exp_age = 0
        alex = Human(exp_name, exp_weight, exp_age)
        res_age = alex.age
        self.assertEqual(res_age, new_exp_age)
