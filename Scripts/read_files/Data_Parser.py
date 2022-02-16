### Class containing functions which convert the raw data files from NOVA and EC-LAb
import os
import re
import pandas as pd
#Makes the saved filename inpputtable into excel - limit of 31 chcaracters
def file_name_match(i):
    name =  os.path.basename(i)
    file_name = os.path.splitext(name)[0]+''
    match = re.search(r'\d\d_\d\d_\d\d ', file_name)
    if match != None:
        date = str(match.group())
        file_name = file_name.replace(date, '')
    match_2 = re.search(r'\d\d\d\d rpm ', file_name)
    if match_2 != None:
        rpm = str(match_2.group())
        file_name = file_name.replace(rpm, '')
    match_3 = re.search(r'\d\d\d\drpm ', file_name)
    if match_3 != None:
        rpm = str(match_3.group())
        file_name = file_name.replace(rpm, '')
    match_4 = re.search(r'\d\d\d rpm ', file_name)
    if match_4 != None:
        rpm = str(match_4.group())
        file_name = file_name.replace(rpm, '')
    match_5 = re.search(r'\d\d\d\drpm ', file_name)
    if match_5 != None:
        rpm = str(match_5.group())
        file_name = file_name.replace(rpm, '')
    if 'N2 ' in i:
        gas = 'N2'
#        file_name = file_name.replace('N2 ', '')   
    elif 'N2_' in i:
        gas = 'N2'
#        file_name = file_name.replace('N2_', '')
    if 'CO2 ' in i:
        gas = 'CO2'
#        file_name = file_name.replace('CO2 ', '')
    elif 'CO2_' in i:
        gas='CO2'
#        file_name = file_name.replace('CO2_', '')
    if 'O2 ' in i:
        gas = 'O2'
#        file_name = file_name.replace('O2 ', '')
    elif 'O2_' in i:
        gas = 'O2'
#        file_name = file_name.replace('O2_', '')  
    match_6 = re.search(r'\d\d_\d\d_\d\d\d\d', file_name)
    if match_6 != None:
        date = str(match_6.group())
        file_name = file_name.replace(date, '')
    if file_name[0] == " ":
        file_name = file_name[1:] 
    if len(file_name)>= 28:
        file_name = file_name[len(file_name)-27:len(file_name)]
    return file_name

class Read_files:
    def __init__(self, file):
        self.file = file
    def read_EC_lab_files(self):
        f = open(self.file, "r")
        for line in f:
            if 'Nb header lines :' in line:
                num = int(line.strip('Nb header lines :'))
        f = open(self.file, "r")
        count = 0
        dat = []
        for line in f:
            if int(count) >= int(num)-1:
                strip=line.strip()
                split=strip.split("\t")
                dat.append(split)
            count = count + 1
        df = pd.DataFrame(dat[1:], columns=dat[0])
        for i in df.columns:
            df[i] = pd.to_numeric(df[i], downcast="float")
        return df
    def read_Nova_files(self):
        name =  os.path.basename(self.file)
        if name != 'data.xlsx':
            lines = []
            f = open(self.file, "r")
            for line in f:
                if 'ï»¿' not in line:
                    lines.append(line)
            #Column names as given by the software - include one for each software
            times = ['Corrected time (s)']
            time_2 = ['Time (s)']
            Potential = ['WE(1).Potential (V)']
            Current = ['WE(1).Current (A)']
            Current_2 = ['WE(2).Current (A)']
            Scan = ['Scan']

            #loop through the data which has just been copied from the file
            lines_2 = []
            count = 0
            for line in lines:
            #if it is the first iteration of the loop
                if count == 0:
                    data1 = line.strip()
                    #choosing the data separator
                    if ';' in data1: 
                        data1 = data1.split(';')
                    else:
                        data1 = data1.split('\t')
                    #strip and split the first line to get the column headings (e.g. 'voltage (V)')
                    columns = data1
                #if it is past the first the iteration of the loop
                if count > 0:
                    #copy the data into a seperate list
                    lines_2.append(line)
                count = count + 1
            #set to 99 to start with as it is an unlikely number to come up so can tell if it is unchanged   
            time_col = 99
            time_2_col = 99
            potential_col = 99
            current_col = 99
            scan_col = 99
            #finding the index of all of the columns
            count = 0
            for i in columns:
                if i in times:
                    time_col = count
                elif i in time_2:
                    time_2_col = count
                elif i in Potential:
                    potential_col = count
                elif i in Current:
                    current_col = count
                elif i in Scan:
                    scan_col = count
                count = count + 1
            #extract potential
            potential_data = []
            if potential_col != 99:
                for line in lines_2:
                    if ';' in line: 
                        data = line.strip().split(';')
                    else:
                        data = line.strip().split()
                    potential_data.append(float(data[potential_col]))
            #extract time
            time_data = []
            if time_col != 99:
                for line in lines_2:
                    if ';' in line: 
                        data = line.strip().split(';')
                    else:
                        data = line.strip().split()
                    time_data.append(float(data[time_col]))
            #extract time_2
            time_2_data = []
            if time_2_col != 99:
                for line in lines_2:
                    if ';' in line:
                        data=line.strip().split(';')
                    else:
                        data = line.strip().split()
                    time_2_data.append(float(data[time_2_col]))
            #extract current
            current_data = []
            if current_col != 99:
                for line in lines_2:
                    if ';' in line:
                        data = line.strip().split(';')
                    else:
                        data = line.strip().split()
                    current_data.append(float(data[current_col]))
            #extract scan 
            scan_data = []
            if scan_col != 99:
                for line in lines_2:
                    if ';' in line:
                        data = line.strip().split(';')
                    else:
                        data = line.strip().split()
                    scan_data.append(float(data[scan_col]))
            #combine data into one dataframe
            dat = {'Corrected Time / s':time_data, 'Time / s':time_2_data, 'Potential':potential_data, 'Current':current_data, 'Scan':scan_data}
            #finding the non-empty columns and make a list
            columns_2 = []
            for i in dat:
                if len(dat[i]) != 0:
                    columns_2.append(i)
            dicts = {}
            for i in columns_2:
                if i == 'Corrected Time / s':
                    dicts[i] = time_data
                if i == 'Time / s':
                    dicts[i] = time_2_data
                if 'Potential' in i:
                    dicts[i] = potential_data
                if 'Current' in i:
                    dicts[i] = current_data
                if 'Scan' in i:
                    dicts[i] = scan_data
            df = pd.DataFrame(dicts)
            return df

