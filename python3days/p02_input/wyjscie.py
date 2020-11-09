# Wypisywanie tekstów i danych na konsolę - print

# Można wypisać konkretne napisy w i wartości

print("Ala ma kota")
print("Ala", "ma", "kota")
print(123)
print(12 * 15)
print(12,"razy",15,"równa się",12*15)
# Domyślnie print wypisuje dane w jednej linii, a po wypisaniu przechodzi do następnej
# a wartości przekazane po przecinku rozdziela za pomocą pojedynczej spacji.

napis = "Ala ma kota"
liczba = 123
ulamek = 0.25

print(napis, liczba, ulamek)
print('AAA', napis, 'BBB', liczba, ulamek)
print()

# Aby odstępem nie była spacja, tylko coś innego, może podać parametr sep

print('Ala','Ola','Ela') # rozdziela spacjami

print('Adam', 'Tomasz', 'Andrzej', sep=' oraz ') # rozdziela słowem oraz
print('Ala', 'Ola', 'Ela', sep=';')
print('Warszawa', 'Kraków', sep='')

# Aby print nie przechodził do nowej linii, można ustawić pusty parametr end

print('Ala ma kota', end='')
print('Ola', 'ma', 'psa', end='!')
print('Koniec')

# inne sposoby łączenia danych w jednym tekście - formatowanie.py
