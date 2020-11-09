# Przykład użycia p17_bazy danych SQLite - baza w pliku, bez serwera.
# Przykład wymaga obecności pliku hr.db - baza z pracownikami - Steven King itd.

# Moduł sqlite jest w bibliotece standardowej - nie trzeba instalować.
import sqlite3

print('Początek programu')

polaczenie = sqlite3.connect('hr.db')
print('Udało się połączyć', polaczenie)

kursor = polaczenie.execute('SELECT * FROM employees')
print('execute zwróciło taki kursor:', kursor)

# wyciągamy wszystkie rekordy w formie listy
# istnieje też fetchmany - czyta porcjami
lista_wynikow = kursor.fetchall()
# wynikiem jest lista tupli (aka "krotek")
print(lista_wynikow)
print()

for emp in lista_wynikow:
    print(emp[1], emp[2], 'zarabia', emp[7])

polaczenie.close()

print('Koniec')
