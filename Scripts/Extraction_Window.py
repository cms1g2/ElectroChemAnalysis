from tkinter import *
from tkinter import ttk
import os
from Scripts.read_files.Files_Selection import select_files
from Scripts.read_files.File_Reading import reading_files
from Scripts.read_files.Files_Selection import *
from Scripts.read_files.Save_Files import *
from Scripts.read_files.Loading_Excel import *
from Scripts.Analysis_Window import *
thisdir = os.path.dirname(__file__)
rcfile = os.path.join(thisdir, '..', 'Misc', 'Icon.ico')

class Extraction_Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Electrochemical Data Extraction')
        self.root.geometry('850x300')
        self.root.resizable(0, 0)
        self.root.iconbitmap(bitmap=rcfile)

        #Open files window
        self.pathh = Text(self.root)
        self.pathh.place(x=120, y = 10, width =700, height=110)
        self.scrollbar = ttk.Scrollbar(self.root, orient='vertical', command=self.pathh.yview)
        self.pathh['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.place(x=820, y = 10, height=110)


        #open files button    
        self.open_button = ttk.Button(self.root,text='Open Files',command=lambda: select_files(self.pathh))
        self.open_button.place(x=10, y=0) 

        #run button
        self.run_button = ttk.Button(self.root, text='Run', command=lambda: reading_files(pstat, Area, loading, check_load, checkbutton, Shift, Convert, Ref, Notes))
        self.run_button.place(x=10, y=30)

        # Save as button
        self.save_as_button = ttk.Button(self.root, text='Save', command = lambda: file_save())
        self.save_as_button.place(x=10, y=60)

        #load excel button
        self.load = ttk.Button(self.root, text='Load', command=lambda: load_excel(self.pathh))
        self.load.place(x=10, y=120)

        self.Analyse = ttk.Button(self.root, text ="Analyse", command =lambda: analysis_window(self.root))
        self.Analyse.place(x=10, y=90)

        #status bar
#        status = Label(root, text='Status: Idle')
        #position of status bar
#        stat_x=0
#        stat_y=280
#        status.place(x=stat_x, y =stat_y)

        #dropdown menu for the potentiostat
        PSTAT = Label(self.root, text='Potentiostat:')
        PSTAT.place(x=10, y = 155)
        pstat = StringVar(self.root)
        pstat.set("Nova") # default value
        pstat_dropdown = OptionMenu(self.root, pstat, "Nova", "EC-Lab", "Ivium")
        pstat_dropdown.place(x=130, y=150)

        #electrode area entry 
        area = Label(self.root, text='Electrode Area:')
        area.place(x=10, y=190)
        Area = Entry(self.root, width=8, borderwidth=5)
        Area.place(x=135, y=185)
        area_2 = Label(self.root, text='cm²')
        area_2.place(x=200, y=190)

        #Loading entry
        Loading = Label(self.root, text='Loading:')
        Loading.place(x=10, y=245)
        loading = Entry(self.root, width=8, borderwidth=5)
        loading.place(x=135, y=240)
        Loading_2 = Label(self.root, text='mg/cm²')
        Loading_2.place(x=200, y=245)
        loading['state'] = DISABLED
        Loading['state'] = DISABLED
        Loading_2['state'] = DISABLED

        check_load = IntVar()
        def FlipState_2():
            State = check_load.get()
            if State == 0:
                loading['state'] = DISABLED
                Loading['state'] = DISABLED
                Loading_2['state'] = DISABLED
            elif State == 1:
                loading['state'] = NORMAL
                Loading['state'] = NORMAL
                Loading_2['state'] = NORMAL
        Check_load = ttk.Checkbutton(self.root, text='Known Loading', variable = check_load, onvalue='1', offvalue='0', command=FlipState_2)
        Check_load.place(x=10, y = 215)

        #reference electrode drop down
        ref = Label(self.root, text='Reference electrode:')
        ref.place(x=270, y = 185)
        Ref = StringVar(self.root)
        Ref.set("MMO") # default value
        Ref_dropdown = OptionMenu(self.root, Ref, "RHE", "MMS", "MMO")
        Ref_dropdown.place(x=380, y=180)
        Ref_dropdown['state'] = DISABLED
        ref['state'] = DISABLED

        #Conversion to drop down
        convert = Label(self.root, text='Convert Ref To:')
        convert.place(x=270, y = 215)
        Convert = StringVar(self.root)
        Convert.set("RHE") # default value
        Convert_dropdown = OptionMenu(self.root, Convert, "RHE", "MMS", "MMO")
        Convert_dropdown.place(x=380, y=210)
        Convert_dropdown['state'] = DISABLED
        convert['state'] = DISABLED

        #Potential shift
        shift = Label(self.root, text='Potential Shift:')
        shift.place(x=270, y=245)
        Shift = Entry(self.root, width=8, borderwidth=5)
        Shift.place(x=385, y=240)
        shift_2 = Label(self.root, text='V')
        shift_2.place(x=445, y=245)
        Shift['state'] = DISABLED
        shift['state'] = DISABLED
        shift_2['state'] = DISABLED

        #Reference Check
        checkbutton = IntVar()
        def FlipState():
            test = checkbutton.get()
            if test == 0:
                Ref_dropdown['state'] = DISABLED
                ref['state'] = DISABLED
                Convert_dropdown['state'] = DISABLED
                convert['state'] = DISABLED
                Shift['state'] = DISABLED
                shift['state'] = DISABLED
                shift_2['state'] = DISABLED
            elif test == 1:
                Ref_dropdown['state'] = NORMAL
                ref['state'] = NORMAL
                Convert_dropdown['state'] = NORMAL
                convert['state'] = NORMAL
                Shift['state'] = NORMAL
                shift['state'] = NORMAL
                shift_2['state'] = NORMAL
        Check = ttk.Checkbutton(self.root, text='Convert Reference', variable = checkbutton, onvalue='1', offvalue='0', command=FlipState)
        Check.place(x=270, y = 155)

        #Notes text box
        notes = Label(self.root, text='Notes')
        notes.place(x=480, y=150)
        Notes = Text(self.root)
        Notes.place(x=480, y = 170, width=340, height=100)
        scrollbar_2 = ttk.Scrollbar(self.root, orient='vertical', command=Notes.yview)
        Notes['yscrollcommand'] = scrollbar_2.set
        scrollbar_2.place(x=820, y = 170, height=100)

    def start(self):
        self.root.mainloop()
