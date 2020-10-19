import sys, os, pprint
from nltk.tokenize import word_tokenize
from nltk.text import Text


trace = False

if sys.platform.startswith('win') :
    dirname = r'C:\Python31\Lib'
else : 
    dirname = '/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee'

allbooks = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.pdf'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allbooks.append((filename, fullsize))

allbooks.sort()
KEY = input('Key word ')
for filename in allbooks:
    WORD = word_tokenize(filename)
    Text(WORD)
    for item in WORD:
        if item == KEY.lower():
            print(filename)