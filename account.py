
class Account:

    def __init__(self, account_id, balance = 0):
        """
        :param account_id:
        :param balance: default balance is set to 0
        """
        self.id = account_id
        self.balance = balance

    def get_account_id(self):
        """
        :return: Account id : <class 'int'>
        """
        return self.id

    def get_balance(self):
        """
        :return: Account balance : <class 'int'>
        """
        return self.balance

    def deposit(self, amount):
        """
        :param amount: Amount to be deposited
        :return: <class 'NoneType'>
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        :param amount: Amount to be withdrawn
        :return: <class 'NoneType'>
        """
        self.balance -= amount





