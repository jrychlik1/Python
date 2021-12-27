from time import time
from random import randint

def calc(n1, n2, n):
    if n == 0:
        pass
    else:
        newN = n1 + n2
        n1 = n2
        n2 = newN
        print(n2, end=", ")
        calc(n1, n2, n-1)

def zadanie1r():
    print('Rekurencja:')
    n = int(input('Podaj liczbę: '))
    t1 = time()
    if n == 0:
        print('0')
    elif n >= 1:
        n1 = 0
        n2 = 1
        calc(n1, n2, n)
    else:
        print('Podaj liczbę większą bądź równą 0')
    t2 = time()
    print('\nCzas działania programu: {}'.format(t2-t1))

def zadanie1n():
    print('Iteracja:')
    n = int(input('Podaj liczbę: '))
    t1 = time()
    if n == 0:
        print('0')
    elif n >= 1:
        n1 = 0
        n2 = 1
        print('0, 1', end=', ')
        for i in range(2, n + 1):
            newN = n1 + n2
            if n1 == min(n1, n2):
                n1 = newN
            else:
                n2 = newN
            print(max(n1, n2), end=', ')
    t2 = time()
    print('\nCzas działania programu: {}'.format(t2 - t1))

def zadanie2(listNumber):
    n = len(listNumber)
    for i in range(1, n):
        key = listNumber[i]
        j = i - 1
        while j >= 0 and listNumber[j] > key:
            listNumber[j+1] = listNumber[j]
            listNumber[j] = key
            j -= 1

    return listNumber

def zadanie3(numbers):
    n = len(numbers)
    while n > 1:
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n -= 1
    return numbers

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 3')

    if exercise == 1:
        zadanie1r()
        zadanie1n()
    elif exercise == 2:
        n = 100
        for i in range(3):
            listNumber = []
            for j in range(n):
                number = randint(0, 20)
                listNumber.append(number)
            n += 100
            t1 = time()
            l = zadanie2(listNumber)
            t2 = time()
            t = t2 - t1
            print(l)
            print('Czas działania programu {}'.format(t))
    elif exercise == 3:
        n = 100
        for i in range(3):
            listNumber = []
            for j in range(n):
                number = randint(0, 20)
                listNumber.append(number)
            n += 100
            t1 = time()
            l = zadanie3(listNumber)
            t2 = time()
            t = t2 - t1
            print(l)
            print('Czas działania programu {}'.format(t))
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()
