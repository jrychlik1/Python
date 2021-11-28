import builtins
import numpy
from math import sin, pi, floor
from numpy import angle, conjugate
from cmath import sqrt, sin as sinz, cos
from numpy import real, imag

def zadanie1():
    print('Zadanie 1:')
    print('Podaj 2 cyfry')

    a = input()
    b = input()
    suma = a + b
    print('Suma wynosi: ' + suma + '\n')
    print('Funkcja input pobiera wartości w formie ciągu znaków,')
    print('więc zmienna b jest dopisana do końca zmiennej a.')
    print(' ')

def zadanie2():
    print('Zadanie 2:')

    a = 3
    b = 4
    alfa = 47
    result = 0.5 * a * b * round(sin(alfa * pi / 180), 4)
    print('Pole trójkąta wynosi: %s' % round(result, 4))

def zadanie3():
    print('Zadanie 3:')

    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    alfa = int(input("Podaj wartość kąta alfa: "))
    result = 0.5 * a * b * round(sin(alfa * pi / 180), 4)
    print('Pole trójkąta wynosi: %s' % round(result, 4))

def zadanie4():
    print('Zadanie 4:')

    print(dir(builtins))
    print(help(print))

    print('Ala ma kota')
    print(2 + 2)
    print('%s\t%s\t%s\t%s' % (2**5, 35//2, 35/2, 35%2))
    print('%s\n%s\n%s\n%s' % (2**5, 35//2, 35/2, 35%2))

def zadanie5():
    print('Zadanie 5:')

    print('5 // 2 = %s' % (5 // 2))
    print('// - dzięki tej operacji otrzymujemy wynik dzielenia bez reszty\n')

    print('round(5 / 2) = %s' % (round(5 / 2)))
    print('round(1.7) = %s' % (round(2.6)))
    print('round - zaokrągla liczbę\n')

    print('floor(5 / 2) = %s' % (floor(5 / 2)))
    print('floor(1.7) = %s' % (floor(2.6)))
    print('floor - zaorągla liczbę (w dół)')

def zadanie6():
    print('Zadanie 6:')

    print('Wartość pierwiastka drugiego stopnia z liczby -17 wynosi: %s' % sqrt(complex(-17)))

def zadanie7():
    print('Zadanie 7:')

    print('"Działanie zmienniej _ w trybie interaktywnym"')
    print('Zmienna _ w trybie interaktywnym służy do zapisywania ostatnio podanej wartości')
    print('Przykład:')
    print('>>> 5')
    print('5')
    print('>>> _ ** 2')
    print('25')

def zadanie8():
    print('Zadanie 8:')

    a = int(input('Podaj liczbę a: '))
    b = int(input('Podaj liczbę b (musi być mniejsza od wcześniej podanej wartości): '))

    if b < a:
        Z = b % a
        Z *= Z + 3

        print('Wynik działania: %s' % Z)
    else:
        print('Wartość liczby b musi być mniejsza od wartości liczby a.')

def zadanie9():
    print('Zadanie 9:')

    z = complex(input('Podaj liczbę: '))

   
    print('Wartość bezwzględna podanej liczby wynosi: %s' % abs(z))

    #print(angle(z))
    #print(conjugate(z))

def zadanie10():
    print('Zadanie 10:')

    z = complex(0, 1)
    zsin = sinz(z)
    zcos = cos(z)

    print('Część rzeczywista dla sin(i) wynosi: %s' % zsin.real)
    print('Część urojona dla sin(i) wynosi: %s' % zsin.imag)
    print('Część rzeczywista fla cos(i) wynosi: %s' % zcos.real)
    print('Część urojona dla cos(i) wynosi: %s \n' % zcos.imag)
    print('Zależność jest spełniona:')
    print('1 = %s \n' % (sinz(z)**2 + cos(z)**2))
    

    
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
