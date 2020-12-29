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
    """ Generate n-degree polynomial """
    i = 0
    while i < n:
        polynominal = ''
        res = []
        for i in range(n+1):

            a = input(f'Podaj wartość współczynnika {i+1}: ')
            if  re.match('[0-9]', a) and n !=0:
                polynominal = polynominal + (f'{a}* x **{n} + ' )
            elif n == 0:
                polynominal = polynominal + str(a)
            else:
                while not re.match('[0-9]', a):
                    print('Podaj tylko liczbe calkowita!')
                    a = input(f'Podaj wartość współczynnika {i + 1}: ')
                    if re.match('[0-9]', a):
                        polynominal = polynominal + (f'{a}* x **{n} + ' )
                        break
                    else:
                        continue
            n -= 1
            res.append(a)
            i +=1

        print(f'Wilemoian n-tego stopnia ma postać: {polynominal}')
        return print('Współczynniki tego wielomianu to: ', res)
power = input('Podaj stopień wielomianu: ')
power= int(power)
generate_polynominal(power)



