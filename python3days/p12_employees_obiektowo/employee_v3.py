from typing import Sequence, List, NoReturn

# W tej wersji używamy "type hints" aby podać typy parametrów i wyników funkcji.
# Sam interpreter Pythona ich nie sprawdza, ale stanowią one:
# 1) element dokumentacji, aby kod bardziej czytelny
# 2) pomagają narzędziom takim jak Pycharm w podpowiedziach

class Employee:
    def __init__(self, id:int, first_name:str, last_name:str, job_title:str, salary:float,
                 hire_date:str, department_name:str, street_address:str, postal_code:str, city:str, country:str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.department_name = department_name
        self.street_address = street_address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    @staticmethod
    def of_csv_fields(fields:Sequence[str]) -> 'Employee':
        return Employee(int(fields[0]), fields[1], fields[2], fields[3], int(fields[4]),
                        fields[5], fields[6], fields[7], fields[8], fields[9], fields[10])

    def __str__(self) -> str:
        return f'Employee {self.id}: {self.first_name} {self.last_name} ({self.job_title}) {self.salary} USD'

    def change_salary(self, amount:float) -> NoReturn:
        self.salary += amount

    def csv_fields(self) -> Sequence[str]:
        return (self.id, self.first_name, self.last_name, self.job_title, self.salary, self.hire_date,
                self.department_name, self.street_address, self.postal_code, self.city, self.country)
        # return self.__dict__.values()


SEPARATOR = ';'

def wczytaj_pracownikow(path:str) -> List[Employee]:
    wynikowa_lista = []

    with open(path, mode='r', encoding='utf-8') as wejscie:
        for linia in wejscie:
            pola = linia.strip().split(SEPARATOR)
            nowy_pracownik = Employee.of_csv_fields(pola)
            wynikowa_lista.append(nowy_pracownik)

    return wynikowa_lista


def zapisz_pracownikow(employees:Sequence[Employee], path:str) -> NoReturn:
    with open(path, mode='w', encoding='utf-8') as wyjscie:
        for emp in employees:
            print(*emp.csv_fields(), sep=SEPARATOR, file=wyjscie)
