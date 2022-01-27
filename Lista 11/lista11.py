import urllib.request
import re

class Zadanie1():
    def __init__(self, link):
        self.link = link

    def check(self):
        try:
            urllib.request.urlopen(self.link).getcode()
            return 'Jest taka strona'
        except:
            return 'Nie ma takiej strony'

class Zadanie3():
    def __init__(self, text):
        self.text = text

    def find_links(self):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]|[.]|[/]))+',
                          self.text)
        print("Urls: ", urls)

class Zadanie4():
    def __init__(self, text):
        self.text = text

    def find_words(self):
        a_and_e = re.findall(' a[a-zA-Z]+| A[a-zA-Z]+| e[a-zA-Z]+| E[a-zA-Z]+', self.text)
        print(a_and_e)

class Zadanie5():
    def __init__(self, text):
        self.text = text

    def change(self):
        return re.sub(r"([a-z])([A-Z])", r"\1 \2", self.text)

class CiagArytmetyczny():
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def __len__(self):
        return self.a1 + self.r

    def __iter__(self):
        self.start = 1
        return self

    def __next__(self):
        if self.start <= self.n:
            result = self.a1
            self.a1 = self.__len__()
            self.start += 1
            return result
        else:
            raise StopIteration()

    def save_file(self, *args):
        file = open('ciag.txt', 'w')
        for a in args:
            file.write(str(a))
        file.close()

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 10!')

    if exercise == 1:
        z1 = Zadanie1('http://www.stackoverflow.com')
        print(z1.check())
    elif exercise == 3:
        z3 = Zadanie3('''Born is a small lunar https://en.wikipedia.org/wiki/Lunar_craters impact crater https://en.wikipedia.org/wiki/Impact_crater
        located near the eastern edge of the Moon https://en.wikipedia.org/wiki/Moon,
        to the northeast of the prominent crater Langrenus https://en.wikipedia.org/wiki/Langrenus_(crater) . It was previously designated Maclaurin Y before being
        named by the IAU https://en.wikipedia.org/wiki/International_Astronomical_Union in 1979.
        Maclaurin https://en.wikipedia.org/wiki/Maclaurin_(crater) itself lies to the north.
        Apollo 15 Mapping Camera image https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Born_crater_AS15-M-1991.jpg/240px-Born_crater_AS15-M-1991.jpg''')
        z3.find_links()
    elif exercise == 4:
        z4 = Zadanie4('''Born is a small lunar https://en.wikipedia.org/wiki/Lunar_craters impact crater https://en.wikipedia.org/wiki/Impact_crater
        located near the eastern edge of the Moon https://en.wikipedia.org/wiki/Moon,
        to the northeast of the prominent crater Langrenus https://en.wikipedia.org/wiki/Langrenus_(crater) . It was previously designated Maclaurin Y before being
        named by the IAU https://en.wikipedia.org/wiki/International_Astronomical_Union in 1979.
        Maclaurin https://en.wikipedia.org/wiki/Maclaurin_(crater) itself lies to the north.
        Apollo 15 Mapping Camera image https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Born_crater_AS15-M-1991.jpg/240px-Born_crater_AS15-M-1991.jpg
        And here is the word beginning with "a" letter.''')
        z4.find_words()
    elif exercise == 5:
        z5 = Zadanie5('BornIsSmallLunarImpactCrater')
        print(z5.change())
    elif exercise == 6:
        z6 = CiagArytmetyczny(2, 3, 4)
        z = list(z6)
        print(z)
        z6.save_file(z)
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()
