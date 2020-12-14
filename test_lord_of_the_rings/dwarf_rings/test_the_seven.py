import unittest

import lord_of_the_rings.dwarf_rings.the_seven as the_rings


class MyTestCase(unittest.TestCase):
    def test_rule(self):
        actual_rule = the_rings.rule()
        self.assertEqual(False, actual_rule, "Unable to rule")

    def test_find(self):
        actual_find = the_rings.find()
        self.assertEqual(False, actual_find, "Unable to find")


if __name__ == '__main__':
    unittest.main()
