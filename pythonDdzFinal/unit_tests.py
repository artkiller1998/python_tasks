import unittest
import sys
from get_skills import form_map
from get_skills import print_map

class TestGetSkills(unittest.TestCase):
    def test_set_former(self):
        list_of_map = [{'key_skills': [{'name': 'Test1'}, {'name': 'Test2'}]}]
        res = form_map(list_of_map)
        exp = {'Test1': 1, 'Test2': 1}
        self.assertEqual(res, exp)

    def test_set_former_repeats(self):
        list_of_map = [{'key_skills':[{'name': 'Test First'},
                       {'name': 'Test Second'}, {'name': 'Test Third'}]}]
        res = form_map(list_of_map)
        exp = {'Test First': 3}
        self.assertEqual(res, exp)

    def test_print_noargs(self):
        map_ready = {'Element1': 1, 'Element2': 1}
        out_file = 'sys.stdout'
        print_map(map_ready, out_file)
        with self.assertRaises(FileNotFoundError):
            open(out_file).read()

    def test_print_args(self):
        map_ready = {'Element1': 1, 'Element2': 1}
        out_file = 'fileSetArgs.txt'
        print_map(map_ready, out_file)
        oppened_file = open(out_file)
        res = oppened_file.read()
        oppened_file.close()
        exp = "Skills for this vacancy:\n" \
              "('Element1', 1)\n" \
              "('Element2', 1)\n"
        self.assertEqual(res, exp)

if __name__ == '__main__':
    unittest.main()
