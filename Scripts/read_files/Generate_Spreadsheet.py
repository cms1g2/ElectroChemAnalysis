### Class for generating a spreadsheet from from the inputted data
class generate_spreadsheet:
    def __init__(self, spreadsheet, data):
        self.data = data
        self.spreadsheet = spreadsheet
    def Notes_page(self, Notes):
        ws = self.spreadsheet.active
        ws.title = 'Notes'
        ws = self.spreadsheet[str('Notes')]
        chuncks = Notes.split('\n')
        counter = 0
        counts = 1
        for row in range(len(chuncks)):
            string = str(chuncks[counter])
            place = 'A'+str(counts)
            mycell = ws[place]
            mycell.value = string
            counter = counter +1
            counts = counts+1
        return ws
         




