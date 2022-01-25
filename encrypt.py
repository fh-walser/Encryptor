def encrypt(word):
    letterArray = list(word)
    letterArray.reverse()
    encDict = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
    for letter in letterArray:
        if letter in encDict:
            letterArray[letterArray.index(letter)] = encDict[letter]
    result = ''.join(item for item in letterArray)
    result = result + 'aca'
    return result

print(encrypt('banana'))
print(encrypt('karaca'))
print(encrypt('burak'))
print(encrypt('alpaca'))
