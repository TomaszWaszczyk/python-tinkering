
import sqlite3

print('Początek programu')

polaczenie = sqlite3.connect('hr.db')
print('Udało się połączyć', polaczenie)

kursor = polaczenie.execute('SELECT * FROM employees')
print('execute zwróciło taki kursor:', kursor)

# Jeśli nie chcemy wczytywać wszystkich danych do pamięci (bo mogą być bardzo duże)
# możemy też dane przeglądać pojedynczo. Jest to wygodnie dzięki temu, że kursor jest iterowalny
# (podobnie jak linie w otwartym pliku).

for emp in kursor:
    print(emp[1], emp[2], 'zarabia', emp[7])
print('-----------------------')

# możliwy prostszy zapis, bo execute zwraca w wyniku referencję do samego kursora
for rekord in polaczenie.execute('SELECT * FROM locations'):
    print(rekord)
print('-----------------------')

polaczenie.close()
print('Koniec')
