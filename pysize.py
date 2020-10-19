import sys, os, fnmatch


if sys.platform.startswith('win') :
    dirname = r'C:\Python31\Lib'
else : 
    dirname = '/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee'


def list_files(startpath):
    book_library = []
    os.remove('book_Data.txt')
    FUCK2 = open('book_Data.txt', 'a')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        #print('{}{}/'.format(indent, os.path.basename(root)))
        book_library.append('{}{}/'.format(indent, os.path.basename(root)))
        FUCK2.write(str('{}{}'.format(indent, os.path.basename(root))))
        FUCK2.write('\n')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.endswith('.jpg'): 
                #print('{}{}'.format(subindent, f))
                book_library.append('{}{}'.format(subindent, f))
                FUCK2.write(str('{}{}'.format(subindent, f)))
                FUCK2.write('\n')
    FUCK2.close()

def insertlist():
    lines = open('book_Data.txt')
    list_lines = lines.readlines()
    for line in list_lines:
        list1.insert(END, line)
    lines.close()

def Clicked(value):
    pattern = '*' + value.strip() 
    for root, dirs, files in os.walk(dirname):
        for book in files:
            if fnmatch.fnmatch(book, pattern):
                fullname = os.path.join(root, book)
                os.system(r'start ' + fullname)
                print(fullname)

def search():
    list1.delete(0, END)
    bookquery = e1.get().lower()
    COUNTBOOKS = 0
    with open('book_Data.txt', 'r') as f:
        for line1 in f.readlines():
            if bookquery in line1.lower():
                list1.insert(END, line1)
                COUNTBOOKS += 1
    tkinter.messagebox.showinfo(title='Results', message='%d books found' %COUNTBOOKS)




#list_files('/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee')