liczby = [33, 21, 11, 14, 27, 13]
# liczby = [33, 21, 11, 27, 13]

for x in liczby:
    print('Oglądam liczbę', x)
    if x % 2 == 0:
        print('Znalazłem liczbę parzystą:', x)
        break
    print('a kuku')
else:
    print('Nie zalazłem liczby parzystej')

print('Koniec programu')

# Pętle for oraz while mogą mieć dodatkowo dopisane else:
# Jeśli pętla kończy się z powodu break, to treść else nie jest wykonywana.
# Jeśli pętla kończy się "normalnie" (for doszedł do końca, while ma niespełniony warunek),
# to wtedy else się wykonuje. Również wtedy, gdy program w ogóle nie wszedł do pętli.
# Najczęstsze zastosowanie: jakaś forma wyszukiwania i wykonywania czynności w przypadku niezalezienia.
