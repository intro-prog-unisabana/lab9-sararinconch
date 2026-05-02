class Person:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        numerocuentas = len(self.accounts)
        return f"Name = {self.name}, Number of accounts = {numerocuentas}"


        