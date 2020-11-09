# Program pyta użytkownika o wiek i na podstawie wieku sugeruje zakup określonego towaru:
# Ile masz lat?...
#
# 0-3 - kaszka z mleczkiem
# 4-17 - czipsy z colą
# 18-64 - piwo i grill
# 65+ - Biovital

wiek = int(input('Ile masz lat? '))

if wiek < 0:
    print('JESZCZE CIĘ NIE MA')
elif wiek < 4:
    print('Możesz kupić kaszkę z mleczkiem')
elif wiek < 18:
    print('Możesz kupić czipsy z colą')
elif wiek < 65:
    print('Możesz kupić piwo na grillu')
else:
    print('Możesz kupić Biovital')
