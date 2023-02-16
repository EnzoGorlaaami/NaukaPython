# Stwórz klasę Shape i jej podklasę Square. Square ma posiadać konstruktor, który przyjmie length jako argument.
# Obie klasy mają posiadać metodę obliczającą pole figury. Domyślnie Shape ma zwracać wartość 0.
# klasa abstrakcyjna

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_circuit(self):
        return 0

    @abstractmethod
    def calculate_field(self):
        return 0


class Square(Shape):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def calculate_field(self) -> int:
        return self.a * self.b

    def calculate_circuit(self):
        return (self.a + self.b) * 2


def main():
    square = Square(2, 2)

if __name__ == '__main__':
    main()