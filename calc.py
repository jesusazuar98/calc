from tkinter import *

class Calculator:


    def __init__(self):

        self.raiz=Tk()

        self.frame=Frame(self.raiz)
        self.frame.pack()
        self.center_window()
        self.raiz.mainloop()

    #Centrar ventana
    def center_window(self,ancho=500,largo=600):
        self.screen_x=self.raiz.winfo_screenwidth()
        self.screen_y=self.raiz.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.raiz.geometry(f'{ancho}x{largo}+{x}+{y}')
