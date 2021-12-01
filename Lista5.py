from sys import exit

def zadanie1():

    number = str(input('Podaj słowo do konwersji: '))

    first = {'jeden': 1, 'dwa': 2, 'trzy': 3, 'cztery': 4, 'pięć': 5,
             'sześć': 6, 'siedem': 7, 'osiem': 8, 'dziewięć': 9}
    second = {'dziesięć': 10, 'jedenaście': 11, 'dwanaście': 12,
             'trzynaście': 13, 'czternaście': 14, 'piętnaście': 15,
             'szesnaście': 16, 'siedemnaście': 17, 'osiemnaście': 18,
             'dziewiętnaście': 19}
    third = {'dwadzieścia': 2, 'trzydzieści': 3, 'czterdzieści': 4,
             'pięćdziesiąt': 5}
    numbers = []

    for n in number.split():
        numbers.append(n)

    if len(numbers) == 1:
        if number in first:
            print('Liczba:', first[number])
        elif number in second:
            print('Liczba:', second[number])
        elif number in third:
            print('Liczba:', third[number] * 10)
        else:
            print('Wprowadzona wartość jest błędna')
    elif len(numbers) == 2:
        if numbers[0] in third:
            if numbers[1] in first:
                print('Liczba:', int(str(third[numbers[0]]) + str(first[numbers[1]])))
            else:
                print('Wprowadzona wartość jest błędna')
        else:
            print('Wprowadzona wartość jest błędna')
    else:
        print('Wprowadzona wartość jest błędna')


def zadanie2():

    number = int(input('Podaj liczbę do konwersji: '))
    
    first = {'1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć',
             '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć', '0': ''}
    second = {'0': 'dziesięć', '1': 'jedenaście', '2': 'dwanaście',
              '3': 'trzynaście', '4': 'czternaście', '5': 'piętnaście',
              '6': 'szesnaście', '7': 'siedemnaście', '8': 'osiemnaście',
              '9': 'dziewiętnaście'}
    third = {'2': 'dwadzieścia', '3': 'trzydzieści', '4': 'czterdzieści',
             '5': 'pięćdziesiąt', '6': 'sześćdziesiąt', '7': 'siedemdziesiąt',
             '8': 'osiemdziesiąt', '9': 'dziewięćdziesiąt', '0': ''}
    fourth = {'1': 'sto', '2': 'dwieście', '3': 'trzysta', '4': 'czterysta',
              '5': 'pięćset', '6': 'sześćset', '7': 'siedemset', '8': 'osiemset',
              '9': 'dziewięćset', '0': ''}
    fifth = {'1': 'tysiąc'}
    result = ''

    if number > 0 and number < 2000:
        sNumber = str(number)

        if len(sNumber) < 5:
            # Sprawdzamy liczbę jedności
            if sNumber[-1] in first:
                # Zapisujemy liczbę jedności
                result += first[sNumber[-1]]
            else:
                 print('Wprowadzona wartość jest błędna')

            if len(sNumber) > 1:
                # Sprawdzamy liczbę dziesiątek
                if sNumber[-2] in third:
                    # Zapisujemy liczbę dziesiątek
                    if sNumber[-2] == '0':
                        pass
                    else:
                        result = '{} {}'.format(third[sNumber[-2]], result)
                elif sNumber[-2] == '1':
                    # Zapisujemy liczbę dziesiątek i jedności
                    if sNumber[-1] in second:
                        result = second[sNumber[-1]]
                else:
                     print('Wprowadzona wartość jest błędna')

                if len(sNumber) > 2:
                    # Sprawdzamy liczbę setek
                    if sNumber[-3] in fourth:
                        # Zapisujemy liczbę setek
                        if sNumber[-3] == '0':
                            pass
                        else:
                            result = '{} {}'.format(fourth[sNumber[-3]], result)
                    else:
                         print('Wprowadzona wartość jest błędna')

                    if len(sNumber) == 4:
                        # Sprawdzamy liczbę tysięcy
                        if sNumber[-4] in fifth:
                            #Zapisujemy liczbę tysięcy
                            result = '%s %s' % (fifth[sNumber[0]], result)
                        else:
                             print('Wprowadzona wartość jest błędna')
        else:
            return  print('Wprowadzona wartość jest błędna')
        print('Liczba:', result)
    else:
         print('Wprowadzona wartość jest błędna')

def create_num(myList, number):
    num = ''
    for i in myList:
        if i in number[0:4]:
            num = i
    return num

def check(numberR, numberA, number, result):
    if numberR in number[0:3]:
        result += numberA
        number = number.replace(numberR, '')
        value = False
    else:
        value = True
    return number, result, value



def zadanie3():


    first = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'IV': 4,
             'VI': 6, 'VII': 7, 'VIII': 8}
    second = {'X': 10, 'IX': 9, 'XX': 20, 'XXX': 30, 'L': 50, 'XL': 40,
              'LX': 60, 'LXX': 70, 'LXXX': 80}
    third = {'C': 100, 'XC': 90, 'CC': 200, 'CCC': 300, 'D': 500, 'CD': 400,
             'DC': 600, 'DCC': 700, 'DCCC': 800}
    fourth = {'M': 1000, 'CM': 900, 'MM': 2000, 'MMM': 3000}
    number = input('Podaj liczbę rzymską: ').upper()
    result = 0
    value_third = True
    value_second = True
    value_first = True

    if not number.count('V') > 1 and not number.count('L') > 1 and not number.count('D') > 1:

        num = create_num(fourth, number)
        if num:
            if len(num) == 1:
                if number[0] != 'M':
                    print('Podano złą wartość')
                    exit()
                else:
                    result += fourth[num]
                    number = number.replace(num, '')
                    if num != 'CM':
                        number, result, value_third = check('CM', 900, number, result)
            else:
                if number[0] != 'M' and number[0:2] != 'CM':
                    print('Podano złą wartość')
                    exit()
                else:
                    result += fourth[num]
                    number = number.replace(num, '')
                    if num != 'CM':
                        number, result, value_third = check('CM', 900, number, result)
                    else:
                        if len(number) > 1:
                            if number[0] == 'M':
                                number = number.replace('M', '')
                                result += 1000
                        value_third = False

        if value_third:
            num = create_num(third, number)
            if num:
                if len(num) == 1:
                    if number[0] != 'D' and number[0] != 'C':
                        print('Podano złą wartość')
                        exit()
                    else:
                        result += third[num]
                        number = number.replace(num, '')
                        if num != 'XC':
                            number, result, value_second = check('XC', 90, number, result)
                else:
                    if number[0] != 'D' and number[0] != 'C' and number[0:2] != 'XC':
                        print('Podano złą wartość')
                        exit()
                    else:
                        result += third[num]
                        number = number.replace(num, '')
                        if num != 'XC':
                            number, result, value_second = check('XC', 90, number, result)
                        else:
                            if len(number) > 1:
                                if number[0] == 'C':
                                    number = number.replace('C', '')
                                    result += 100
                            value_second = False
        else:
            if len(number) >= 2:
                if number[0:2] == 'XC':
                    result += 90
                    number = number[2:]
                    value_second = False

        if value_second:
            num = create_num(second, number)
            if num:
                if len(num) == 1:
                    if number[0] != 'L' and number[0] != 'X':
                        print('Podano złą wartość')
                        exit()
                    else:
                        result += second[num]
                        number = number.replace(num, '')
                        if num != 'IX':
                            number, result, value_first = check('IX', 9, number, result)
                else:
                    if number[0] != 'X' and number[0] != 'L' and number[0:2] != 'IX':
                        print('Podano złą wartość')
                        exit()
                    else:
                        result += second[num]
                        number = number.replace(num, '')
                        if num != 'IX':
                            number, result, value_first = check('IX', 9, number, result)
                        else:
                            if len(number) > 1:
                                if number[0] == 'X':
                                    number = number.replace('X', '')
                                    result += 10
                            value_first = False
        else:
            if len(number) >= 2:
                if number[0:2] == 'IX':
                    result += 9
                    number = number[2:]
                    value_first = False

        if value_first:
            num = create_num(first, number)
            if num:
                if len(num) == 1 or len(num) == 2:
                    if number[0] != 'I' and number[0] != 'V':
                        print('Podano złą wartość')
                        exit()
                    else:
                        result += first[num]
                        number = number.replace(num, '')
                else:
                    result += first[num]
                    number = number.replace(num, '')

    if number:
        print('Wprowadzono złe dane lub za dużą liczbę')
    elif result >= 4000:
        print('Wprowadzono złe dane')
    else:
        print(result)



def zadanie4():
    ekey = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}
    dkey = {'y': 'a', 'i': 'e', 'o': 'i', 'a': 'o', 'e': 'y'}
    NewmyString = []
    DecodecString = []
    myString = str(input('Podaj test do szyfrowania: '))
    for s in myString:
        if s in ekey:
            NewmyString = myString.replace[s, ekey(s)]

    print('Zaszyforwany tekst to: ', NewmyString)









def main():
    while True:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            break
        except ValueError:
            print('Numer zadania musi być od 1 do 5')

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