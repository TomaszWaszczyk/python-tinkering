class Employee:
    def __init__(self, id, first_name, last_name, job_title, salary,
                 hire_date, department_name, street_address, postal_code, city, country):
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

    def __str__(self):
        return f'Employee {self.id}: {self.first_name} {self.last_name} ({self.job_title}) {self.salary} USD'


def wczytaj_pracownikow(sciezka):
    lista = []
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        for linia in plik:
            pola = linia.strip().split(';')
            emp = Employee(int(pola[0]), pola[1], pola[2], pola[3], int(pola[4]),
                           pola[5], pola[6], pola[7], pola[8], pola[9], pola[10])
            lista.append(emp)
    return lista

def zapisz_pracownikow(employees, sciezka):
    with open(sciezka, mode='w', encoding='utf-8') as wyjscie:
        for emp in employees:
            print(emp.id, emp.first_name, emp.last_name, emp.job_title, emp.salary, emp.hire_date,
                  emp.department_name, emp.street_address, emp.postal_code, emp.city, emp.country,
                  sep=';', file=wyjscie)

