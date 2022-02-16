from tkinter import filedialog as fd
from tkinter import *

def file_save():
    from Scripts.read_files import Files_Selection
    from Scripts.read_files import File_Reading
    
    global save_loc

    dir = Files_Selection.directory
    spreadsheet = File_Reading.spreadsheet

    #status = Label(root, text='')
    #status.place(x=stat_x, y =stat_y)
    #status.destroy()
    #status = Label(root, text='Status: Saving')
    #status.place(x=stat_x, y =stat_y)
    
    file_typ = (("Excel Files", "*.xlsx"),('All files', '*.*'))
    
    f = fd.asksaveasfile(initialdir=str(dir),defaultextension=".xlsx", filetypes=file_typ)
    
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    save_loc = str(f.name)
    spreadsheet.save(save_loc)
#    status.destroy()
#    status = Label(root, text='Status: Saved')
#    status.place(x=stat_x, y =stat_y)