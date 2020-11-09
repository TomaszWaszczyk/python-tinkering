
import sqlite3

stanowisko = input('Podaj kod stanowiska, np. IT_PROG: ')

# TODO niech program wypisze tylko tych pracowników, których kolumna job_id ma taką wartość

polaczenie = sqlite3.connect('hr.db')
print('Udało się połączyć', polaczenie)

kursor = polaczenie.execute('SELECT * FROM employees')
print('execute zwróciło taki kursor:', kursor)

for emp in kursor:
    print(emp[1], emp[2], emp[6], 'zarabia', emp[7])

polaczenie.close()

print('Koniec')
