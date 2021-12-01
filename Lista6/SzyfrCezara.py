def encryption(sentence):
    result = ''
    for i in sentence:
        numberOfLetter = ord(i)
        if numberOfLetter > 96 and numberOfLetter < 123:
            numberOfLetter += 5
            if numberOfLetter > 122:
                numberOfLetter -= 26
        elif numberOfLetter > 64 and numberOfLetter < 91:
            numberOfLetter += 5
            if numberOfLetter > 90:
                numberOfLetter -= 26
        result += chr(numberOfLetter)
    return result

def decryption(sentence):
    result = ''
    for i in sentence:
        numberOfLetter = ord(i)
        if numberOfLetter > 96 and numberOfLetter < 123:
            numberOfLetter -= 5
            if numberOfLetter < 97:
                numberOfLetter += 26
        elif numberOfLetter > 64 and numberOfLetter < 91:
            numberOfLetter -= 5
            if numberOfLetter < 65:
                numberOfLetter += 26
        result += chr(numberOfLetter)
    return result