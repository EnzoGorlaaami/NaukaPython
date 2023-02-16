# Zad. 1
# Stwórz klasę reprezentującą studenta. Cechy studenta określaj z poziomu konstruktora. Dodaj do klasy metodę wyświetlającą informacje o danym obiekcie.



#Co to znaczy z poziomu konstruktora ?

class Student:
    def __init__(self, name, age, year_of_study):
        self.name = name
        self.age = age
        self.year_of_study = year_of_study

    def introduce(self):
        print(f'Hello, My name is {self.name}, I am {self.age} years old, '
              f'and this is my {self.year_of_study} year of study here. ')


def main():
    piotrek = Student("Piotr", 33, "second")
    piotrek.introduce()

if __name__ == "__main__":
    main()

