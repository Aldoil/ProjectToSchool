"""
ZADANIE 4. (10 punktów)
Gra losowa polega na zgadnięciu 6 liczb z przedziału od 1-10, wygrana następuję gdy mamy co najmniej 5 trafień. Kolejność podania liczb jest nieistotna.
Napisz program, który ma celu sprawdzenie prawdopodobieństwa sukcesu w pewnej grze losowej.
Masz przeprowadzić symulację 1000 krotnej próby gry w tej grę. Zadbaj o to żeby zarówno liczby podane jak i wylosowane nie powtarzały się np.
nie może być tak że wylosowane to [1,8,3,4,8,3]. Na koniec podaj prawdopodobieństwo sukcesu, czyli ilość wygranych gier w naszej symulacji.
Podpowiedź: Symulacja jednej gry polega na stworzeniu dwóch list, a następnie sprawdzeniu ile się powtarza.
"""

import random
import re

def random_int_list():
    """ Creating list of random integers """
    rand = []
    for i in range(6):
        a = random.randint(1,10)
        if a in rand:
            while a in rand:
                a = random.randint(1, 10)

        if a not in rand:
            rand.append(a)
    return rand


def user_int_list():
    """ Creating list of elements given by the user """
    user = []
    for i in range(6):
        while True:
            b = input(f'Podaj liczbe {i+1} od 1 do 10:   ')

            if  not re.match('[0-9]', b):
                print('Podano wartość nieprawidłową.')
                continue
            if int(b) in user:
                print('Podano tą samą wartość, spróbuj ponownie.')
                continue

            if (int(b) <= 0 or int(b) > 10):
                print('Podano wartość nieprawidłową, zakres liczb to 1-10.')
                continue

            if (int(b) > 0 and int(b) <=10):
                user.append(int(b))
                break
    return user

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    elif n in (0,1):
        return 1

answer = ''
while answer != 'STOP':
    print('Witaj w programie!')
    print('1. Podaj liczby i sprawdz czy wygrałeś.')
    print('2. Sprawdz prawdopodobieństwo wygrania.')
    print('3. Sprawdz ile gier uda się wygrać przy 1000 próbach.')
    print('4. Zakończ program.')
    print('\n')

    answer = input('Wybierz jedną z powyższych opcji: ')

    result = 0
    if answer == '1':

        first = random_int_list()
        second = user_int_list()
        print(first)
        print(second)
        for i in first:
            if i in second:
                result +=1
            else:
                continue
        if result >= 5:
            print(f'Gratulacje wygrałeś podająć poprawnie {result} liczb!')
        else:
            print(f'Niestety, podałeś poprawnie tylko {result} liczb.')

    if answer == '2':


        six = ((factorial(10)) / ((factorial(6)) * (factorial(10 - 6))))
        print('\nWszystkich możliwych kombinacji trafienia 6 liczb jest : ', int(six))
        print('Możliwych kombinacji trafienia 5 z 6 liczb : ', factorial(5-1))
        propability = six/factorial(5-1)

        print('Prawdopodobieństwo trafienia conajmniej 5 cyfr wynosi: ',  round(1/propability,2)*100, '%\n')
    if answer == '3':

        end_res = 0
        for i in range(1000):
            res = 0
            first_list = random_int_list()
            second_list = random_int_list()
            for number in first_list:
                if number in second_list:
                    res +=1
                else:
                    continue
            if res >= 5:
                end_res += 1
            else:
                continue
        print(end_res, '\n')

    if answer == '4':
        break















