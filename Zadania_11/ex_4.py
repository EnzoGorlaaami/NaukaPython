# Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak:
# numer_konta, nazwa właściciela konta, stan konta. OK

# Stwórz konstruktor odpowiednio uzupełniający pola. OK
# Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto. OK
# Dodaj założenie, że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł. OK

# Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta. OK
# Program ma wyświetlać odpowiedni komunikat, gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy OK
# (przykładowo z powodu braku wystarczającej ilości środków na koncie). OK

# Napisz metodę change_ownership(), która przyjmować będzie imię nowego właściciela konta i będzie aplikowała tę zmianę w obiekcie klasy. OK
# Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie. OK


class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self):
        amount = int(input('How many cash You wanna deposit on Your acount?: '))
        commission = amount // 100 * 2
        self.balance += amount - commission
        # while depo > 0:
        #     if depo >= 99:
        #         self.balance += 98
        #         depo -= 100
        #     else:
        #         self.balance += depo - 2
        #         break
        print(f'Your acount status is now {self.balance}$.')

    def withdraw(self):
        amount = int(input('How many cash You wanna get from Your acount?: '))
        if amount <= self.balance:
            self.balance -= amount
            print(f'Your acount status is now {self.balance}$.')
        else:
            print('Not enough funds in the account')

    def change_ownership(self):
        new_owner_name = input("Set a new name of account Owner: ")
        self.owner_name = new_owner_name
        print(f'Welcome {self.owner_name}!')


    def display(self):
        print(f'Welcome {self.owner_name}!\n'
              f'Your acount number is {self.account_number}, and status of this account is {self.balance}$.')

def main():
    piotr_acount = BankAccount(1234, "piotrek", 5000)
    print(piotr_acount)


if __name__ == "__main__":
    main()