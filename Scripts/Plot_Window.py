from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Scripts.analysis import plot_data
import os
thisdir = os.path.dirname(__file__)
rcfile = os.path.join(thisdir, '..', 'Misc', 'Icon.ico')

class plot_window:
    def __init__(self, root, files, wb, check_z, scan_select):
        from Scripts import Analysis_Window_Check
    
        x_selection = Analysis_Window_Check.x_selection
        y_selection = Analysis_Window_Check.y_selection
        z_selection = Analysis_Window_Check.z_selection
        z_2_selection = Analysis_Window_Check.z_2_selection
        
        self.root = root
        Plot_Window = Toplevel(self.root)
        Plot_Window.title("Plot")
        Plot_Window.geometry("800x450")
        Plot_Window.iconbitmap(bitmap=rcfile)

        fig = Figure(figsize = (8, 4), dpi = 100)
        plot1 = fig.add_subplot(111)

        plot_data.plot(plot1, fig, check_z, files, wb, scan_select, x_selection, y_selection, z_selection, z_2_selection)

        Plot_canvas = FigureCanvasTkAgg(fig,master = Plot_Window)  
        Plot_canvas.draw()
        Plot_canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(Plot_canvas, Plot_Window)
        toolbar.update()
        Plot_canvas.get_tk_widget().pack()
        fig.tight_layout() 