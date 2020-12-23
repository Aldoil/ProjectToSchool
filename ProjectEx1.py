"""
ZADANIE 1. (15 punktów)
Napisz program, który stworzy przemówienie na podstawie ściągi zebraniowej. W czterech zbiorach informacyjnych
(słownikach, listach, krotkach, nawet w plikach jak ktoś da radę – zależy to od waszej inwencji)
program odgórnie przechowuje części zdania z każdej podgrupy. Użytkownik w ramach działania programu ma mieć następujące funkcjonalności:
1) Dodanie następnego zdania – program ma pobrać losowy element z kolejnych zbiorów i połączyć je według wzoru:
element z listy nr 1 + element z listy nr 2 itd. (losowe mają być elementy z list, a nie kolejność ich łączenia!).
Całe przemówienie ma znaleźć się w osobnym pliku o rozszerzeniu .txt.
2) Wyświetlanie całego przemówienia
3) Usuwanie zdania z przemówienia
4) Usuwanie całego przemówienia
"""
import random

column_1 = ['Koleżanki i koledzy ', 'z drugiej strony ', 'podobnie ', 'nie zapominajmy jednak, że ', 'w ten sposób ', 'praktyka dnia codziennego dowodzi, że ',
          'wagi i znaczenia tych problemów nie trzeba szerzej udowadniać, ponieważ ', 'różnorakie i bogate doświadczenia ', 'troska organizacji a szególnie ',
          'wyższe zalożenia ideowe, a także ' ]

column_2 = ['realizacja nakreślonych zadań programowych ', 'zakres i miejsca szkolenia kadr ', 'stały wzrost ilości i zakres naszej aktywności ',
          'aktualna struktura organizacji ', 'nowy model działalności organizacyjnej ', 'dalszy rozwój różnych form działalności ',
          'stałe zabezpieczenie informacyjno-propagandowe naszej działalności ', 'wzmocnienie i rozwijanie struktur ',
          'konsultacja z szerokim aktywem ', 'rozpoczęcie powszechnej akcji kształtowania postaw ']

column_3 = ['zmusza nas do przeanalizowania ', 'spełnia istotną rolę w kształtowaniu ', 'wymaga sprecyzowania i określania ', 'pomaga w przygotowaniu i realizacji ',
          'zabezpiecza udział szerokiej grupie w kształtowaniu ', 'spełnia ważne zadania w wypracowaniu ', 'umożliwia w większym stopniu tworzenie ',
          'powoduje docenianie wagi ', 'przedstawia interesującą próbę sprawdzenia ', 'pociąga za sobą proces wdrażania i unowo-cześniania']

column_4 = ['istniejących warunków administracyjno-finansowych', 'dalszych kierunków rozwoju', 'systemu powszechnego uczestnictwa',
          'postaw uczestników wobec zadań stawianych przez organizację', 'nowych propozycji', 'kierunków postępowego wychowania',
          'systemu szkolenia kadry odpowiadającego potrzebom', 'odpowiednich warunków aktywizacji', 'modelu rozwoju', 'form oddziaływania']

create_file = open('speech.txt', 'w')
create_file.write('Przemówienie!\n')
create_file.close()

def make_sentence(variable):
    while variable == '1':
        file = open('speech.txt', 'a')
        sentence = (random.choice(column_1)).capitalize() + random.choice(column_2) + random.choice(column_3) + random.choice(column_4) + '.'

        file.write(sentence + '\n')
        print('Dodano zdanie to pliku!')
        what_next = input('Czy chcesz dodać kolejne zdanie? t/n?')
        if what_next == 't':
            variable = '1'
            continue
        elif (what_next == 'n'):
            file.close()
            break
        else:
            print(f'Podana wartość {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            file.close()
            break


def show_speech(variable):
    while variable == '2':
        file = open('speech.txt')
        for lines in file.readlines():
            print(lines)

        what_next = input('Czy chcesz powrocic do menu? t/n?')
        if what_next == 't':
            file.close()
            break
        if what_next == 'n':
            variable = '2'
            continue
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            file.close()
            break


def del_sentence(variable):
    while variable == '3':
        file = open('speech.txt')
        res = []
        for lines in file.readlines():
            res.append(lines)
        file.close()

        delete = input('Które zadnie chcesz usunąć? Podaj numer: ')
        sentence = res[(int(delete))]
        res.remove(sentence)

        file = open('speech.txt', 'w')
        file.writelines(res)
        file.close()

        what_next = input('Usunięto zdanie, czy chcesz usunąć kolejne? t/n?')
        if what_next == 't':
            variable = '3'
            continue
        elif what_next == 'n':
            break

        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break


def del_speech(variable):
    while variable == '4':
        file = open('speech.txt', 'w')
        file.write('Przemówienie!\n')
        file.close()

        what_next = input('Czy chcesz powrocic do menu? t/n?')
        if what_next == 't':
            break
        elif what_next == 'n':
            variable = '4'
            continue
        else:
            print(f'Podana wartosc {what_next} jest nieprawidłowa. Zostajesz przeniesiony do menu.')
            break


option = ''
while option != '5':
    print('    Witam w programie   ')
    print('==========MENU==========')
    print('1. Dodaj losowe zdanie na podstawie ściągi zbiorowej do przemówienia. ')
    print('2. Wyświetl przemówienie. ')
    print('3. Usuń wybrane zdanie z przemówienia. ')
    print('4. Usuń wszystkie zdania z przemówienia. ')
    print('5. Wyjdz z programu.')
    option = input('Wybierz co chcesz zrobić: ')
    if option == '1':
        make_sentence('1')
    if option == '2':
        show_speech('2')
    if option == '3':
        del_sentence('3')
    if option == '4':
        del_speech('4')
    elif option not in ['1', '2', '3', '4', '5']:
        print('BLAD')
        continue

#DODAC JUTRO ABY ZDANIA ZACZYNALY SIE Z DUZEJ I KONCZYLY KROPKA