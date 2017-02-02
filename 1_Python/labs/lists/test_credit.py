import unittest
import credit


class TestCreditModule(unittest.TestCase):

    def test_good_card_number_is_valid(self):
        good_acct_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
        self.assertEqual(credit.validate(good_acct_num), 'Valid!')

    def test_bad_card_number_is_invalid(self):
        bad_acct_num = [4, 5, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
        self.assertEqual(credit.validate(bad_acct_num), 'Invalid!')


if __name__ == '__main__':
    unittest.main()
