from os import chdir, getcwd, path, makedirs, listdir
from sys import exit
from pathlib import Path
from datetime import datetime
from re import search, findall
from random import randint

def save(content, endPath, n, info='zaszyfrowany'):
    chdir(endPath)
    dt = datetime.now()

    fileName = 'plik_{}{}_{}-{}-{}.txt'.format(info, n, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'))

    file = open(fileName, 'w', encoding='utf-8')
    file.write(content)
    file.close()

def change(i, move):
    letter = ['a', 'ą', 'b', 'c', 'ć', 'd',
              'e', 'ę', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'ł', 'm', 'n',
              'ń', 'o', 'ó', 'p', 'q', 'r',
              's', 'ś', 't', 'u', 'w', 'x',
              'y', 'z', 'ż', 'ź']

    if i in letter:
        ind = letter.index(i)
        ind += move
        if ind >= len(letter):
            ind = ind - len(letter)
        i = letter[ind]

    return i

def size(fileName, move):
    file = open(fileName, 'r', encoding='utf-8')

    result = ''
    for line in file.readlines():
        for i in line:
            if i.isupper():
                i = change(i.lower(), move)
                i = i.upper()
            else:
                i = change(i, move)

            result += str(i)

    file.close()
    return result

def checkFile(filePath):
    fileName = Path(filePath).name
    chdir(path.dirname(filePath))

    if path.exists(fileName):
        return fileName
    else:
        print('Nie istnieje taki plik!')
        return False

def zadanie1():
    filePath = input('Podaj ścieżkę do pliku txt: ')

    try:
        move = int(input('Podaj przesunięcie (od 1 do 10): '))
    except ValueError:
        print('Nie podano liczby!')
        exit()

    if filePath[-4:] == '.txt':
        if move >= 1 and move <= 10:
            if path.exists(filePath):
                if checkFile(filePath):
                    result = size(checkFile(filePath), move)
                    endPath = input('Podaj ścieżkę do pliku zapisu: ')
                    if path.exists(endPath):
                        save(result, endPath, move)
                    else:
                        try:
                            makedirs(endPath)
                            save(result, endPath, move)
                        except:
                            print('Nieoczekiwany błąd!')
                            exit()
                else:
                    exit()
            else:
                print('Nie istnieje taki plik lub taka ścieżka do pliku!')
                exit()
        else:
            print('Podano liczbę spoza przedziału')
            exit()
    else:
        print('Nie podano pliku z rozszerzeniem \'.txt\'')

def findFile(filePath):
    for file in listdir(filePath):
        myFile = search('^plik_zaszyfrowany(\d)+_\d\d\d\d-\d\d-\d\d\.txt$', file)
        try:
            move = findall(r'\d', myFile.group())
            if len(move) == 10:
                move = int(move[0] + move[1])
            else:
                move = int(move[0])
            result = size(path.join(filePath, myFile.group()), -move)
            save(result, filePath, -move, info='deszyfrowany')
        except:
            continue

def zadanie2():
    filePath = input('Podaj ścieżkę do folderu z plikiem do odszyfrowania: ')
    try:
        if path.exists(filePath):
            findFile(filePath)
        else:
            print('Nie istnieje taka ścieżka')
    except NotADirectoryError:
        print('Podano ścieżkę do istniejącego pliku!')

def last_number(pesel):
    lastNumber = int(pesel[0]) + 3 * int(pesel[1]) + 7 \
                 * int(pesel[2]) + 7 * int(pesel[3]) + 7 \
                 * int(pesel[4]) + 7 * int(pesel[5]) + 7 \
                 * int(pesel[6]) + 7 * int(pesel[7]) + 7 \
                 * int(pesel[8]) + 7 * int(pesel[9])
    lastNumber %= 10
    lastNumber = 10 - lastNumber
    if lastNumber == 10:
        lastNumber = 0
    return str(lastNumber)

def generate_pesel():
    year = randint(1800, 2299)
    month = randint(1, 12)
    pesel = str(year)[-2:]

    if year < 1900:
        pesel += str(month + 80)
    elif year >= 1900 and year < 2000:
        if month < 10:
            pesel += '0' + str(month)
        else:
            pesel += str(month)
    elif year >= 2000 and year < 2100:
        pesel += str(month + 20)
    elif year >= 2100 and year < 2200:
        pesel += str(month + 40)
    else:
        pesel += str(month + 60)

    if month == 1 or month == 3 or month == 5 or \
            month == 7 or month == 8 or month == 10 or month == 12:
        day = randint(1, 31)
    elif month == 2:
        day = randint(1, 28)
    else:
        day = randint(1, 30)

    if day < 10:
        pesel += '0' + str(day)
    else:
        pesel += str(day)

    number = randint(0, 9999)

    if number < 10:
        pesel += '000' + str(number)
    if number < 100:
        pesel += '00' + str(number)
    if number < 1000:
        pesel += '0' + str(number)
    else:
        pesel += str(number)

    lastNumber = last_number(pesel)
    pesel += lastNumber

    return pesel

def zadanie3():
    file = open('PESEL.txt', 'w')
    for i in range(10):
        file.write(generate_pesel() + '\n')
    file.close()

def read_date(pesel):
    month = pesel[2:4]
    year = ''

    if month[0] == '0' or month[0] == '1':
        year = '19' + pesel[:2]
    elif month[0] == '2' or month[0] == '3':
        year = '20' + pesel[:2]
        month = int(month) - 20
    elif month[0] == '4' or month[0] == '5':
        year = '21' + pesel[:2]
        month = int(month) - 40
    elif month[0] == '6' or month[0] == '7':
        year = '22' + pesel[:2]
        month = int(month) - 60
    elif month[0] == '8' or month[0] == '9':
        year = '18' + pesel[:2]
        month = int(month) - 80

    day = pesel[-2:]

    return '{}-{}-{}'.format(day, month, year)

def zadanie4():
    try:
        content = []
        file = open('PESEL.txt')

        for line in file.readlines():
            if len(line[:-1]) == 11:
                lastNumber = last_number(line)
                if lastNumber == line[-2]:
                    plec = ''
                    date = read_date(line[0:6])

                    if int(line[-3]) % 2 == 0:
                        plec = 'Kobieta'
                    else:
                        plec = 'Meżczyzna'

                    content.append('nr PESEL:{}\n data urodzenia {};\t płeć: {}\n'.format(line[:-1], date, plec))
                else:
                    print('Pesel został źle zdefiniowany')
            else:
                print('Pesel został źle zdefiniowany')

        file.close()

        file = open('PESEL.txt', 'w')
        for c in content:
            file.write(c)
        file.close()
    except FileNotFoundError:
        print('Plik PESEL.txt nie istnieje')

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 4!')

    if exercise == 1:
        zadanie1()
    elif exercise == 2:
        zadanie2()
    elif exercise == 3:
        zadanie3()
    elif exercise == 4:
        zadanie4()
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()