# Stwórz klasę reprezentującą Prostokąt.
# Dodaj do niej metody obliczające pole i obwód z przechowywanych pól - szerokości i długości.

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def rectangle_area(self):
        rectangle_area = self.side_a * self.side_b
        print(f'Rectangle area of your rectangle is: {rectangle_area}m2. ')

    def rectangle_circuit(self):
        rectangle_circuit = (self.side_a + self.side_b) * 2
        print(f'Rectangle circiut of your rectangle is: {rectangle_circuit}m. ')

    @staticmethod
    def get_sides_of_rectangle():
        side_a = int(input("Enter first side of rectangle in meters: "))
        side_b = int(input("Enter second side of rectangle in meters: "))
        return side_a, side_b

def main():
    side_a, side_b = Rectangle.get_sides_of_rectangle()
    my_rectangle = Rectangle(side_a, side_b)
    my_rectangle.rectangle_circuit()
    my_rectangle.rectangle_area()


if __name__ == "__main__":
    main()