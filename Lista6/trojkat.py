from math import acos, pi

def circuit(a, b, c):
    result = a + b + c
    return result

def field(a, b, c):
    p = circuit(a, b, c) / 2
    result = round((p * (p - a) * (p - b)*(p - c)) ** 0.5, 4)
    if result == 0:
        print('Warunek istnienia trójkąta nie został spełniony.')
    else:
        return result

def checkTriangle(a, b, c):
    if a == b and b == c:
        return 'Trójkąt jest równoboczny'
    elif a == b or a == b or b == c:
        return 'Trójkąt jest równoramienny'
    else:
        return 'Trójkąt jest różnoboczny'

def checkTriangle2(a, b, c):
    cosAlpha = ((a ** 2) - (b ** 2) - (c ** 2)) / (-2 * b * c)
    result1 = acos(round(cosAlpha, 4))
    result1 = round(result1 * 180 / pi)

    cosBeta = ((b ** 2) - (a ** 2) - (c ** 2)) / (-2 * a * c)
    result2 = acos(round(cosBeta, 4))
    result2 = round(result2 * 180 / pi)

    cosGamma = ((c ** 2) - (a ** 2) - (b ** 2)) / (-2 * a * b)
    result3 = acos(round(cosGamma, 4))
    result3 = round(result3 * 180 / pi)

    if result1 == 90 or result2 == 90 or result3 == 90:
        return 'Trójkąt jest prostokątny'
    elif result1 > 90 or result2 > 90 or result3 > 90:
        return 'Trójkąt jest rozwartokątny'
    else:
        return 'Trójkąt jest ostrokątny'