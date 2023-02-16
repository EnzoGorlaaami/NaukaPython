from typing import Union
class Vehicle:

    def __init__(self, type: str, max_speed: int, number: int, depot: str):
        self.type = type
        self.max_speed = max_speed
        self.number = number
        self.depot = depot

    def __str__(self) -> str:
            return f"I'm {self.type} nr. {self.number}, My depot is {self.depot}, my max speed is {self.max_speed}"



class Tram(Vehicle):
    def __init__(self, number: int, carts: int) -> None:
        super().__init__('Tram', 40, number, 'Tram_Depot')
        self.carts = carts
        while self.carts not in range(1, 4):
            self.carts = int(input("Set number of cars in range between 1-3: "))

        # if 1 <= attributes <= 3:
        #     super().__init__('Tram', 40, number, 'Tram_Depot', attributes)
        # else:
        #     print('Wrong number of tram cars! ')
        #     new_atr = int(input('Set number of tram cars between 1 - 3: '))
        #     super().__init__('Tram', 40, number, 'Tram_Depot', new_atr)

    def __str__(self):
        return super().__str__() + f", and I have {self.carts} tram cars."

class Bus(Vehicle):
    def __init__(self, number: int, daily_fuel_use: int) -> None:
        super().__init__('Bus', 80, number, 'Bus_Depot')
        self.daily_fuel_use = daily_fuel_use

    def __str__(self):
        return super().__str__() + f"and I'had burned {str(self.daily_fuel_use)} liters of fuel this day."

class Depot:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type
        self.vehicle_list: list[Union[Bus, Tram]] = []

    def add_veh(self, vehicle: Union[Bus, Tram]) -> None:
        self.vehicle_list.append(vehicle)

    def __str__(self) -> str:
        return f"Welcome at {self.name}! We are a {self.type}. We got {len(self.vehicle_list)}"

    def introduce(self) -> None:
        print(self)
        for veh in self.vehicle_list:
            print(veh)

class BusDepot(Depot):
    def __init__(self, name):
        super().__init__(name, 'Bus_Depot')

    def monthly_fuel_consumption(self) -> int:
        fuel = 0
        for vehicle in self.vehicle_list:
            fuel += vehicle.daily_fuel_use * 30
        return fuel

    def __str__(self):
        return super().__str__() + f'buses. Our total fuel consumption is {self.monthly_fuel_consumption()} liters in this month.'

class TramDepot(Depot):
    def __init__(self, name):
        super().__init__(name, 'Tram_Depot')

    def total_sum_of_carts(self) -> int:
        carts = 0
        for vehicle in self.vehicle_list:
            carts += vehicle.carts
        return carts

    def __str__(self):
        return super().__str__() + f" trams. Our total tram cars is {self.total_sum_of_carts()}.'"


def main():
    bus = BusDepot('Bus Park')
    tram = TramDepot('Tram Park')
    bus49 = Bus(49, 60)
    bus56 = Bus(56, 123)
    tram777 = Tram(777, 2)
    tram75 = Tram(75, 4)
    bus.add_veh(bus49)
    bus.add_veh(bus56)
    tram.add_veh(tram777)
    tram.add_veh(tram75)
    bus.introduce()
    tram.introduce()


if __name__ == "__main__":
    main()

