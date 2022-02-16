from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Scripts.analysis.integrate_data import *
import os
thisdir = os.path.dirname(__file__)
rcfile = os.path.join(thisdir, '..', 'Misc', 'Icon.ico')

class integrate_window:
    def __init__(self, root, check_z, files, wb, sheets):
        from Scripts import Analysis_Window_Check
    
        x_selection = Analysis_Window_Check.x_selection
        y_selection = Analysis_Window_Check.y_selection
        z_selection = Analysis_Window_Check.z_selection
        z_2_selection = Analysis_Window_Check.z_2_selection

        self.root = root
        State = check_z.get()### if colour by z is checked
        No_selections = len(x_selection.keys())
        if No_selections == 1:
            #print(len(x_selection.keys())) ### number of ticked sheets
            plot_counter = 0
            place = list(x_selection.keys())[0]
            sheet = str(files[place])
            sheets[plot_counter] = sheet
            x = str(x_selection[place].get())
            y = str(y_selection[place].get())
            z = str(z_selection[place].get())
            z_2 = str(z_2_selection[place].get())
            x_sheet=wb[sheet]
            if x == 'time/s' or x == 'Time / s':
                if z_2 != 'None':
                    integrate_Window = Toplevel(self.root)
                    integrate_Window.title("Baseline Parameters")
                    integrate_Window.geometry("750x500")
                    integrate_Window.resizable(0, 0)
                    integrate_Window.iconbitmap(bitmap=rcfile)

                    a_label = Label(integrate_Window, text = 'X1', font='Helvetica 11 bold')
                    a_label.place(x=10, y=12.5)
                    a = Entry(integrate_Window, width=8, borderwidth=5)
                    a.place(x=100, y=10)
                    b_label = Label(integrate_Window, text = 'X2', font='Helvetica 11 bold')
                    b_label.place(x=10, y=42.5)
                    b = Entry(integrate_Window, width=8, borderwidth=5)
                    b.place(x=100, y=40)
                
                    y_label = Label(integrate_Window, text='y', font='Helvetica 11 bold')
                    y_label.place(x=10, y=70)

                    equal_label = Label(integrate_Window, text='=', font='Helvetica 11 bold')
                    equal_label.place(x=40, y=70)

                    m_label = Label(integrate_Window, text='m', font='Helvetica 11 bold')
                    m_label.place(x=70, y=70)

                    times_label = Label(integrate_Window, text='*', font='Helvetica 11 bold')
                    times_label.place(x=100, y=70)

                    x_label = Label(integrate_Window, text='x', font='Helvetica 11 bold')
                    x_label.place(x=130, y=70)

                    plus_label = Label(integrate_Window, text='+', font='Helvetica 11 bold')
                    plus_label.place(x=160, y=70)

                    c_label = Label(integrate_Window, text='c', font='Helvetica 11 bold')
                    c_label.place(x=190, y=70)

                    m = Entry(integrate_Window, width=6, borderwidth=5)
                    m.place(x=55, y=100)
                    
                    c = Entry(integrate_Window, width=6, borderwidth=5)
                    c.place(x=175, y=100)

                    fig=plt.figure(figsize=(5,5))
                    ax = fig.add_subplot(111)
                    
                    int = integrate(ax, x_sheet, State, x, y, z, z_2)
                    int_dat = int.data_acquisition(ax, x_sheet, x, y, z_2)
                    
                    canvas=FigureCanvasTkAgg(fig,master=integrate_Window)
                    canvas.get_tk_widget().place(x = 250, y = 0)

                    plotbutton=tk.Button(master=integrate_Window, text="Plot Baseline", command=lambda: int.baseline(canvas, int_dat[0], int_dat[1], ax, a, b, m, c, x, y), width = 10)
                    plotbutton.place(x=100,y=140)

                    Integrate_text = Text(integrate_Window)
                    Integrate_text.place(x=10, y=200, height=290, width=230)

                    integration_button = tk.Button(master=integrate_Window, text='Integrate', command=lambda: int.integration(Integrate_text, canvas, int_dat[0], int_dat[1], ax, a, b, m, c, x, y), width = 10)
                    integration_button.place(x=100, y=170)

                    fig.tight_layout()
        