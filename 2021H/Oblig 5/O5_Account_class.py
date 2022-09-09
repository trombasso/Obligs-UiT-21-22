class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annual_interest_rate = float(annual_interest_rate)

    @property
    def id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @property
    def annual_interest_rate(self):
        return self.__annual_interest_rate

    @id.setter
    def id(self, value):
        self.__id = value

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @annual_interest_rate.setter
    def annual_interest_rate(self, value):
        self.__annual_interest_rate = value

    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12

    def get_monthly_interest(self):
        return self.get_monthly_interest_rate() * (self.balance / 100)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value


def main():

    konto1 = Account(1122, 20000, 4.5)
    konto1.withdraw(2500)
    konto1.deposit(3000)
    print("ID", konto1.id, "\n")
    print("Balanse", konto1.balance, "\n")
    print("Renter", konto1.get_monthly_interest(), "\n")
    print("Månedlig R", konto1.get_monthly_interest_rate(), "\n")


if __name__ == "__main__":
    main()
