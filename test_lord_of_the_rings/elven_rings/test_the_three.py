import unittest
from unittest.mock import patch

import lord_of_the_rings.elven_rings.the_three as the_rings
from lord_of_the_rings.elven_rings import narya, neya, vilya


class MyTestCase(unittest.TestCase):
    @patch.object(narya, 'rule', return_value=True)
    @patch.object(neya, 'rule', return_value=True)
    @patch.object(vilya, 'rule', return_value=True)
    def test_rule(self, mock_narya, mock_neya, mock_vilya):
        the_rings.rule()
        self.assertTrue(mock_narya.called)
        self.assertTrue(mock_neya.called)
        self.assertTrue(mock_vilya.called)

    @patch.object(narya, 'find', return_value=True)
    @patch.object(neya, 'find', return_value=True)
    @patch.object(vilya, 'find', return_value=True)
    def test_find(self, mock_narya, mock_neya, mock_vilya):
        the_rings.find()
        self.assertTrue(mock_narya.called)
        self.assertTrue(mock_neya.called)
        self.assertTrue(mock_vilya.called)


if __name__ == '__main__':
    unittest.main()
