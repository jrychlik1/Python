from numpy import linalg, array
from matplotlib import pyplot
from numpy import pi, sin, power, linspace, cos, sqrt, arange

def zadanie1():
    a = array([[1, 2, 3, -2, -1],
               [3, 5, 5, -3, -9],
               [2, 3, 2, 0, -8],
               [2, 6, 7, -5, 1],
               [1, 2, 6, -4, -10]])

    b = array([6, 2, -5, 17, 12])

    result = linalg.solve(a, b)
    print("x = {:.2f}, y = {:.2f}, z = {:.2f}, t = {:.2f}, u = {:.2f}".format(*result))

def zadanie3():
    initialSpeed = float(input("Podaj prędkość początkową [m/s]: "))
    alfa = float(input("Podaj kąt pod jakim został rzucony obiekt (w stopniach): "))
    g = 9.81

    alfa = alfa * pi / 180
    highMax = power(sin(alfa) * initialSpeed, 2) / (2 * g)
    throwRange = (power(initialSpeed, 2) * sin(2 * alfa)) / g
    time = (2 * initialSpeed * sin(alfa)) / g

    print("Maksymalna wysokość osiągnięta przez obiekt: {:.2f}m".format(highMax))
    print("Zasięg obiektu: {:.2f}m".format(throwRange))
    print("Czas lotu obiektu: {:.2f}s".format(time))

    initialSpeedY = sin(alfa) * initialSpeed
    time1 = linspace(0, time, 100)
    ones = linspace(1, 1, 100)
    speedFromTime = (initialSpeedY - g * time1)
    speed = initialSpeed * cos(alfa)
    speedFromTimeX = speed * ones
    xt = speedFromTimeX * time1
    yt = initialSpeedY * time1 - (g * time1 ** 2) / 2

    pyplot.subplots_adjust(hspace=1.2)
    pyplot.subplot(3, 1, 1)
    pyplot.grid()
    pyplot.title('Predkość chwilowa w kierunku pionowym i poziomym po czasie t', fontsize=12)
    pyplot.ylabel('[m/s]')
    pyplot.xlabel('t[s]')
    pyplot.plot(time1, speedFromTime)
    pyplot.twinx()
    pyplot.plot(time1, speedFromTimeX)

    pyplot.subplot(3, 1, 2)
    pyplot.grid()
    pyplot.title('Położenie w funkcji czasu', fontsize=12)
    pyplot.xlabel('t[s]')
    pyplot.ylabel('r[m]')
    r = sqrt(power(xt, 2) + power(yt, 2))
    pyplot.plot(time1, r)

    pyplot.subplot(3, 1, 3)
    pyplot.ylabel('y[m]')
    pyplot.xlabel('x[m]')
    pyplot.axis('equal')
    pyplot.title('Tor rzutu ukośnego', fontsize=12)
    pyplot.plot(xt, yt)
    pyplot.grid()

    pyplot.show()

def zadanie4():
    languages = ('Java', 'C', 'Python', 'C++', 'C#', 'Visual Basic .NET',
                 'JavaScript', 'PHP', 'SQL', 'Swift')
    percent = [17.253, 16.086, 10.308, 6.196, 4.801,
               4.743, 2.090, 2.048, 1.843, 1.490]
    y = arange(len(languages))

    pyplot.bar(y, percent, align='center')
    pyplot.tick_params(labelsize=5)
    pyplot.xticks(y, languages)
    pyplot.ylabel('Popularność [%]')
    pyplot.xlabel('Język')
    pyplot.title('10 najpopularniejszych języków programowania')
    pyplot.show()

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
    elif exercise == 3:
        zadanie3()
    elif exercise == 4:
        zadanie4()
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()