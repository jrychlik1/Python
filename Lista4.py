from sys import argv
from numpy import prod
from math import pi
from itertools import permutations
from colorsys import rgb_to_hsv
from math import factorial

def zadanie1():

    print('Zad. 1')
    print('\n' + '***' + '\n')
    lst = []

    my_list = int(input('Podaj ilość elementów listy:'))
    for i in range (0, my_list):
        final_list = int(input())
        lst.append(final_list)


    print('Suma elementów listy: ' , sum(lst))
    print('Iloczyn elementów listy: ' , prod(lst))



def zadanie2():

    print('Zad. 2')
    print('\n' + '***' + '\n')

    aqls = []
    qls = []

    lista = int(input('Podaj ilość elementów listy:' ))
    for w in range(0, lista):
        almost_list = int(input())
        aqls.append(almost_list)

    for k in range (0, lista):
        g = aqls[k]
        if g not in qls:
           qls.append(g)

    print('Lista z usuniętymi powtarzającymi się elementami: ' , qls)


def zadanie3():

    print('Zad. 3')
    print('\n' + '***' + '\n')

    stat = '' 
    cond = 'Yy'
    number = int(input('Podaj liczbę stopni lub radianów: '))

    Stat = str(input('Jeśli chcesz zamienić stopnie na radiany wprowadź Y i zatwierdź klawiszem enter. Jeśli radiany na stopnie - wprowadź dowolny znak: '))
    
    if Stat == 'y' or Stat == 'Y' :
        final_number = number * pi / 180
        print('Po zamianie stopni na radiany: ', final_number)
    else:
        final_number = number * 180 / pi
        print('Po zamianie radiany na stopnie: ', final_number)
            


def zadanie4():
    
    print('Zad. 4')
    print('\n' + '***' + '\n')

    while True:
        n = int(input('Wprowadź numer elementu ciągu: '))
        if n >= 1:
            break
        else:
            print('Liczba nie może być mniejsza od 1.')

    a1 = int(input('Wartość pierwszego elementu ciągu: '))
    q = int(input('Wartość iloczynu ciągu geometrycznego: '))

    n1 = a1 * (q ** (n-1))
    print('N−ty element ciągu geometrycznego wynosi: ', n1)


def zadanie5():

    print('Zad. 5')
    print('\n' + '***' + '\n')
    almost_list = []

    lista = int(input('Podaj ilość elementów listy:' ))
    for w in range(0, lista):
        lister = int(input())
        almost_list.append(lister)


    if len(almost_list) > 1:
        for per in list(permutations(almost_list)):
            print(per)
    else:
        print('Nie podano listy')
    

def zadanie6():

    print('Zad. 6')
    print('\n' + '***' + '\n')

    r = int(input('Podaj wartość r: '))
    g = int(input('Podaj wartość g: '))
    b = int(input('Podaj wartość b: '))

    print('HSV: %s, %s, %s' % rgb_to_hsv(r, g, b))


def zadanie7():

    print('Zad. 7')
    print('\n' + '***' + '\n')

    number = int(input('Podaj liczbę n wierszy trójkąta Pascala: '))

    if number >= 1:
        result = []

        for num in range(number):
            row = []

            for element in range(num + 1):
                row.append(int((factorial(num)) / ((factorial(element)) * factorial(num - element))))
            result.append(row)

        for row in result:
            for r in row:
                print(r, end=' ')
            print()
    else:
        print('Liczba wierszy musi być większa od 0')


def zadanie8():

    print('Zad. 8')
    print('\n' + '***' + '\n')

    number = int(input('Podaj liczbę n-tego elementu ciągu harmonicznego: '))
    if number > 0:
        result = 0
        for i in range(1, number + 1):
            result += 1 / (i)
        print(result)
    else:
        print('Wartość musi być większa niż 0')



def zadanie9():

    print('Zad. 9')
    print('\n' + '***' + '\n')


    while True:
        number = int(input('Podaj liczbę całkowitą większą od 0: '))
        if number > 0:
            print(factorial(number))
            break
        else:
            print('Liczba musi być większa niż 0')

def eukli(a,b):
    if a== 0 or b == 0:
        number = max(a,b)
        print('Największy wspólny dzielnik to:', number)
    else:
        eukli((b%a),a)



def zadanie10():

    print('Zad. 10')
    print('\n' + '***' + '\n')

    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))

    if a >= 0 and b >= 0:
        eukli(a,b)
    else:
        print('Obie liczby muszą być liczbami naturalnymi')




def main():
    work = False
    while not work:
        try:
            zadanie = int(input('Podaj numer zadania i zatwierdź klawiszem enter: '))
            work = True
        except ValueError:
            print('Numer zadania musi zawierać się w przedziale 1-10')

    if zadanie == 1:
        zadanie1()

    elif zadanie==2:
        zadanie2()
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