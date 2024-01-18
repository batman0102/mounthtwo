class SavingAccount:
    pass

class CheckingAccount:
    pass

class Stock:
    pass

class Bond:
    pass

class RealEstate:
    pass

class BankAccount(SavingAccount, CheckingAccount):
    pass

class Security(Stock, Bond):
    pass

class InterestBearingItem(BankAccount, Security):
    pass

class Asset(BankAccount, RealEstate, Security):
    pass

class InsurableItem(RealEstate, BankAccount):
    pass

