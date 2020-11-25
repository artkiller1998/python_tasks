#!/usr/bin/python3
# это файл test_pz4.py
import unittest
from unittest.mock import patch
from ugad import Guesser

class TestGuesser(unittest.TestCase):
    def test_check(self):
        should_list=[]
        ans_list=[]
        rnd1 = 15
        with patch('random.randint', return_value=rnd1):
            guesser = Guesser()
        guess = 15
        should_ans = 0
        should_list.append(should_ans)
        ans_list.append(guesser.check(guess))

        rnd2 = 999999
        with patch('random.randint', return_value=rnd2):
            guesser = Guesser()
        guess = 15
        should_ans = -1
        should_list.append(should_ans)
        ans_list.append(guesser.check(guess))

        rnd3 = -999999
        with patch('random.randint', return_value=rnd3):
            guesser = Guesser()
        guess = 15
        should_ans = 1
        should_list.append(should_ans)
        ans_list.append(guesser.check(guess))

        for sh, an in zip(should_list, ans_list):
            self.assertEqual(an, sh)

    def test_play(self):
        rnd4=44
        with patch('random.randint', return_value=rnd4):
            guesser = Guesser()
        with patch('builtins.input', return_value=rnd4):
            guesser.play()