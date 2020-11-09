# Zasadniczo pętla for działa na zasadzie przeglądania kolekcji i wykonania czyności dla każdego elementu kolekcji.
# for zmienna in KOLEKCJA:
#    TREŚĆ

for imie in ['Ala', 'Ola', 'Ela', 'Ula']:
    print('Witaj', imie)
print()

# Bardzo często używa się pętli for w połączeniu z range.
# range - generator liczb z określonego przedziału

for liczba in range(10, 20):
    print('Kolejna liczba to', liczba)

# W Pythonie nie ma takiej pętli for jak w C, C++, Java, JavaScript, C#, PHP
# for(int i = 0; i < n; i++)
