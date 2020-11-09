
import sqlite3

stanowisko = input('Podaj kod stanowiska, np. IT_PROG: ')

# TODO niech program wypisze tylko tych pracowników, których kolumna job_id ma taką wartość

polaczenie = sqlite3.connect('hr.db')

kursor = polaczenie.execute(f"SELECT * FROM employees WHERE job_id = '{stanowisko}'")

for emp in kursor:
    print(emp[1], emp[2], emp[6], 'zarabia', emp[7])

polaczenie.close()

# To zapytanie jest już wydajne.

# Przykładowy kod, który zamula bazę danych (u mnie na kilka minut):
# IT_PROG' AND (SELECT count(*) FROM employees e1, employees e2, employees e3, employees e4, employees e5) > 1000000 AND job_id = 'IT_PROG
