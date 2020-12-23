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


candidate_Adam = 0
candidate_Anna = 0
candidate_Kamil = 0
def elektor1():
    global candidate_Adam, candidate_Anna, candidate_Kamil

    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote1_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote1_2 = input('kandydat nr 2 - Anna Woda: ')
    vote1_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote1_1, vote1_2, vote1_3 = int(vote1_1), int(vote1_2), int(vote1_3)

    if (vote1_1 == vote1_2) or (vote1_2 == vote1_3) or (vote1_3 == vote1_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote1_2 or vote1_3 or vote1_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote1_1 - 1)
        candidate_Anna += (vote1_2 - 1)
        candidate_Kamil += (vote1_3 - 1)



def elektor2():
    global candidate_Adam, candidate_Anna, candidate_Kamil

    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote2_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote2_2 = input('kandydat nr 2 - Anna Woda: ')
    vote2_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote2_1, vote2_2, vote2_3 = int(vote2_1), int(vote2_2), int(vote2_3)
    if (vote2_1 == vote2_2) or (vote2_2 == vote2_3) or (vote2_3 == vote2_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote2_2 or vote2_3 or vote2_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote2_1 -1 )
        candidate_Anna += (vote2_2 -1)
        candidate_Kamil += (vote2_3 -1)


def elektor3():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print('Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote3_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote3_2 = input('kandydat nr 2 - Anna Woda: ')
    vote3_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote3_1, vote3_2, vote3_3 = int(vote3_1), int(vote3_2), int(vote3_3)

    if (vote3_1 == vote3_2) or (vote3_2 == vote3_3) or (vote3_3 == vote3_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote3_2 or vote3_3 or vote3_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote3_1 - 1)
        candidate_Anna += (vote3_2 - 1)
        candidate_Kamil += (vote3_3 - 1)



def elektor4():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote4_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote4_2 = input('kandydat nr 2 - Anna Woda: ')
    vote4_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote4_1, vote4_2, vote4_3 = int(vote4_1), int(vote4_2), int(vote4_3)

    if (vote4_1 == vote4_2) or (vote4_2 == vote4_3) or (vote4_3 == vote4_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote4_2 or vote4_3 or vote4_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote4_1 - 1)
        candidate_Anna += (vote4_2 - 1)
        candidate_Kamil += (vote4_3 - 1)



def elektor5():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote5_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote5_2 = input('kandydat nr 2 - Anna Woda: ')
    vote5_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote5_1, vote5_2, vote5_3 = int(vote5_1), int(vote5_2), int(vote5_3)

    if (vote5_1 == vote5_2) or (vote5_2 == vote5_3) or (vote5_3 == vote5_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote5_2 or vote5_3 or vote5_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote5_1 - 1)
        candidate_Anna += (vote5_2 - 1)
        candidate_Kamil += (vote5_3 - 1)



def elektor6():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote6_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote6_2 = input('kandydat nr 2 - Anna Woda: ')
    vote6_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote6_1, vote6_2, vote6_3 = int(vote6_1), int(vote6_2), int(vote6_3)

    if (vote6_1 == vote6_2) or (vote6_2 == vote6_3) or (vote6_3 == vote6_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote6_2 or vote6_3 or vote6_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote6_1 - 1)
        candidate_Anna += (vote6_2 - 1)
        candidate_Kamil += (vote6_3 - 1)



def elektor7():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote7_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote7_2 = input('kandydat nr 2 - Anna Woda: ')
    vote7_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote7_1, vote7_2, vote7_3 = int(vote7_1), int(vote7_2), int(vote7_3)

    if (vote7_1 == vote7_2) or (vote7_2 == vote7_3) or (vote7_3 == vote7_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote7_2 or vote7_3 or vote7_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote7_1 - 1)
        candidate_Anna += (vote7_2 - 1)
        candidate_Kamil += (vote7_3 - 1)




def elektor8():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote8_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote8_2 = input('kandydat nr 2 - Anna Woda: ')
    vote8_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote8_1, vote8_2, vote8_3 = int(vote8_1), int(vote8_2), int(vote8_3)

    if (vote8_1 == vote8_2) or (vote8_2 == vote8_3) or (vote8_3 == vote8_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote8_2 or vote8_3 or vote8_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote8_1 - 1)
        candidate_Anna += (vote8_2 - 1)
        candidate_Kamil += (vote8_3 - 1)



def elektor9():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote9_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote9_2 = input('kandydat nr 2 - Anna Woda: ')
    vote9_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote9_1, vote9_2, vote9_3 = int(vote9_1), int(vote9_2), int(vote9_3)

    if (vote9_1 == vote9_2) or (vote9_2 == vote9_3) or (vote9_3 == vote9_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote9_2 or vote9_3 or vote9_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote9_1 - 1)
        candidate_Anna += (vote9_2 - 1)
        candidate_Kamil += (vote9_3 - 1)



def elektor10():
    global candidate_Adam, candidate_Anna, candidate_Kamil
    print(
            'Wskaż w skali od 1 do 3 (gdzie 3 oznacza najbardziej przypadł mi do gustu) jak mocno przypadł Ci do gustu : ')
    vote10_1 = input('kandydat nr 1 - Adam Nowak: ')
    vote10_2 = input('kandydat nr 2 - Anna Woda: ')
    vote10_3 = input('kandydat nr 3 - Kamil Pol: ')
    vote10_1, vote10_2, vote10_3 = int(vote10_1), int(vote10_2), int(vote10_3)

    if (vote10_1 == vote10_2) or (vote10_2 == vote10_3) or (vote10_3 == vote10_1):
        print('Nie można dopasowac takich samych preferencji do kilku kandydatów!')
    if (vote10_2 or vote10_3 or vote10_1) not in [1, 2, 3]:
        print('Podano błędną wartość!')
    else:
        candidate_Adam += (vote10_1 - 1)
        candidate_Anna += (vote10_2 - 1)
        candidate_Kamil += (vote10_3 - 1)



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
        elektor1()
    if choose == '2':
        elektor2()
    if choose == '3':
        elektor3()
    if choose == '4':
        elektor4()
    if choose == '5':
        elektor5()
    if choose == '6':
        elektor6()
    if choose == '7':
        elektor7()
    if choose == '8':
        elektor8()
    if choose == '9':
        elektor9()
    if choose == '10':
        elektor10()
    if choose == 'STOP':
        break




candidates = {'Adam Nowak': candidate_Adam , 'Anna Woda': candidate_Anna,  'Kamil Pol': candidate_Kamil}
print(candidates)
