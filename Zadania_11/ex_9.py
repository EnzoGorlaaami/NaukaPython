from datetime import datetime as dt

class Notes:
    timeformat = '%Y-%m-%d \ %H:%M'
    counter = 0
    def __init__(self, work_name: str, tank_name: str, water_volume: int, status: int) -> None: #stasus -> 0 = error \ stasus -> 1 = done
        Notes.counter += 1
        self.date = dt.now()
        self.number = Notes.counter
        self.work_name = work_name
        self.tank_name = tank_name
        self.water_volume = water_volume
        self.status = status

    # def notes_list(self) -> None:
    #     self.note_list: list[Notes] = [] -> nie wiem jak sie do tego dostac, myslalem zeby zrobic to w init ale wtedy bylby dluzszy kod wiec wyrzucilem note_list poza klasę, a potem w klasie report sie do niej odwołałem

    def __str__(self):
        status_str: list[str] = ['Error', 'Done']
        return f'Date: {dt.strftime(self.date, Notes.timeformat)} | Number: {self.number} | Action: {self.work_name} | Tank name: {self.tank_name} | Water volume: {self.water_volume} | Status: {status_str[self.status]}'

note_list: list[Notes] = []
class Tank:
    def __init__(self, name: str, volume: int, actual_volume: int):
        self.name = name
        self.volume = volume
        self.actual_volume = actual_volume
        self.start_volume = actual_volume

    def __str__(self):
        return f'Tank: "{self.name}" | Volume: {self.volume}L. | Actual volume: {self.actual_volume}L. '


    def free_space(self) -> int:
        space = self.volume - self.actual_volume
        return space

    def pour_water(self, water_volume: int) -> None:
        space = self.free_space()
        if water_volume > space:
            print('Too much water!')
            pour_water_note = Notes('pour_water', self.name, water_volume, 0)
            note_list.append(pour_water_note)
        else:
            self.actual_volume += water_volume
            print('Water added to the Tank! ')
            pour_water_note = Notes('pour_water', self.name, water_volume, 1)
            note_list.append(pour_water_note)

    def pour_out_water(self, water_volume: int) -> None:
        if water_volume > self.actual_volume:
            print('No enough water!')
            pour_out_water_note = Notes('pour_out_water', self.name, -water_volume, 0)
            note_list.append(pour_out_water_note)
        else:
            self.actual_volume -= water_volume
            print('Water pour out!')
            pour_out_water_note = Notes('pour_out_water', self.name, -water_volume, 1)
            note_list.append(pour_out_water_note)

    def transfer_water(self, tank, water_volume: int) -> None:
        space = self.free_space()
        if tank.actual_volume < water_volume:
            print('No enough water in Tank!')
            transfer_water_note = Notes('transfer_water', self.name, water_volume, 0)
            note_list.append(transfer_water_note)
        elif water_volume > space:
            print('No enough space in Tank!')
            transfer_water_note = Notes('transfer_water', self.name, water_volume, 0)
            note_list.append(transfer_water_note)
        else:
            self.actual_volume += water_volume
            tank.actual_volume -= water_volume
            print(f'From {tank.name} added {water_volume}L. water for {self.name}')
            transfer_water_note = Notes('transfer_water', self.name, water_volume, 1)
            transfer_water_note2 = Notes('transfer_water', tank.name, -water_volume, 1)
            note_list.extend([transfer_water_note, transfer_water_note2])

    def tank_return(self) -> list[str, int]:
        tank_name = self.name
        volume = self.volume
        actual_volume = self.actual_volume
        return [tank_name, volume, actual_volume]
class TankBase:
    def __init__(self) -> None:
        self.tank_list: list[Tank] = []

    def __str__(self):
        return f"There's {len(self.tank_list)} tanks in TankBase."

    def add_tank(self, tank: Tank) -> None:
        self.tank_list.append(tank)

    def most_water(self) -> str:
        most_water_tank = ['xxx',0, 0]
        for tank in self.tank_list:
            i = tank.tank_return()
            if i[2] > most_water_tank[2]:
                most_water_tank = i
        return f'The tank with the highest water level is {most_water_tank[0]} with {most_water_tank[2]}L. of water.'

    def most_full_tank(self) -> str:
        most_full_tank = ['xxx',0, 0]
        most_full_tank_percentage = 0
        for tank in self.tank_list:
            tank_data = tank.tank_return()
            percentage = int((tank_data[2] / tank_data[1]) * 100)
            if percentage > most_full_tank_percentage:
                most_full_tank = tank_data
                most_full_tank_percentage = percentage
        return f'The tank witch is most full of water is {most_full_tank[0]} and it is {most_full_tank_percentage}% full'

    def empty_tanks(self) -> str:
        empty_tank_list = []
        for tank in self.tank_list:
            if tank.actual_volume == 0:
                empty_tank_list.append(tank)
        return f"There's {len(empty_tank_list)} empty tanks"



class Raport:
    def __init__(self):
        self.raport_list = note_list

    def most_error(self) -> str:
        error_dict = {}
        for raport in self.raport_list:
            if raport.status == 0:
                if raport.tank_name in error_dict:
                    error_dict[raport.tank_name] += 1
                else:
                    error_dict.update({raport.tank_name : 1})
        most_error_tanks = []
        most_errors = max(error_dict.values())
        for key, val in error_dict.items():
            if val == most_errors:
                most_error_tanks.append(key)
        return f"Most error's numer is {most_errors}, and these tanks have so many of them: {most_error_tanks}. "

    def most_operation(self, operation_name: str) -> str:
        self.operation_name = operation_name
        operation_dict = {}
        for raport in self.raport_list:
            if raport.work_name == self.operation_name:
                if raport.work_name in operation_dict:
                    operation_dict[raport.tank_name] += 1
                else:
                    operation_dict.update({raport.tank_name : 1})
        most_operations_tanks = []
        most_operations = max(operation_dict.values())
        for key, val in operation_dict.items():
            if val == most_operations:
                most_operations_tanks.append(key)
        return f"For {self.operation_name} operation, most of this activity took place on {most_operations_tanks}, in the number of {most_operations}. "

    def check_state(self, tank: [Tank]):
        self.tank = tank
        real_volume = tank.actual_volume
        start_volume = tank.start_volume
        sum_of_operations = real_volume - start_volume
        sum_of_raport_operations = 0
        for raport in self.raport_list:
            if raport.tank_name == tank.name:
                if raport.status == 1:
                    sum_of_raport_operations += raport.water_volume
        if sum_of_operations == sum_of_raport_operations:
            return "The water level in the tank is consistent with the reports. "
        else:
            return "The water level in the tank isn't consistent with the reports. "


def main():
    yyy = TankBase()
    xxx = Tank('zbiornik1', 1000, 100)
    xxx2 = Tank('zbiornik2', 1000, 300)
    print(xxx)
    print(xxx2)
    yyy.add_tank(xxx)
    yyy.add_tank(xxx2)
    xxx.transfer_water(xxx2, 200)
    xxx.pour_water(300)
    xxx.pour_out_water(1300)
    xxx.pour_out_water(1300)
    xxx.pour_out_water(1300)
    for notes in note_list:
        print(notes)
    print(yyy.most_water())
    print(yyy.most_full_tank())
    print(yyy.empty_tanks())
    zzz = Raport()
    print(zzz.most_error())
    print(zzz.most_operation('transfer_water'))
    print(zzz.check_state(xxx))




if __name__ == '__main__':
    main()