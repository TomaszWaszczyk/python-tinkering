with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
    for nr, linia in enumerate(plik):
        print(f'{nr + 1:5}: {linia}', end='')
