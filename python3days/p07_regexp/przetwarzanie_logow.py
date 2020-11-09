# 2020-09-22 22:55:24|install|libqt4-sql-sqlite|4.8.7-lp152.10.3.1
import re

FILE = 'zypper.log'

PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})\|(\w+)\|([^|]+)\|([^|]+)')

ops = {'install', 'patch'}

czegoszukam = 'python3'

with open(FILE) as file:
    for line in file:
        m = PATTERN.match(line)
        if m and m[3] in ops:
            #print(m[1], m[2], m[3], m[4], m[5])
            if m[4].startswith(czegoszukam):
                print(f'Pakiet {m[4]} w wersji {m[5]} został zainstalowany {m[1]}')
