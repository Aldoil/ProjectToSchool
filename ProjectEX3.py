"""
ZADANIE 3. (10 punktów)
Napisz funkcję, która będzie generować wielomian n-tego stopnia - ten stopień zostać podany jako parametr tej funkcji.
W ciele funkcji powinna się znaleźć instrukcja dla użytkownika, który ma podać współczynniki tego wielomianu (nie więcej, niż zawiera stopień tego wielomianu!).
Pamiętaj, aby uwzględnić możłiwość wpisania innego typu zmiennej niż liczby - gdy tak się stanie, program ma się spytać ponownie o współczynnik.
Należy również wypisać zdanie typu: „Wilemoian n-tego stopnia ma postać: [wielomian]”.
Funkcja powinna zwracać współczynniki tego wielomianu.
"""

import re

def generate_polynominal(n):
    i = 0
    while i < n:
        polynominal = ''
        res = []
        for i in range(n):
            a = input(f'Podaj wartość współczynnika {i+1}: ')

            if  re.match('[0-9]', a):
                n= str(n)
                polynominal = polynominal + (a+'* x **'+n + ' + ')
            else:
                while not re.match('[0-9]', a):
                    print('Podaj tylko liczbe calkowita!')
                    a = input(f'Podaj wartość współczynnika {i + 1}: ')
                    if re.match('[0-9]', a):
                        polynominal = polynominal + (a+'* x **'+n + ' + ')
                        break
                    else:
                        continue
            res.append(a)
            i +=1

        polynominal = polynominal[:(len(polynominal)-2)]
        print(f'Wilemoian n-tego stopnia ma postać: {polynominal}')
        return print('Współczynniki tego wielomianu to: ', res)

generate_polynominal(10)



