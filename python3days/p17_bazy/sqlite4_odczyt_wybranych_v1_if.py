
import sqlite3

stanowisko = input('Podaj kod stanowiska, np. IT_PROG: ')

# TODO niech program wypisze tylko tych pracowników, których kolumna job_id ma taką wartość

polaczenie = sqlite3.connect('hr.db')

kursor = polaczenie.execute('SELECT * FROM employees')

for emp in kursor:
    if emp[6] == stanowisko:
        print(emp[1], emp[2], emp[6], 'zarabia', emp[7])

polaczenie.close()

# W tej wersji wczytujemy wszystkie rekordy, a nasz program w Pythonie przegląda je i sprawdza, które wypisać
# To jest niewydajnie jeśli weźmiemy większe p17_bazy danych.
# Pobieramy wszystkie dane: baza musi przeczytać wszystkie rekordy,
# (w przypadku prawdziwych baz) całe dane są transferowane przez sieć
# nasz program w Pythonie przegląda wszystkie rekordy i ma dużo roboty.
# Przy tym podejściu nie skorzystamy z indeksów założonych w bazie danych.
