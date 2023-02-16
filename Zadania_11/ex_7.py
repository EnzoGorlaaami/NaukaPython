# Utworzyć klasy Notatka (Note) i Notatnik (Notebook).
# Klas notatki przechowuje autora, treść i czas utworzenia (autor i treść są podawane jako argumenty konstruktora,
# a czas jest pobierany i zapisywany przy tworzeniu obiektu).

# Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów,
# lecz tworzy pustą listę do której będą dodawane obiekty klasy Notatka.
# Klasa Notatnika musi posiadać implementacje metod, pozwalających:
# dodać nową notatkę, dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki.
# Dodatkowo musi być obsłużona sytuacja kiedy notatnik jest pusty.

import datetime

class Note:

    def __init__(self, writer: str, note: str) -> None:
        self.writer = writer
        self.note = note
        self.date: datetime = datetime.datetime.now()

    def __str__(self) -> str:
        return f"{self.date}\n{self.writer}:\n{self.note}"

class Notebook:

    def __init__(self) -> None:
        self.note_list: list[Note] = []


    def new_note(self) -> None:
        writer: str = input('Introduce Writer of Note: ')
        note: str = input('Set note: ')
        self.note_list.append(Note(writer, note))

    def add_note(self, note: Note) -> None:
        self.note_list.append(note)
    #
    # def number_of_notes(self):
    #     return len(self.note_list)

    def __len__(self) -> int:
        return len(self.note_list)

    def show_notes(self) -> None:
        if len(self) == 0:
            print(f"There's no notes in Notebook!")
        else:
            for note in self.note_list:
                print(note)

def menu():
    notes = Notebook()
    while True:
        menu: str = 'Menu:\n1: Create note \ 2: Add note \ 3: Number of notes \ 4: Show notes \ 5: Exit'
        print(menu)
        user_input = int(input('What You want to do?: '))
        if user_input == 1:
            notes.new_note()
        elif user_input == 2:
            notes.add_note()
        elif user_input == 3:
            print(f'In Notebook is {len(notes)} notes. ')
        elif user_input == 4:
             notes.show_notes()
        elif user_input == 5:
            print('See You next time! ')
            break
        else:
            print('Wrong choice! ')

def main():
    print('Welcome in Notebook! ')
    menu()

if __name__ == "__main__":
    main()