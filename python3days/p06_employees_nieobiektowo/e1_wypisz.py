with open('pracownicy.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        t = linia.split(';')
        first_name = t[1]
        last_name = t[2]
        salary = int(t[4])
        print(f'{first_name} {last_name} zarabia {salary}')
