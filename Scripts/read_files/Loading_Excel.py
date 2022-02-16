from tkinter import filedialog as fd
from tkinter import *
import os

def load_excel(pathh):
    global save_loc
#    status = Label(root, text='')
#    status.place(x=stat_x, y =stat_y)
#    status.destroy()
#    status = Label(root, text='Status: Loading File')
#    status.place(x=stat_x, y =stat_y)

    file_typ = (("Excel Files", "*.xlsx"),('All files', '*.*'))
    filenames = fd.askopenfilenames(initialdir='/',defaultextension=".xlsx", filetypes=file_typ)
    if filenames is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    lst = list(filenames)
    for i in lst:
        file_name_2 = os.path.split(i)[1]
        pathh.insert(END, f'{file_name_2}\n')
        save_loc = i
#    status.destroy()
#    status = Label(root, text='Status: Excel Loaded')
#    status.place(x=stat_x, y =stat_y)