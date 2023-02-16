# Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:
import datetime

first_case = {'name': 'first_case', 'created_task' : '2021-10-26T19:48:12', 'end_task' : None}
second_case = {'name': 'second_case','created_task': '2021-09-26T19:48:12', 'end_task' : '2021-10-26T19:48:12'}

# Klasa Case ma zawierać metodę retrieve_seconds, która zwracać będzie różnicę czasową między end_task a created_task podaną w sekundach.
#
# UWAGA
# Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa.
# Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie

from datetime import datetime as dt



class Case:
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
    def __init__(self, name: str, created_task: str, end_task: datetime) -> None:
        self.name = name
        self.created_task: datetime = dt.strptime(created_task, Case.TIME_FORMAT)
        if not end_task:
            self.end_task = dt.now()
        else:
            self.end_task = dt.strptime(end_task, Case.TIME_FORMAT)

    def calculate_seconds(self) -> datetime.timedelta:
        task_duration = self.end_task - self.created_task
        return task_duration

    def retrieve_seconds(self) -> float:
        return round(self.calculate_seconds().total_seconds(), 1)

def main():
    first = Case(first_case['name'], first_case['created_task'], first_case['end_task'])
    first_1 = Case(**first_case) # -> name=
    second = Case(second_case['name'], second_case['created_task'], second_case['end_task'])
    print(first_1.retrieve_seconds())



if __name__ == "__main__":
    main()