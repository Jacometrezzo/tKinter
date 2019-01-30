from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt =''
    def __init__(self):
        Tk.__init__(self)
        self.title('Termómetro')
        self.geometry('210x150')
        self.configure(bg='#DED7B9')
        self.resizable(0,0)
        
        self.temperatura = StringVar(value = '')
        self.temperatura.trace('w', self.validateTemperature)
        self.tipoUnidad = StringVar(value = 'F')
        

        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text='Grados:').place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text='Fahrenheit', variable=self.tipoUnidad,value='F').place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text='Celsius', variable=self.tipoUnidad,value='C').place(x=20, y=95)


    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):
        nuevoValor = self.temperatura.ret()
        
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temeratur.set(self.__temperaturaAnt)

        
if __name__ == '__main__':
    app = mainApp()
    app.start()
        
        