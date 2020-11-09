# Podejście do testowania nr 1:
# mamy program interaktywny (w praktyce raczej webowy, ale tutaj konsolowy)
# poprzez ten program będziemy sprawdzać czy jakaś klasa / funkcja działa prawidłowo

# Zaleta: elastyczność, łatwość wpisywanie róznych danych
# Wada: pracochłonność, błędogenność (łatwo przeoczyć)

from klasa_employee import Employee

stawka = int(input('Podaj stawkę: '))
emp = Employee('Ala', 'Kowalska', stawka)

while True:
    wybor = input('Co chcesz zrobić: P - praca, W - wypłata, Q - koniec\n').strip().upper()
    if wybor == 'P':
        g = int(input('Ile godzin? '))
        emp.register_time(g)
    elif wybor == 'W':
        sal = emp.pay_salary()
        print('Wypłata: ', sal)
    elif wybor == 'Q':
        break

print('papa')
