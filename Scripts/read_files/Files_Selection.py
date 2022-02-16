from tkinter import filedialog as fd
from tkinter import *
import os
#from read_files.File_Reading import *

def select_files(pathh):
#    status = Label(root, text='')
#    status.place(x=stat_x, y =stat_y)
#    status.destroy()
#    status = Label(root, text='Status: Opening Files')
#    status.place(x=stat_x, y=stat_y)
    global filenames
    global directory
    filetypes = (('All files', '*.*'),('text files', '*.txt'))
   
    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    lst = list(filenames)  
    for i in lst:
        directory = os.path.split(i)[0]
        file_name_2 = os.path.split(i)[1]
        pathh.insert(END, f'{file_name_2}\n')
#    status.destroy()
#    status = Label(root, text='Status: Files Open')
#    status.place(x=stat_x, y =stat_y)