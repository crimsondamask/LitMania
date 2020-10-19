from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.messagebox
import tkinter.font as font
from pysize import *
import fnmatch
import os, subprocess, webbrowser 

if sys.platform.startswith('win') :
    dirname = r'C:\Python31\Lib'
else : 
    dirname = '/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee'

main = tk.ThemedTk(theme='equilux')
main.geometry('600x800')
main.configure(bg='gray28')

is_checkedPDF = IntVar()
is_checkedEPUB = IntVar()

def insertlist():
    list1.delete(0, END)
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
                fullname = os.path.abspath(os.path.join(root, book))
                webbrowser.open(fullname)
                print(fullname)

def search():
    list1.delete(0, END)
    bookquery = e1.get().lower()
    COUNTBOOKS = 0
    with open('book_Data.txt', 'r') as f:
        for line1 in f.readlines():
            if bookquery in line1.lower():
                if is_checkedPDF.get():
                    if is_checkedEPUB.get():
                        if line1.endswith('.epub\n') or line1.endswith('.pdf\n'):
                            list1.insert(END, line1)
                            COUNTBOOKS += 1
                    else:
                        if line1.endswith('.pdf\n'):
                            list1.insert(END, line1)
                            COUNTBOOKS += 1
                else:
                    if is_checkedEPUB.get():
                        if line1.endswith('.epub\n'):
                            list1.insert(END, line1)
                            COUNTBOOKS += 1
                    else:
                        list1.insert(END, line1)
                        COUNTBOOKS += 1

    tkinter.messagebox.showinfo(title='Results', message='%d books found' %COUNTBOOKS)


myFont = font.Font(family='Helvetica', size=11)

l1 = ttk.Label(main, text='Welcome To LitMania', width=30)
l1.configure(anchor="center")
l1.grid(row=1, column=2)


chk_pdf = ttk.Checkbutton(main, text='pdf', width=5, onvalue=1, offvalue=0, variable=is_checkedPDF)
chk_pdf.grid(row=3, column=2)
chk_epub = ttk.Checkbutton(main, text='epub', width=5, onvalue=1, offvalue=0, variable=is_checkedEPUB)
chk_epub.grid(row=4, column=2)

l5 = ttk.Label(main, text='Queries')
l5.grid(row=6, column=2)

title_text = StringVar()
e1 = ttk.Entry(main, textvariable=title_text, width=30)
e1.grid(row=2, column=2)

list1 = Listbox(main, background='old lace', height=12, width=30)
scroll1 = ttk.Scrollbar(main)

list1.config(yscrollcommand=scroll1.set, background='gray28', foreground='gray66', relief=SUNKEN)
list1.config(font=myFont)
scroll1.config(command=list1.yview)

list1.grid(row=7, column=2, rowspan=6, columnspan=2, sticky=NSEW)
main.rowconfigure(7, weight=1)
main.columnconfigure(2, weight=1)
scroll1.grid(row=7, column=4, rowspan=6, sticky=NSEW)

b1 = ttk.Button(main, text='Search', command=search)
b1.grid(row=3, column=1)

b2 = ttk.Button(main, text='View All', command=insertlist)
b2.grid(row=4, column=1)

b3 = ttk.Button(main, text='Update', command=list_files(dirname))
b3.grid(row=5, column=1)

b4 = ttk.Button(main, text='Quit', command=main.destroy)
b4.grid(row=6, column=1)

def OnClick(event):
    search()

def do_popup(event):
    m.tk_popup(event.x_root, event.y_root)

def Double(event):
    SelectValue = list1.get(list1.curselection())
    Clicked(SelectValue)
    print(SelectValue)

def Click_Menu():
    SelectValueMenu = list1.get(list1.curselection())
    Clicked(SelectValueMenu)
    print(SelectValueMenu)

#def Open_Folder():
    #if sys.platform.startswith('win'):


m = Menu(main, tearoff=0)
m.config(background='gray28', foreground='gray66')
m.add_command(label="Open", command=Click_Menu)
m.add_command(label="Description")
m.add_command(label="Containing Folder")

list1.bind('<Double-Button-1>', Double)
list1.bind("<Button-3>", do_popup)
main.bind('<Return>', OnClick)
main.title('Book Library')
main.mainloop()