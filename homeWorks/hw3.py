class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Добавить сумму: "))
        self._balance += amount
        print(f"Ваш новый баланс: {self._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Ваш баланс был умножен в 10 раз: {self._balance}")

    def _kill(self):
        self._balance = 0
        print(f"Ваш баланс был онулирован: {self._balance}")

    def _merge_balance(self, other):
        self._balance += other._balance
        print(f"После объедениния, ваш баланс: {self._balance}")

Account1 = Bank('Ruslan', 100)
Account2 = Bank('Beke',100)


Account1.moneyX()
Account1._Bank__jackpot()
Account1._kill()
Account1._merge_balance(Account2)