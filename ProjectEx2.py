"""
ZADANIE 2. (15 punktów)
Trwają wybory na prezesa koła naukowego.
Jest 3 kandydatów oraz 10 głosujących. Napisz program, który umożliwi każdemu z głosujących uszeregowanie kandydatów według preferencji.
Program ma znać odgórnie kandydatów oraz głosujących oraz po kolei dać tym ostatnim szansę na uszeregowanie preferencji.
Elektor nie powinien mieć możliwości nadania tej samej kolejności preferencji dwóm różnym kandydatom, kolejność preferencji powinna być określona od 1 do 3.

Następnie program ma policzyć głosy. Z każdej „karty wyborczej” program ma policzyć głosy według preferencji:
kandydat najbardziej preferowany otrzymuje od elektora 2 głosy, środkowy 1 a ostatni 0.
Program ma policzyć ogólną liczbę głosów oddanych na danego kandydata oraz wyświetlić wynik wyborów po procedurze szeregowania preferencji.

DLA CHĘTNYCH: stwórz raport wyborczy, który będzie tworzony przez program po zakończeniu procedury wyborczej, który będzie przechowywany w pliku .txt.
"""


def elektor1():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote1_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote1_2 = input('kandydat nr 2 - Anna Woda: ')
        vote1_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote1_2 in ['1', '2', '3'] and vote1_3 in ['1', '2', '3'] and vote1_1 in ['1', '2', '3']:
            vote1_1, vote1_2, vote1_3 = int(vote1_1), int(vote1_2), int(vote1_3)
            if (vote1_1 == vote1_2) or (vote1_2 == vote1_3) or (vote1_3 == vote1_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote1_2 or vote1_3 or vote1_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote1_1, vote1_2, vote1_3







def elektor2():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote2_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote2_2 = input('kandydat nr 2 - Anna Woda: ')
        vote2_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote2_2 in ['1', '2', '3'] and vote2_3 in ['1', '2', '3'] and vote2_1 in ['1', '2', '3']:
            vote2_1, vote2_2, vote2_3 = int(vote2_1), int(vote2_2), int(vote2_3)
            if (vote2_1 == vote2_2) or (vote2_2 == vote2_3) or (vote2_3 == vote2_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote2_2 or vote2_3 or vote2_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote2_1, vote2_2, vote2_3


def elektor3():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote3_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote3_2 = input('kandydat nr 2 - Anna Woda: ')
        vote3_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote3_2 in ['1', '2', '3'] and vote3_3 in ['1', '2', '3'] and vote3_1 in ['1', '2', '3']:
            vote3_1, vote3_2, vote3_3 = int(vote3_1), int(vote3_2), int(vote3_3)
            if (vote3_1 == vote3_2) or (vote3_2 == vote3_3) or (vote3_3 == vote3_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote3_2 or vote3_3 or vote3_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote3_1, vote3_2, vote3_3

def elektor4():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote4_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote4_2 = input('kandydat nr 2 - Anna Woda: ')
        vote4_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote4_2 in ['1', '2', '3'] and vote4_3 in ['1', '2', '3'] and vote4_1 in ['1', '2', '3']:
            vote4_1, vote4_2, vote4_3 = int(vote4_1), int(vote4_2), int(vote4_3)
            if (vote4_1 == vote4_2) or (vote4_2 == vote4_3) or (vote4_3 == vote4_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote4_2 or vote4_3 or vote4_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote4_1, vote4_2, vote4_3



def elektor5():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote5_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote5_2 = input('kandydat nr 2 - Anna Woda: ')
        vote5_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote5_2 in ['1', '2', '3'] and vote5_3 in ['1', '2', '3'] and vote5_1 in ['1', '2', '3']:
            vote5_1, vote5_2, vote5_3 = int(vote5_1), int(vote5_2), int(vote5_3)
            if (vote5_1 == vote5_2) or (vote5_2 == vote5_3) or (vote5_3 == vote5_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote5_2 or vote5_3 or vote5_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote5_1, vote5_2, vote5_3



def elektor6():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote6_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote6_2 = input('kandydat nr 2 - Anna Woda: ')
        vote6_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote6_2 in ['1', '2', '3'] and vote6_3 in ['1', '2', '3'] and vote6_1 in ['1', '2', '3']:
            vote6_1, vote6_2, vote6_3 = int(vote6_1), int(vote6_2), int(vote6_3)
            if (vote6_1 == vote6_2) or (vote6_2 == vote6_3) or (vote6_3 == vote6_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote6_2 or vote6_3 or vote6_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote6_1, vote6_2, vote6_3



def elektor7():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote7_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote7_2 = input('kandydat nr 2 - Anna Woda: ')
        vote7_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote7_2 in ['1', '2', '3'] and vote7_3 in ['1', '2', '3'] and vote7_1 in ['1', '2', '3']:
            vote7_1, vote7_2, vote7_3 = int(vote7_1), int(vote7_2), int(vote7_3)
            if (vote7_1 == vote7_2) or (vote7_2 == vote7_3) or (vote7_3 == vote7_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote7_2 or vote7_3 or vote7_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote7_1, vote7_2, vote7_3



def elektor8():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote8_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote8_2 = input('kandydat nr 2 - Anna Woda: ')
        vote8_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote8_2 in ['1', '2', '3'] and vote8_3 in ['1', '2', '3'] and vote8_1 in ['1', '2', '3']:
            vote8_1, vote8_2, vote8_3 = int(vote8_1), int(vote8_2), int(vote8_3)
            if (vote8_1 == vote8_2) or (vote8_2 == vote8_3) or (vote8_3 == vote8_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote8_2 or vote8_3 or vote8_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote8_1, vote8_2, vote8_3


def elektor9():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote9_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote9_2 = input('kandydat nr 2 - Anna Woda: ')
        vote9_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote9_2 in ['1', '2', '3'] and vote9_3 in ['1', '2', '3'] and vote9_1 in ['1', '2', '3']:
            vote9_1, vote9_2, vote9_3 = int(vote9_1), int(vote9_2), int(vote9_3)
            if (vote9_1 == vote9_2) or (vote9_2 == vote9_3) or (vote9_3 == vote9_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote9_2 or vote9_3 or vote9_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote9_1, vote9_2, vote9_3



def elektor10():
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    while True:
        vote10_1 = input('kandydat nr 1 - Adam Nowak: ')
        vote10_2 = input('kandydat nr 2 - Anna Woda: ')
        vote10_3 = input('kandydat nr 3 - Kamil Pol: ')

        if vote10_2 in ['1', '2', '3'] and vote10_3 in ['1', '2', '3'] and vote10_1 in ['1', '2', '3']:
            vote10_1, vote10_2, vote10_3 = int(vote10_1), int(vote10_2), int(vote10_3)
            if (vote10_1 == vote10_2) or (vote10_2 == vote10_3) or (vote10_3 == vote10_1):
                print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
                continue
            if (vote10_2 or vote10_3 or vote10_1) not in [1, 2, 3]:
                print('Podano błędną wartość!')
                continue
            else:
                 break
        else:
            print('Podano błędną wartość!')
            continue

    return vote10_1, vote10_2, vote10_3


candidate_Adam = 0
candidate_Anna = 0
candidate_Kamil = 0
res = ''
print('Witaj w programie do głosowania!')
while res != 'STOP':
    print('==========MENU==========')
    print('Jestem glosujacym nr 1')
    print('Jestem glosujacym nr 2')
    print('Jestem glosujacym nr 3')
    print('Jestem glosujacym nr 4')
    print('Jestem glosujacym nr 5')
    print('Jestem glosujacym nr 6')
    print('Jestem glosujacym nr 7')
    print('Jestem glosujacym nr 8')
    print('Jestem glosujacym nr 9')
    print('Jestem glosujacym nr 10')
    print('Aby zakończyć program wpisz STOP')
    choose = input('Podaj swoj numer glosujacego: ')
    if choose == '1':
        v1_1, v1_2 , v1_3 = elektor1()
        candidate_Adam += v1_1-1
        candidate_Anna += v1_2-1
        candidate_Kamil += v1_3-1

    if choose == '2':
        v2_1, v2_2, v2_3 = elektor2()
        candidate_Adam += v2_1-1
        candidate_Anna += v2_2-1
        candidate_Kamil += v2_3-1

    if choose == '3':
        v3_1, v3_2, v3_3 = elektor3()
        candidate_Adam += v3_1-1
        candidate_Anna += v3_2-1
        candidate_Kamil += v3_3-1
    if choose == '4':
        v4_1, v4_2, v4_3 = elektor4()
        candidate_Adam += v4_1-1
        candidate_Anna += v4_2-1
        candidate_Kamil += v4_3-1

    if choose == '5':
        v5_1, v5_2, v5_3 = elektor5()
        candidate_Adam += v5_1-1
        candidate_Anna += v5_2-1
        candidate_Kamil += v5_3-1

    if choose == '6':
        v6_1, v6_2, v6_3 = elektor6()
        candidate_Adam += v6_1-1
        candidate_Anna += v6_2-1
        candidate_Kamil += v6_3-1

    if choose == '7':
        v7_1, v7_2, v7_3 = elektor7()
        candidate_Adam += v7_1-1
        candidate_Anna += v7_2-1
        candidate_Kamil += v7_3-1

    if choose == '8':
        v8_1, v8_2, v8_3 = elektor8()
        candidate_Adam += v8_1-1
        candidate_Anna += v8_2-1
        candidate_Kamil += v8_3-1

    if choose == '9':
        v9_1, v9_2, v9_3 = elektor9()
        candidate_Adam += v9_1-1
        candidate_Anna += v9_2-1
        candidate_Kamil += v9_3-1

    if choose == '10':
        v10_1, v10_2, v10_3 = elektor10()
        candidate_Adam += v10_1-1
        candidate_Anna += v10_2-1
        candidate_Kamil += v10_3-1

    if choose.upper() == 'STOP':
        break




candidates = {'Adam Nowak': candidate_Adam , 'Anna Woda': candidate_Anna,  'Kamil Pol': candidate_Kamil}
print(candidates)
