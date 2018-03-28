import tkinter as tk
from functools import partial

#start    
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def __btnClick(self, evt):
        if evt.widget['text'] == 'AC':
           self.lblOutput['text'] = ''
        else:
            if evt.widget['text'] == '=':
                if bool(eval(self.lblOutput['text'])) == 'false':
                    self.lblOutput['text'] = 'Error'
                else:
                    ans = eval(self.lblOutput['text'])
                    self.lblOutput['text'] = str(ans)  
            else:
                self.lblOutput['text'] = self.lblOutput['text'] + evt.widget['text']
                
                
                
        
    def __btnCreate(self, lbl, rownum, columnnum):
        btn = tk.Button(self, text = lbl, width = 5, height = 2, borderwidth = 2, relief = 'raised' )
        btn.grid(row = rownum, column = columnnum)
        btn.bind('<Button-1>', self.__btnClick)

    def createWidgets(self):
        self.lblOutput = tk.Label(self, text = '', bg = 'light grey', font = 20, height = 3, borderwidth = 3, relief = 'sunken', width=20)
        self.lblOutput.grid(column=0, row=0 , columnspan = 4, rowspan =3)
        
        #buttons 0-9, +, -, *, /, =, AC
        row = 3
        column = -1
        for i in ['0', '1','2','3','4','5','6','7','8','9','.', '+', '-', '*', '/', '=', 'AC']:
            if column == 3:
                column = 0
                row = row + 1
            else:
                column = column + 1
            self.__btnCreate(i, row, column)
           



app = Application()
app.mainloop()
