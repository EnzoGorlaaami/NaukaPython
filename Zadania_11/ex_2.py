# Stwórz klasę reprezentującą pojazd.
# Dodaj do niej pola określające maksymalną prędkość obiektu oraz jego przebieg.
# Dodaj do klasy metodę, która zwiększać będzie wartość pola przebiegu o przesłaną wartość typu float.

class Vehicle:
    def __init__(self, max_speed_, mileage):
        self.max_speed = max_speed_
        self.mileage = mileage
        #self.next_mileage = next_mileage

    def mileage_increase(self, new_mileage):
        self.mileage += new_mileage
        print(f' Max speed of Your car is {self.max_speed}km\h, and previous mileage was {self.mileage}km. '
              f'Now, mileage is increased for {new_mileage}km. ')
    #
    # def next_mileage_cytrus(self):
    #     next_mileage_cytrus = float(input(f' Enter how many kilometers you have driven since the last time,'
    #                                       f' in thousands of kilometers, to three decimal places: '))
    #     return next_mileage_cytrus

def main():
    cytrus = Vehicle(180, 398.000)
    cytrus.mileage_increase(300)

if __name__ == "__main__":
    main()


