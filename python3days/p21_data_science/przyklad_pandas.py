import pandas

print('Startujemy')
emps = pandas.read_csv('pracownicy_z_naglowkiem.csv',
                       index_col='employee_id',
                       encoding='utf-8',
                       sep=';')

print('Udało się wczytać')
print('============================')
print(emps)
print('============================')
print()

pensja = emps.loc[107, 'salary']
print('Prykładowa pensja:', pensja)

pensja = emps.iloc[7, 3]
print('Prykładowa pensja:', pensja)
print()

srednia = emps.salary.mean()
print('Średnia wszystkich:', srednia)

srednia = emps[emps.job_title == 'Programmer'].salary.mean()
print('Średnia programistów:', srednia)
print()

# grupy = emps.groupby('job_title').mean()
grupy = emps.groupby('job_title').agg({'salary': ['count', 'min', 'mean', 'max']})
print(grupy)
print()

grupy.to_csv('grupy.csv', sep=';')
# grupy.to_excel('grupy.xlsx')
grupy.to_html('grupy.html')
print('Zapisane do pliku')

pensje = emps.groupby('job_title').mean()
wykres = pensje.plot(kind='bar')
wykres.figure.savefig('wykres.png')
print('Wykres zapisany')
