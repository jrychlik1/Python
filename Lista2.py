from math import exp
from itertools import chain

def zadanie1():

    print('Zad. 1')

    print('\n' + '***' + '\n')
    print(20 * ('%s\n' % (1.2 * exp(1) + 3 + 34.5)))
    print('***' + '\n')

def zadanie2():

    print('Zad. 2')

    text = input('Podaj dowolny tekst - program wyświetli go 30-krotnie:') + '\n'
    print('\n' + '***' + '\n')
    print(30 * text)
    print('***' + '\n')

def zadanie3():

    print('Zad. 3')

    print('\n' + 'Podaj dowolny tekst - program utworzy nowy tekst')
    textin = input('składający się z jego dwóch pierwszych i ostatnich znaków:')
    textout = textin[:2] + textin[-2:]
    print('\n' + '***' + '\n')
    print(textout +'\n')
    print('***' + '\n')

def zadanie5():

    print('Zad. 5')

    textin = input('\n' + 'Wprowadź dowolny wyraz - program wstawi w jego środek drugi wprowadzony wyraz: ')
    textin2 = input('Podaj drugi wyraz: ')
    mid = int(len(textin) / 2)
    print('\n' + '***')
    textout = textin[:mid] + textin2 + textin[mid:]
    print('\n' + 'Z podanych wyrazów został utworzony nowy wyraz:' + '\n')
    print(textout)
    print('\n' + '***' + '\n')

def zadanie6():

    print('Zad. 6' + '\n')

    lista = [ 'Kasia', 'Basia', 'Marek', 'Darek' ]
    lista.append('Józek')
    lista.extend([ 'Ania', 'Basia'] )
    lista.sort()

    print('Czwarty student na liście to: ', lista[3], '\n')
    print('Dwójka pierwszych studentów to: ', lista[:2], '\n')
    print('Dwójka ostatnich studentów to: ', lista[-2:], '\n')

    while 'Basia' in lista:
        lista.remove('Basia')

    print('Ilość studentów: ', len(lista), '\n')

    krotka = tuple(lista)
    print('Krotka: ', krotka)
    print('\n' + '***' + '\n')

def zadanie7():

    print('Zad. 7' + '\n')

    print('***' + '\n')
    print('Uporządkowana lista po drugim elemencie:' + '\n')
    lista = [(2, 8), (5, 5), (9, 3), (1, 0),(3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
    lista = sorted(lista, key=lambda x:x[1])

    print(lista)
    print('\n' + '***' + '\n')

def zadanie8():

    print('Zad. 8' + '\n')

    letters = ['K', 'R', 'O', 'K', 'O', 'D', 'Y', 'L']
    word = ' '.join(letters)
    #lub bez spacji:
    #word = ''.join(letters)
    print('Utworzony wyraz: ' + word)

def zadanie9():

    print('Zad. 9' + '\n')

    lista1 = [2, 4, 3], [1, 5, 6], [9], [7, 9, 0]
    print('Lista początkowa:', '\n', lista1,'\n')
    
    lista2 = list(chain([2, 4, 3], [1, 5, 6], [9], [7, 9, 0]))
    print('Lista po obniżeniu stopnia zagnieżdżenia:' + '\n')
    print(lista2, '\n')

def zadanie10():

    print('Zad. 10' + '\n')

    print('***' + '\n')

    lista = []
    for number in range(3, 100, 3):
        lista.append(number)

    print('Wielokrotności liczby 3 < 100: ', '\n', lista, '\n')

    for num in range(4, len(lista), 2):
        try:
            del lista[num]
        except:
            break
    print('Usunięto co trzeci element (>5): ', '\n', lista, '\n')

    aryt = sum(lista) / len(lista)
    print('Zaokrąglona średnia arytmetyczna listy: ', '\n', round(aryt), '\n')

def zadanie4():

    print('Zad. 4:' + '\n')

    textin = input('Wprowadź tekst: ')
    textout = ''

    for signs in range(len(textin)):
        if signs == 0:
            textout += textin[0]
            continue
        elif textin[signs] == textin[0].lower():
            textout += '$'
        elif textin[signs] == textin[0].upper():
            textout += '$'
        else:
            textout += textin[signs]
    print('\n', 'Tekst po zamianie znaków: ', textout, '\n')





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