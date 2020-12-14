import unittest
from unittest.mock import patch

import lord_of_the_rings.mortal_men_rings.the_nine as the_rings
from lord_of_the_rings.mortal_men_rings import nazguls


class MyTestCase(unittest.TestCase):
    @patch.object(nazguls, 'rule', return_value=True)
    def test_rule(self, mock_nazguls):
        the_rings.rule()
        assert mock_nazguls.called

    @patch.object(nazguls, 'find', return_value=True)
    def test_rule(self, mock_nazguls):
        the_rings.find()
        assert mock_nazguls.called


if __name__ == '__main__':
    unittest.main()
