"""
This program encrypts a string using the railfence
cipher and will decrypt it back.
"""



import math

def scramble2Encrypt(plainText):
    evenChars = ''
    oddChars = ''
    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            #even
            evenChars = evenChars + ch
        else:
            #odd
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = evenChars + oddChars

    return cipherText

def decryptMessage(msg):
    if len(msg)%2 == 1:
        msg = msg + ' '
    halfLength=int(math.ceil((len(msg)/2)))
    decrypted = ''
    for i in range(halfLength):
        decrypted = decrypted + msg[0+i]
        decrypted = decrypted + msg[halfLength+i]
    return decrypted

def intro():
    intro=input('Do you want to encrypt or decrypt?: ')
    if intro.lower() == 'encrypt':
        statement=input('What would you like to encrypt?: ')
        msg=scramble2Encrypt(statement)
        print(msg)
    elif intro.lower() == 'decrypt':
        statement=input('What would you like to decrypt?: ')
        msg=decryptMessage(statement)
        print(msg)
    else:
        print('huh?')
        intro()


intro()
blank=input('')
