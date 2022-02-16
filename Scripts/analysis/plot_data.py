from matplotlib.ticker import AutoMinorLocator
from Scripts.analysis.plot_settings import *

def plot(plot1, fig, check_z, files, wb, scan_select, x_selection, y_selection, z_selection, z_2_selection):
    State = check_z.get()
    
    x_plot = {}
    y_plot = {}
    z_plot = {}
    single_x_plot = {}
    single_y_plot = {}
    scan_1_x_plot = {}
    scan_1_y_plot = {}
    scan_2_x_plot = {}
    scan_2_y_plot = {}
    sheets = {}

    plot_counter = 0
    col = 0
    for i in x_selection:
        sheet = str(files[i])
        sheets[plot_counter] = sheet
        x = str(x_selection[i].get())
        y = str(y_selection[i].get())
        z = str(z_selection[i].get())
        z_2 = str(z_2_selection[i].get())
        x_sheet=wb[sheet]
        col_counter = 1
        for cell in x_sheet[1]:
            if cell.value == x:
                x_col_idx = chr(ord('@')+col_counter)
            if cell.value == y:
                y_col_idx = chr(ord('@')+col_counter)
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
        x_plot[plot_counter] = x_data
        y_plot[plot_counter] = y_data
        
        if len(scan_select.get()) == 0 and State == 0 and z_2 != 'None':
            col_counter = 1
            for cell in x_sheet[1]:
                if cell.value == 'Scan' or cell.value == 'cycle number':
                    z_2_col_idx = chr(ord('@')+col_counter)
                col_counter = col_counter+ 1
            col_5_counter = 0
            Single_x_scan = []
            Single_y_scan = []
            rows = []
            single_count_2 = 0
            for row in x_sheet[z_2_col_idx]:
                if col_5_counter > 2:
                    if int(row.value) == int(float(z_2)):
                        rows.append(single_count_2)
                    single_count_2 = single_count_2+1
                col_5_counter = col_5_counter+1
            for m in rows:
                Single_x_scan.append(x_plot[plot_counter][m])
                Single_y_scan.append(y_plot[plot_counter][m])
            single_x_plot[plot_counter] = Single_x_scan
            single_y_plot[plot_counter] = Single_y_scan
            single_line_plot_settings(plot1, single_x_plot[plot_counter],  single_y_plot[plot_counter], x, y, sheet)
        
        if len(scan_select.get()) == 0 and State == 1 and z_2 == 'None':
            if z != 'None':
                col_counter = 1
                for cell in x_sheet[1]:
                    if cell.value == z:
                        z_col_idx = chr(ord('@')+col_counter)
                    col_counter = col_counter+ 1
                col_4_counter = 0
                z_data = []
                for row in x_sheet[z_col_idx]:
                    if col_4_counter > 2:
                        z_data.append(row.value)
                    col_4_counter = col_4_counter+1
                z_plot[plot_counter] = z_data
                colour_by_z_scatter(plot1, fig, x_plot[plot_counter], y_plot[plot_counter], z_plot[plot_counter], x, y, sheet)
            
            if z == 'None':
                scatter_plot(plot1, x_plot[plot_counter], y_plot[plot_counter], x, y, sheet)
        
        if len(scan_select.get()) > 0 and State == 0 and z_2 == 'None':
            scan = scan_select.get()
            scan = scan.split(',')
            if z != 'None':
                col_counter = 1
                for cell in x_sheet[1]:
                    if cell.value == z:
                        z_col_idx = chr(ord('@')+col_counter)
                    col_counter = col_counter+ 1
                
                Single_x_scan = []
                Single_y_scan = []
                rows = []
                scan_1_x = []
                scan_1_y = []
                scan_2_x = []
                scan_2_y = []
                rows_1 = []
                rows_2 = []

                scan_count = 0
                if len(scan) == 2:
                    scn_1 = scan[0]
                    scn_2 = scan[1]
                    for scn in scan:
                        single_count = 0
                        col_5_counter = 0
                        for row in x_sheet[z_col_idx]:
                            if col_5_counter > 2:
                                if int(float(row.value)) == int(float(scn_1)):
                                    rows_1.append(single_count)
                                if int(float(row.value)) == int(float(scn_2)):
                                    rows_2.append(single_count)
                                single_count = single_count+1
                            col_5_counter = col_5_counter+1
                        scan_count = scan_count + 1
                    for f in rows_1:
                        scan_1_x.append(x_plot[plot_counter][f])
                        scan_1_y.append(y_plot[plot_counter][f])
                    for f in rows_2:
                        scan_2_x.append(x_plot[plot_counter][f])
                        scan_2_y.append(y_plot[plot_counter][f])
                    scan_1_x_plot[plot_counter] = scan_1_x
                    scan_1_y_plot[plot_counter] = scan_1_y
                    scan_2_x_plot[plot_counter] = scan_2_x
                    scan_2_y_plot[plot_counter] = scan_2_y

                    plot_2_scans(plot1, scan_1_x_plot[plot_counter], scan_1_y_plot[plot_counter], scan_2_x_plot[plot_counter], scan_2_y_plot[plot_counter], x, y, sheet, col)
                if len(scan) > 2 or len(scan) == 1:    
                    for scn in scan:
                        single_count = 0
                        col_5_counter = 0
                        for row in x_sheet[z_col_idx]:
                            if col_5_counter > 2:
                                if int(float(row.value)) == int(float(scn)):
                                    rows.append(single_count)
                                single_count = single_count+1
                            col_5_counter = col_5_counter+1
                        scan_count = scan_count + 1
                    for f in rows:
                        Single_x_scan.append(x_plot[plot_counter][f])
                        Single_y_scan.append(y_plot[plot_counter][f])
                    single_x_plot[plot_counter] = Single_x_scan
                    single_y_plot[plot_counter] = Single_y_scan
                    
                    single_line_plot_settings(plot1, single_x_plot[plot_counter], single_y_plot[plot_counter], x, y, sheet)
            if z == 'None':
                plt_2_scans_single(plot1, x_plot[plot_counter], y_plot[plot_counter], x, y, sheet, col)
        
        if len(scan_select.get()) == 0 and State == 0 and z_2 == 'None':
                single_line_plot_settings(plot1, x_plot[plot_counter], y_plot[plot_counter], x, y, sheet)
        col = col+1
        plot_counter = plot_counter + 1
    return