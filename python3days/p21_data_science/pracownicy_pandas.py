import pandas

# dane = pandas.read_csv('pracownicy.csv', encoding='UTF-8', sep=';', header=None)
dane = pandas.read_csv('pracownicy_z_naglowkiem.csv', encoding='UTF-8', sep=';')
print(dane)
print()

srednia = dane.salary.mean()
print('Średnia wszystkich:', srednia)

sredniap = dane[dane.job_title=='Programmer'].salary.mean()
print('Średnia programistów:', sredniap)

