import unittest

import lord_of_the_rings.the_one_ring as the_ring


class MyTestCase(unittest.TestCase):
    def test_rule(self):
        actual_rule = the_ring.rule_them_all()
        self.assertEqual(False, actual_rule, "Unable to rule")

    def test_find(self):
        actual_find = the_ring.find_them()
        self.assertEqual(False, actual_find, "Unable to find")

    def test_bind(self):
        self.assertRaises(Exception, the_ring.bring_them_all_and_in_the_darkness_bind_them)


if __name__ == '__main__':
    unittest.main()
