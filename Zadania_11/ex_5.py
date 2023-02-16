# Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card).
# Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond).
# W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii.
# W Deck znaleźć mają się takie metody jak: shuffle (która może wykorzystywać metodę o tej samej nazwie - shuffle - z biblioteki random)
# oraz deal (która będzie usuwała i zwracała ostatnią kartę z talii).
#
# Podpowiedź:
# Talia kart ma się składać z 52 różnych obiektów Card o wszystkich możliwych kombinacjach pól,
# np. (A - Diamond, A - Clubs itd).
# Aby utworzyć taką kombinację, utwórz dwie niezależne listy - w pierwszej przechowuj możliwe figury, a w drugiej wartości.
# Następnie przechodząc pętlami, łącz je ze sobą i twórz obiekty.
import random

class Card:
    def __init__(self, color: str, figure: str) -> None:
        self.color = color
        self.figure = figure

    def __str__(self):
        return f"Jestem kartą o wartośći {self.figure} i {self.color}"

    def __repr__(self):
        return f"Card({self.color}, {self.figure})"


class Deck:
    card_f: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_c: list[str] = ["Club", "Diamond", "Heart", "Spade"]

    def __init__(self):
        self.deck: list[Card] = Deck.create_deck()

    @staticmethod
    def create_deck() -> list[Card]:
        arr = []
        for colors in Deck.card_c:
            for figure in Deck.card_f:
                arr.append(Card(colors, figure))
        return arr

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def deal(self) -> Card:
        return self.deck.pop()

def main():
    card = Card('Heart', '3')
    print(card)
    all_cards = Deck()
    all_cards.shuffle()
    print(all_cards.deck)

if __name__ == "__main__":
    main()