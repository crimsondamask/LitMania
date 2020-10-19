from softmax import softmax
from atbash import atbash
ANSWER = input('What do you want to do? ')
if ANSWER.lower() == 'cipher' :
    #This block ciphers a message according to the atbash cipher
    ANSWER2 = input('Great! Did you put your text in the Desktop/code/cipher.txt ? ')
    if ANSWER2.lower() == 'yes' :
        TXT = open('cipher.txt', "r")
        CIPHERTXT = TXT.read()
        print(atbash(CIPHERTXT))
        TXT.close()
        CIPHERTXT2 = atbash(CIPHERTXT)
        f = open('cipher.txt', "a")
        f.write('The ciphered text==========> ')
        f.write(CIPHERTXT2)
        TXT.close()
        print('==> Thank You! The ciphered text is added to the bottom of the txt file.' )
    else :
        WORD = input('enter word to be ciphered: ')
        CIPHER = atbash(WORD)
        print(CIPHER)
        print('Thank You!' )
elif ANSWER.lower() == 'softmax' :
    #this block calculates the softmax for a vector
    num_array = list()
    num = input("Enter the number of elements you want to put in your vector:")
    print('Enter the numbers in the set individually ')
    for i in range(int(num)):
        n = input("num :")
        num_array.append(int(n))
    SOFTMAX = softmax(num_array)
    print(SOFTMAX)
else :
    print('Sorry! This program can only do ciphers and softmax functions :(... for now at least ')
