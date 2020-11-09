# Wersja z wykorzystaniem * - moim zdaniem mniej porządna, gdzie w samym init dokonujemy konwersi typów

class Employee:
    def __init__(self, id, first_name, last_name, job_title, salary,
                 hire_date, department_name, street_address, postal_code, city, country):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = int(salary)
        self.hire_date = hire_date
        self.department_name = department_name
        self.street_address = street_address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return f'Employee {self.id}: {self.first_name} {self.last_name} ({self.job_title}) {self.salary} USD'


def wczytaj_pracownikow(sciezka):
    lista = []
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        for linia in plik:
            pola = linia.strip().split(';')
            lista.append(Employee(*pola))
    return lista
