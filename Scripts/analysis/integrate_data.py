from Scripts.analysis.plot_settings import *
import numpy as np
from shapely.geometry.linestring import LineString
import scipy.integrate as spi
from tkinter import *

count_2 = 0
class integrate:
    def __init__(self, ax, x_sheet, State, x, y, z, z_2):
        self.ax = ax
        self.x_sheet = x_sheet
        self.Strate = State
        self.x = x
        self.y = y
        self.z = z
        self.z_2 = z_2
        self.count_2 = count_2
    
    def data_acquisition(self, ax, x_sheet, x, y, z_2):
        col_counter = 1
        for cell in x_sheet[1]:
            if cell.value == x:
                x_col_idx = chr(ord('@')+col_counter)
            if cell.value == y:
                y_col_idx = chr(ord('@')+col_counter)
            if cell.value == 'Scan' or cell.value == 'cycle number':
                z_2_col_idx = chr(ord('@')+col_counter)
            col_counter = col_counter+1
        
        col_2_counter = 0
        x_data = []
        for row in x_sheet[x_col_idx]:
            if col_2_counter > 2:
                x_data.append(row.value)
            col_2_counter = col_2_counter +1
        col_3_counter = 0
        y_data = []
        for row in x_sheet[y_col_idx]:
            if col_3_counter > 2:
                y_data.append(row.value)
            col_3_counter = col_3_counter+1
        single_x_scan = []
        single_y_scan = []
        rows = []
        col_5_counter =0
        single_count_2 = 0
        for row in x_sheet[z_2_col_idx]:
            if col_5_counter > 2:
                if int(row.value) == int(float(z_2)):
                    rows.append(single_count_2)
                single_count_2 = single_count_2+1
            col_5_counter = col_5_counter+1
        for f in rows:
            single_x_scan.append(x_data[f])
            single_y_scan.append(y_data[f])
        single_x_scan_2 = []
        for i in single_x_scan:
            time_correction = i - single_x_scan[0]
            single_x_scan_2.append(time_correction)
        
        integrate_data_plot(ax, single_x_scan_2, single_y_scan, x, y)
        
        return single_x_scan_2, single_y_scan
        
    def baseline(self, canvas, single_x_scan_2, single_y_scan, ax, a, b, m, c, x, y):
        global x_val
        global y_val
        ax.clear()
        a_val = float(a.get())
        b_val = float(b.get())
        m_val = float(m.get())
        c_val = float(c.get())
        x_val = np.arange(a_val, b_val, 1)
        y_val=m_val*x_val+c_val

        integrate_data_plot(ax, single_x_scan_2, single_y_scan, x, y)
        integrate_data_plot(ax, x_val, y_val, x, y)
        canvas.draw()
    
    def integration(self, Integrate_text, canvas, single_x_scan_2, single_y_scan, ax, a, b, m, c, x, y):
        self.count_2 += 1
        ax.clear()
        a_val = float(a.get())
        b_val = float(b.get())
        m_val = float(m.get())
        c_val = float(c.get())
        first_line = LineString(np.column_stack((single_x_scan_2, single_y_scan)))
        second_line = LineString(np.column_stack((x_val, y_val)))
        intersection = first_line.intersection(second_line)
        count = 0
        for i in LineString(intersection).xy:
            lst = i.tolist()
            if count == 0:
                inter_x = lst
            if count == 1:
                inter_y = lst
            count = count+1
        count = 0 
        counter = []
        for i in single_x_scan_2:
            if i >= inter_x[0] and i <= inter_x[1]:
                counter.append(count)
            count = count + 1
        new_x_3 = []
        new_y_3 = []
        for i in counter:
            new_x_3.append(single_x_scan_2[i])
            new_y_3.append(single_y_scan[i])
        x_3 = np.linspace(inter_x[0],inter_x[1], len(new_x_3)) 
        y_3 = m_val*x_3+c_val
        new_y_4 = []
        count = 0
        for i in new_y_3:
            new_y_4.append(i - y_3[count])
            count = count + 1
        integral_1 = spi.trapz(new_y_4,new_x_3)

        integrate_data_plot(ax, single_x_scan_2, single_y_scan, x, y)
        integrate_data_plot(ax, x_val, y_val, x, y)
        integation_plot(ax, inter_x[0], inter_x[1], inter_y[0], inter_y[1], new_x_3, new_y_3)
        canvas.draw()

        if 'mA' in y:
            coulomb = integral_1/1000
            num = round(coulomb, 10)
        else:
            num = round(integral_1, 10)
            
        message = str(self.count_2)+'    '+str(num) + ' C'
        Integrate_text.insert(END, f'{message}\n')

