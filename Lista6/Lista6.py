import trojkat
import SzyfrCezara as sc

def zadanie1():

    
    print('Zad. 1')
    print('\n' + '***' + '\n')

    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    c = int(input('Podaj trzecią liczbę: '))

    if a > b + c or b > a + c or c > a + b:
        print('Podane wartości nie spełniają warunku by być długościami trójkąta!')
    elif a <= 0 or b <= 0 or c <= 0:
        print('Podane wartości nie spełniają warunku by być długościami trójkąta!')
    else:
        print('Obwód: {}'.format(trojkat.circuit(a, b, c)))
        print('Pole: {}'.format(trojkat.field(a, b, c)))
        print(trojkat.checkTriangle(a, b, c))
        print(trojkat.checkTriangle2(a, b, c))

def zadanie2():
    sentence = input('Podaj dowolne zdanie:\n')
    print(sc.encryption(sentence))

def zadanie3(number):
    last_number = '1'
    if number == 1:
        return last_number
    elif number > 1:
        for num in range(2, number + 1):
            last_number += ' '
            new_number = ''
            count = 1
            for i in range(0, len(last_number) - 1):
                if last_number[i] == last_number[i + 1]:
                    count += 1
                else:
                    new_number += str(count) + str(last_number[i])
                    count = 1
            last_number = new_number
        return last_number
    else:
        return 'Liczba musi być większa od 0!'

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 10!')

    if exercise == 1:
        zadanie1()
    elif exercise == 2:
        zadanie2()
    elif exercise == 3:
        print(zadanie3(8))
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()
