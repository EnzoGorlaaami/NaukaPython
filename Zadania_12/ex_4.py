import datetime as dt



class NotesSubManager:
    def __init__(self):
        self.name = input("Twórca: ")
        self.date = dt.datetime.now()

class CardsSubManager:
    def __init__(self):
        self.cards = []

# class Manager(NotesSubManger, CardsSubManger)
# def __init__(self):
# self.menu = Menu()

class Card(SubManager):
    def __init__(self):
        super().__init__()
        self.phone_nr = int(input("Podaj Swój numer telefonu: "))
        self.mail_adr = input("Podaj Swój adres e-mail: ")

    def __str__(self):
        return f'Utworzono: {self.date}\n"{self.name}"\nTelefon: {self.phone_nr}\nAdres e-mail: {self.mail_adr}'
class Note(SubManager):
    def __init__(self):
        super().__init__()
        self.note = input("Podaj notatkę: ")

    def __str__(self):
        return f'Utworzono: {self.date}\nTwórca: {self.name}\n{self.note}'


class Menu:
    def __init__(self):
        self.menu = '1. Dodaj notatkę\n2. Dodaj wizytówkę (Card)\n3. Wyświetl wszystkie notatki\n4. Wyświetl wszystkie wizytówki\n5. Wyjdź'

    def wybory_menu(self, choice: int):
        while True:
            if choice == 5:
                print("Do następnego razu! ")
                break
            elif choice == 1:
                new_note = Note()
                self.note_list.append(new_note)
                print("\n")
            elif choice == 2:
                new_card = Card()
                self.cards_list.append(new_card)
                print("\n")
            elif choice == 3:
                for notes in self.note_list:
                    print(notes)
                print("\n")
            elif choice == 4:
                for cards in self.cards_list:
                    print(cards)
                print("\n")

    def __str__(self):
        return self.menu

class Manager(SubManager):

    def __init__(self):
        self.cards_list: list[Card] = []
        self.note_list: list[Note] = []
    def show_menu(self) -> str:
        print(self.menu)

    def execute(self) -> int:
        choice = 0
        while choice not in range(1,6):
            choice = int(input("Co robimy? :"))
            return choice


    def start(self) -> None:
        self.menu = Menu()
        self.execute()

def main():
    man = Manager()
    man.start()

if __name__ == '__main__':
    main()