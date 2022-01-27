from math import pi
from itertools import chain, combinations
import xml.etree.ElementTree as ET

class Kolo(object):
    def __init__(self, r):
        self.r = r

    def pole(self):
        p = pi * (self.r ** 2)
        p = round(p, 2)
        return p

    def obwod(self):
        obw = 2 * pi * self.r
        obw = round(obw, 2)
        return obw

class Zadanie2(object):
    def __init__(self, iterable):
        self.iterable = iterable

    def __str__(self):
        return 'Zadanie 2'

    def comb(self):
        return chain.from_iterable(combinations(self.iterable, n) for n in range(len(self.iterable) + 1))

class Zadanie3(object):
    def __init__(self, numberList):
        self.numberList = numberList

    def __str__(self):
        return 'Zadanie 3'

    def subsets(self):
        result = []
        for id, element in enumerate(self.numberList):
            try:
                for i, el in enumerate(self.numberList[id + 1:]):
                    try:
                        for n in self.numberList[id + i + 2:]:
                            if element + el + n == 0:
                                result.append([element, el, n])
                    except IndexError:
                        continue
            except IndexError:
                continue
        return result

class ExchangeRates(object):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return 'Zadanie 4\nKurs Walut'

    def availableRates(self):
        try:
            root = ET.parse(self.path).getroot()
            namesOfCurrency = []
            for value in root.findall('pozycja/nazwa_waluty'):
                namesOfCurrency.append(value.text)
            return namesOfCurrency
        except FileNotFoundError:
            return 'Nie znaleziono podanego pliku'

    def findValue(self, value):
        root = ET.parse(self.path).getroot()
        for v in root.findall('pozycja'):
            for n in v.findall('nazwa_waluty'):
                if n.text == value:
                    for c in v.findall('kurs_sredni'):
                        return c.text

    def convertPLN(self):
        ar = self.availableRates()
        money = int(input('Podaj kwotę do konwertowania: '))
        nameOfCurrency = input('Podaj nazwę waluty do konwertowania: ')

        if nameOfCurrency in ar and type(ar) == list:
            value = float(self.findValue(nameOfCurrency))

            while True:
                choice = input('Jeśli chcesz konwertować na PLN wpisz 1, a jeśli z PLN wpisz 2: ')

                if choice == '1':
                    return round(money * value, 2)
                elif choice == '2':
                    return round(money / value, 2)
                else:
                    print('Nie ma takiej opcji!')
        else:
            return "Podano złą walutę!"

    def convert(self):
        ar = self.availableRates()
        money = int(input('Podaj kwotę do konwertowania: '))
        first = input('Podaj nazwę waluty, którą posiadasz: ')

        if first in ar and type(ar) == list:
            second = input('Podaj nazwę waluty, którą chcesz: ')

            if second in ar and type(ar) == list:
                money *= float(self.findValue(first))
                money /= float(self.findValue(second))
                return round(money, 2)
            else:
                return "Podano złą walutę!"
        else:
            return "Podano złą walutę!"

    def menu(self):
        while True:
            print('\nDostępne opcje:')
            print('0. Zakończ')
            print('1. Lista dostępnych kursów')
            print('2. Konwersja dowolnej waluty na PLN')
            print('3. Konwersja wybranej waluty na wybraną walute')
            choice = input('Wybierz opcje: ')
            print()

            if choice == '0':
                break
            elif choice == '1':
                namesOfCurrency = self.availableRates()
                if type(namesOfCurrency) == list:
                    print('Lista dostępnych kursów:')
                    for element in namesOfCurrency:
                        print(element)
                else:
                    print(namesOfCurrency)
            elif choice == '2':
                print(self.convertPLN())
            elif choice == '3':
                print(self.convert())
            else:
                print('Nie ma takiej opcji!')

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 4!')

    if exercise == 1:
        print('Zadanie 1')
        try:
            r = float(input('Podaj promień koła: '))
        except:
            r = 0
        kolo = Kolo(r)
        print('Pole koła: {}'.format(kolo.pole()))
        print('Obwód koła: {}'.format(kolo.obwod()))

    elif exercise == 2:
        zadanie2 = Zadanie2([1, 2, 3])
        print(zadanie2)
        print(list(zadanie2.comb()))

    elif exercise == 3:
        zadanie3 = Zadanie3([-1, 1, 0, 3, 5, -5])
        print(zadanie3)
        print(zadanie3.subsets())

    elif exercise == 4:
        exchangeRates = ExchangeRates('C:\\Users\KOMPUTER\Desktop\Lista 10\waluty.xml')
        print(exchangeRates)
        exchangeRates.menu()
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()