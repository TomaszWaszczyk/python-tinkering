# Przykład obsługi parametrów.
# W porównaniu do SQLite, tutaj należy inaczej oznaczać miejsca na parametry - za pomocą %s.

import psycopg2
# conn = psycopg2.connect("host='localhost' dbname='hr' user='hr' password='abc123'")
conn = psycopg2.connect("host='vps497901.ovh.net' dbname='hr' user='hr' password='vps497901_abc123'")
c = conn.cursor()

print('Wszystkie stanowiska:')
print(f'  Kod  | Stanowisko')
c.execute("SELECT job_id, job_title FROM jobs ORDER BY 1")
for row in c:
    print(f'{row[0]:8} | {row[1]}')
print()

sql = "SELECT count(*), min(salary), max(salary), avg(salary) FROM employees WHERE job_id=%s"
while True:
    job = input(f'Podaj kod stanowika: ')
    if not job:
        break
    job = job.strip().upper()
    # Przekazuję tuplę parametrów, które będą wpisane na poszczególne znaki zapytania - tutaj tylko jeden parametr
    c.execute(sql, (job, ))
    
    # tak można odczytać jeden wiersz wyniku; przy okazji unpacking, bo wiersz z tabeli jest udostępniany jako tupla
    count, min, max, avg = c.fetchone()
    print(f'Liczba pracowników: {count:5}')
    print(f'Najmniejsza pensja: {min:8.2f}')
    print(f'Największa pensja:  {max:8.2f}')
    print(f'Średnia pensja:     {avg:8.2f}')

conn.close()
print('Koniec')
