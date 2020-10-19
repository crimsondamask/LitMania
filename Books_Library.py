import sys, os, pprint

#'/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee'

allbooks_pdf = []
def booklib(directory):
    dirname = directory 
    for (thisDir, subsHere, filesHere) in os.walk(dirname):
        for filename in filesHere:
            if filename.endswith('.pdf'):
                fullname = os.path.join(thisDir, filename)
                fullsize = os.path.getsize(fullname)
                allbooks_pdf.append((filename, fullsize))
    allbooks_pdf.sort()
    return(allbooks_pdf)

COUNT = 0

if __name__ == '__main__' :
    DIR = input('Enter your directory ')
    booklib(DIR)
    LIB = open('book_library.txt', 'a')
    for (filename, fullsize) in allbooks_pdf:
        LIBLIST = LIB.write(filename)
        LIBLIST = LIB.write(',  ')
        LIBLIST = LIB.write(str(fullsize))
        LIBLIST = LIB.write(' Bytes')
        LIBLIST = LIB.write('\n')  
        COUNT += 1  
    LIB.close()
    print(COUNT)