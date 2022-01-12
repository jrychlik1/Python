from sys import argv
from numpy import average, var, std

def main():
    if len(argv) < 2:
        print('Nie podano argumentów!')
    else:
        data = argv[1:]
        data = list(map(int, data))
        aver = average(data)
        v = var(data)
        s = std(data)
        print("Średnia to {}\nWariacja to {}\n"
              "Odchylenie standardowe to {}".format(aver, v, s))


if __name__ == '__main__':
    main()