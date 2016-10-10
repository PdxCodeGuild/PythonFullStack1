import random

class Account(object):
    '''
    Bank Account Base Class
    '''
    _overdraft_fee = 35.0

    def __init__(self, balance, account_type, account_no=None):
        if account_no is None:
            self._account_no = self.gen_account_num()
        else:
            self.account_no = account_no

        self.balance = float(balance)
        self.account_type = account_type

    def __str__(self):
        return '{self.account_type} #{self._account_no!s} - ${self.balance!s}'.format(self=self)

    def __repr__(self):
        return '{self.__class__.__name__}({self.balance}, {self.account_type})'.format(self=self)

    @staticmethod
    def gen_account_num():
        gen_number = random.randint(100000000000000, 9999999999999999)
        return gen_number

    def get_funds(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdraw(self, amount):
        proposal = (self.balance - amount)
        return True if proposal >= 0 else False

    def withdraw(self, amount):
        if self.check_withdraw(amount) is True:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Not enough funds.")

    def calc_interest(self):
        interest = self.balance * 0.01
        total = self.balance * 1.01
        self.balance = total
        return self.balance

    def get_standing(self):
        return True if self.balance >= 1000 else False

    def make_record(self, filename='account.log'):
        with open(filename, 'w') as file:
            file.write('{self._account_no!s},{self.balance!s},{self.account_type}\n'.format(self=self))

    @classmethod
    def from_csv_string(Klass, record):
        record = record.split(',')
        account_no, balance, account_type = record[0], record[1], record[2]
        return Klass(balance, account_type, account_no=account_no)
