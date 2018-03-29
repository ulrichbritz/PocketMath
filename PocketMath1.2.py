import tkinter as tk
from functools import partial

#start
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Heading = 'PocketMath'
        tk.Frame.__init__(self, master, borderwidth = 8, relief = 'groove', bg = 'powder blue')
        self.grid()
        self.createWidgets()
        self.line = ''
        self.top = ''

    def __btnClick(self, evt):
        if self.lblOutput['text'] == 'Error':
            self.line = ''
            self.lblOutput['text'] = ''
            self.lblTop['text'] = self.top
        if evt.widget['text'] == 'AC':
            self.line = ''
            self.lblOutput['text'] = ''
            self.lblTop['text'] = ''
            self.top = ''
        else:
            if evt.widget['text'] == '=':
                try:
                    self.lblTop['text'] = self.top
                    #self.lblLine['text'] = self.line
                    self.line = str(eval(self.line))
                    self.lblOutput['text'] = self.line
                except:
                    self.lblTop['text'] = self.top
                    self.lblOutput['text'] = 'Error'
                    self.line = ''
                    self.top = ''
            else:
                if evt.widget['text'] == '+' or evt.widget['text'] == '-' or evt.widget['text'] == '*' or evt.widget['text'] =='/':
                    try:
                        self.top = self.top + evt.widget['text']
                        self.lblTop['text'] = self.top
                        self.line = str(eval(self.line))
                        self.lblOutput['text'] = self.line
                        self.line = self.line + evt.widget['text']
                    except:
                        pass   
                else:
                    if self.line.endswith('+') or self.line.endswith('-') or self.line.endswith('*') or self.line.endswith('/'):
                        self.lblOutput['text'] = ''
                    self.top = self.top + evt.widget['text']
                    self.line = self.line + evt.widget['text']
                    self.lblTop['text'] = self.top
                    self.lblOutput['text'] = self.lblOutput['text'] + evt.widget['text']
         
                
    def __btnCreate(self, lbl, rownum, columnnum):
        btn = tk.Button(self, text = lbl, width = 5, height = 2, borderwidth = 2, relief = 'raised' )
        btn.grid(row = rownum, column = columnnum)
        btn.bind('<Button-1>', self.__btnClick)

    def createWidgets(self):
        self.lblOutput = tk.Label(self, text = '', bg = 'light grey', font = 20, height = 3, borderwidth = 3, relief = 'sunken', width=20)
        self.lblOutput.grid(column=0, row=1 , columnspan = 4, rowspan =3)

        self.lblTop = tk.Label(self, text = '', bg = 'light grey', font = 5, height = 2, borderwidth = 3, relief = 'sunken',fg = 'grey', width=20)
        self.lblTop.grid(column=0, row=0 , columnspan = 4, rowspan =1)
        
        #buttons 0-9, +, -, *, /, =, AC
        row = 4
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
