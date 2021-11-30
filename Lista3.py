from math import sqrt
from re import compile, search

def zadanie1():

    print('Zad. 1')
    print('\n' + '***' + '\n')

    #spol = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z')
    samo = ('a', 'e', 'i', 'o', 'u', 'y')

    litera = input('Wprowadź literę (UWAGA - program nie obsługuje polskich znaków): ')
    if litera in samo:
        print('Litera >' + litera + '< to samogłoska.');
    else:
        print('Litera >' + litera + '< to spółgłoska.');

    print('\n' + '***' + '\n')


def zadanie2():

    print('Zad. 2')
    print('\n' + '***' + '\n')

    liczba = int(input('Wprowadź liczbę, aby sprawdzić czy jest parzysta lub nieparzysta: '))
    if liczba % 2 == 0:
        print('\n Liczba >', liczba,'< jest parzysta')
    else:
        print('\n Liczba >', liczba, '< jest nieparzysta \n')

    print('\n Ten sam program bez użycia IF można uruchomić wybierając zadanie "22"')
    print('\n' + '***' + '\n')


def zadanie22():

    print('Zad. 2-2')
    print('\n' + '***' + '\n')

    liczba = int(input('Wprowadź liczbę, aby sprawdzić czy jest parzysta lub nieparzysta: '))
    wynik = ('jest liczbą parzystą', 'jest liczbą nieparzystą')
    print('\n', liczba, wynik[liczba % 2], '\n')

    print('\n' + '***' + '\n')


def zadanie3():

    print('Zad. 3')
    print('\n' + '***' + '\n')

    print('Program służy do obliczenia pierwiastków równania kwadratowego.')
    print('Proszę o podanie wartości dla: a, b oraz c poniżej:' + '\n')

    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))

    if a == 0:
        print('\n' + 'Współczynnik a jest równy 0, wobec tego równanie NIE jest kwadratowe.')
        print('Program kończy działanie, miłego dnia.')

    else:
        delta = (b*b)-(4*a*c)

        if delta == 0:
            x0 = (-b)/(2*a)
            print('\n' + 'Miejsce zerowe danej funkcji kwadratowej to: %s' % x0)
            #np a=1 b=6 c=9

        elif delta < 0:
            print('\n' + 'Delta jest mniejsza od zera. Równanie nie ma rozwiązań wśród liczb R')
            #1 2 3

        else:
            x1 = round((-b)+sqrt(delta))/(2*a)
            x2 = round((-b)-sqrt(delta))/(2*a)
            print('\n' + 'Pierwiastkami danej funkcji są: %s v %s' % (x1, x2))
            #-1 3 4

    print('\n' + '***' + '\n')


def zadanie4():
    
    print('Zad. 4' + '\n')

    print('Pierwsza opcja:' + '\n')
    print('*            *        ****')
    print('*           * *       *   *')
    print('*          *   *      *   *')
    print('*         *******     ****')
    print('*        *       *    * *')
    print('*       *         *   *  *')
    print('*****  *           *  *   *', '\n')

    print('Druga opcja:')
    print('''
    *            *        ****
    *           * *       *   *
    *          *   *      *   *
    *         *******     ****
    *        *       *    * *
    *       *         *   *  *
    *****  *           *  *   *
    ''')


def zadanie5():

    print('Zad. 5')
    print('\n' + '***' + '\n')

    password = input('Wpisz hasło: ')
    reg = compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d@$#%*?&!]{6,16}$')
    if search(reg, password):
        print("Hasło spełnia wymagania")
    else:
        print("Hasło nie spełnia wymagań")

def zadanie6():

    print('Zad. 6')
    print('\n' + '***' + '\n')

    iin = int(input('Podaj liczbę: '))

    print('\n')
    print('Tablica mnożenia: \n')

    if iin > 0:
        print(' ', end=' ')

        for i in range(1, iin + 1):
            ij = str(i)
            print(ij.rjust(6), end=' ')
        print()

        for j in range(1, 11):
            print(str(j).rjust(2), end='')
            for i in range(1, iin + 1):
                wynik = str(i * j)
                print(wynik.rjust(6), end=' ')
            print()

def zadanie7():

    print('Zad. 7')
    print('\n' + '***' + '\n')

    N = int(input('Podaj ilość elementów ciągu Fibonacciego, jaka ma zostać wyświetlona: '))

    N1, N2 = 0, 1
    count = 0

    if N <= 0:
        print('\n' + 'Wartość musi być większa od zera.')

    elif N == 1:
        print('\n', N1)

    else:
       print('\n' + 'Kolejne elementy ciągu Fibonacciego:')
       while count < N:
           print('\n', N1)
           Nn = N1 + N2
           N1 = N2
           N2 = Nn
           count += 1

    print('\n' + '***' + '\n')


def zadanie8():

    print('Zad. 8')
    print('\n' + '***' + '\n')

    for cyfry in range(1, 10):
        print(str(cyfry) * cyfry)

    print('\n' + '***' + '\n')


def zadanie9():

    print('Zad. 9')
    print('\n' + '***' + '\n')

    m = int(input('Podaj liczbę wierszy: '))
    n = int(input('Podaj liczbę kolumn: '))
    print('\n')

    elementy = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):

        for j in range(n):
            elementy[i][j] = i*j

    for line in elementy:

        for num in line:
            print(num, end=' ')

        print()


def zadanie10():

    print('Zad. 10')
    print('\n' + '***' + '\n')

    lista = []
    for liczba in range(100, 401):
        cyfry = str(liczba)
        if '1' in cyfry or '3' in cyfry or '5' in cyfry or '7' in cyfry or '9' in cyfry:
            continue
        lista.append(cyfry)

    for x in lista:
        print(x, end=', ')





def main():
    work = False
    while not work:
        try:
            zadanie = int(input('Podaj numer zadania i zatwierdź klawiszem enter: '))
            work = True
        except ValueError:
            print('')

    if zadanie == 1:
        zadanie1()

    elif zadanie==2:
        zadanie2()
    elif zadanie==22:
        zadanie22()
    elif zadanie == 3:
        zadanie3()
    elif zadanie == 4:
        zadanie4()
    elif zadanie == 5:
        zadanie5()
    elif zadanie == 6:
        zadanie6()
    elif zadanie == 7:
        zadanie7()
    elif zadanie == 8:
        zadanie8()
    elif zadanie == 9:
        zadanie9()
    elif zadanie == 10:
        zadanie10()

if __name__ == '__main__':
    main()