import unittest
from atm_interface_solution import Account


class TestAccountCreation(unittest.TestCase):
    account = Account(200, 'checking')

    def test_initial_account_open(self):
        account = Account(210, 'checking')
        self.assertEqual(account.balance, 200)
        self.assertEqual(account.account_type, 'checking')
