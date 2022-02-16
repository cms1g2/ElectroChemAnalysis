### Class handling the conversion of data 
# - converting between reference electrodes
# - converting current to current density
# - converting current density to mass activity
class data_conversion:
    def __init__(self, data):
        self.data = data
    def ref_conversion(self, shift, convert, ref):
        columns = self.data.columns
        col = len(columns)
        Shift_data = []
        Elect_Shift = float(shift)
        Conversion_to = str(convert)
        Conversion_from = str(ref)
        new = 'Potential / V vs. ' + Conversion_from
        Shifted = 'Potential / V vs. ' + Conversion_to
        if 'Ewe/V' in columns:
            for i in self.data['Ewe/V']:
                Shift_data.append(float(i)+Elect_Shift)
        if 'Potential' in columns:
            for i in self.data['Potential']:
                Shift_data.append(float(i)+Elect_Shift)
        self.data.insert(col, Shifted, Shift_data)
        if 'Ewe/V' in columns:
            self.data.columns = [new if x=='Ewe/V' else x for x in self.data.columns]
        if 'Potential' in columns:
            self.data.columns = [new if x=='Potential' else x for x in self.data.columns]
        return self.data
    def current_density_convert(self, res):
        col = len(self.data.columns)
        current_den = []
        Elect_area = float(res)
        new = 'Current / mA'
        if '<I>/mA' in self.data.columns:
            for i in self.data['<I>/mA']:
                mA = i
                current_den.append(mA/Elect_area)
        if 'Current' in self.data.columns:
            for i in self.data['Current']:
                mA = i*1000
                current_den.append(mA/Elect_area)
        self.data.insert(col, 'Current Density / mA/cm²', current_den)
        if '<I>/mA' in self.data.columns:
            new = 'Current / mA'
            self.data.columns = [new if x=='<I>/mA' else x for x in self.data.columns]
        if 'Current' in self.data.columns:
            new = 'Current / A'
            self.data.columns = [new if x=='Current' else x for x in self.data.columns]
        return self.data
    def loading_convert(self, load_entry, res):
        col = len(self.data.columns)
        load_entry = float(load_entry)
        Elect_area = float(res)
        mass_act = []
        if 'Current / mA' in self.data.columns:
            for i in self.data['Current / mA']:
                mA = i
                mass = (Elect_area*load_entry)/1000
                mass_act.append((mA/mass))
        if 'Current / A' in self.data.columns:
            for i in self.data['Current / A']:
                mA = i*1000
                mass = (Elect_area*load_entry)/1000
                mass_act.append((mA/mass))
        self.data.insert(col, 'Current Density / mA/g', mass_act)
        return self.data