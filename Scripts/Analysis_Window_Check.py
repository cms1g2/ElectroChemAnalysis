from tkinter import *
import pandas as pd

def check_state(cb, cbVariables, wb, files, right_scrollable_frame):
    global y_drops
    global x_drops
    global z_drops
    global labels
    global x_selection
    global y_selection
    global z_selection
    global z_2_drops
    global z_2_selection
    check_state.counter += 1
    if int(check_state.counter) > 1:
        for i in x_drops:
            y_drops[i].destroy()
            x_drops[i].destroy()
            labels[i].destroy()
            z_drops[i].destroy()
            z_2_drops[i].destroy()
        
    counter = 0
    x_drops = {}
    y_drops = {}
    z_drops = {}
    labels = {}
    z_2_drops = {}
    x_selection = {}
    y_selection = {}
    z_selection = {}
    z_2_selection = {}
    grid_count = 1
    variable_dict = {}
    for i in cb:
        if cbVariables[counter].get() == 1:
            sheet = str(files[counter])
            ws = wb[sheet]
            headings=[]
            for cell in ws[1]:
                if cell.value != None:
                    headings.append(cell.value)
            headings.extend(['None'])
            x_selection[counter] = StringVar()
            y_selection[counter] = StringVar()
            z_selection[counter] = StringVar()
            z_2_selection[counter] = StringVar()
            initial_x_selection = []
            initial_y_selection = []
            
            for i in headings:
                if i == 'Potential / V':
                    initial_x_selection.append(i)
                if i == 'Current / A' or i == 'Current / mA':
                    initial_y_selection.append(i)
            if len(initial_x_selection) == 0:
                    initial_x_selection.append(headings[0])
            if len(initial_y_selection) == 0:
                    initial_y_selection.append(headings[1])
            if len(initial_x_selection) > 1:
                x_selection[counter].set(initial_x_selection[-1])
            if len(initial_y_selection) > 1:
                y_selection[counter].set(initial_y_selection[-1])
            if len(initial_x_selection) == 1:
                x_selection[counter].set(initial_x_selection[0])
            if len(initial_y_selection) == 1:
                y_selection[counter].set(initial_y_selection[0])
            else:
                x_selection[counter].set(initial_x_selection[0])
                y_selection[counter].set(initial_y_selection[1])
            
            z_selection[counter].set('None')
            z_2_selection[counter].set('None')

            data = ws.values
            columns = next(data)[0:]
            df = pd.DataFrame(data, columns=columns)
            df = df.drop([0])
            data_dict = df.to_dict('list')
            s_count = 0
            for i in headings:
                if i == 'Scan': 
                    variables = data_dict['Scan']
                    variables_2 = list(dict.fromkeys(variables))
                    variables_3 = []
                    for i in variables_2:
                        variables_3.append(str(i))
                    variables_3.append('None')
                    variable_dict[counter] = variables_3
                    s_count=s_count+1
                if i == 'cycle number':
                    variables = data_dict['cycle number']
                    variables_2 = list(dict.fromkeys(variables))
                    variables_3 = []
                    for i in variables_2:
                        variables_3.append(str(i))
                    variables_3.append('None')
                    variable_dict[counter] = variables_3
                    s_count=s_count+1
                if s_count == 0:
                    variable_dict[counter]=['None']   
            labels[counter] = Label(right_scrollable_frame, text=sheet, bg="white")
            labels[counter].grid(row=grid_count, column=0)
            x_drops[counter] = OptionMenu(right_scrollable_frame, x_selection[counter], *headings)
            x_drops[counter].grid(row=grid_count, column=1)
            y_drops[counter] = OptionMenu(right_scrollable_frame, y_selection[counter], *headings)
            y_drops[counter].grid(row=grid_count, column=2)
            z_drops[counter] = OptionMenu(right_scrollable_frame, z_selection[counter], *headings)
            z_drops[counter].grid(row=grid_count, column=3)
            z_2_drops[counter] = OptionMenu(right_scrollable_frame, z_2_selection[counter], *variable_dict[counter])
            z_2_drops[counter].grid(row=grid_count, column=4)
            grid_count = grid_count+1
        counter = counter + 1
check_state.counter = 0