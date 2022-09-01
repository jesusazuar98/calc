from msilib.schema import Font
from tkinter import *
import tkinter.font as font

class Calculator:


    def __init__(self):

        self.raiz=Tk()
        self.raiz.title('Calculadora')
        self.raiz.iconbitmap('calc.ico')
        self.raiz.resizable(width=0,height=0)
        #-------Pantalla-------------#

        self.numero_pantalla=StringVar()
        self.operacion=''
        self.resultado=float()

        self.results=Frame(self.raiz,height=150,bg='#B9B9B9')
        self.results.pack(side='top',fill='x')

        self.window=Entry(self.results,width=22,justify='right',font=font.Font(size=22),textvariable=self.numero_pantalla)
        self.window.grid(row=0,column=0,ipady=50,ipadx=10,padx=40,pady=5)

        #------Botones---------------#
        self.digits=Frame(self.raiz)
        self.digits.pack(fill='both',expand=True)

        #------Fila1---------------#
        
        self.button_font=font.Font(weight="bold",size=10)

        self.boton7=Button(self.digits,text='7',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('7'))
        self.boton7.grid(row=1,column=1)


        self.boton8=Button(self.digits,text='8',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('8'))
        self.boton8.grid(row=1,column=2)

        self.boton9=Button(self.digits,text='9',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('9'))
        self.boton9.grid(row=1,column=3)

        self.botonx=Button(self.digits,text='x',width=13,font=font.Font(size=10),height=5,command=lambda:self.multiplicar(self.numero_pantalla.get()))
        self.botonx.grid(row=1,column=4)

        #-----Fila 2------------#

        self.boton4=Button(self.digits,text='4',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('4'))
        self.boton4.grid(row=2,column=1)


        self.boton5=Button(self.digits,text='5',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('5'))
        self.boton5.grid(row=2,column=2)

        self.boton6=Button(self.digits,text='6',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('6'))
        self.boton6.grid(row=2,column=3)

        self.botonresta=Button(self.digits,text='-',width=13,font=font.Font(size=10),height=5,command=lambda:self.resta(self.numero_pantalla.get()))
        self.botonresta.grid(row=2,column=4)

        #----Fila 3 -----------#
        self.boton1=Button(self.digits,text='1',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('1'))
        self.boton1.grid(row=3,column=1)


        self.boton2=Button(self.digits,text='2',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('2'))
        self.boton2.grid(row=3,column=2)

        self.boton3=Button(self.digits,text='3',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('3'))
        self.boton3.grid(row=3,column=3)

        self.botonsuma=Button(self.digits,text='+',width=13,font=font.Font(size=10),height=5,command=lambda:self.suma(self.numero_pantalla.get()))
        self.botonsuma.grid(row=3,column=4)

        #--Fila 4 ---------------#

        self.botonc=Button(self.digits,text='C',font=self.button_font,width=13,height=5, command=lambda:self.numero_pulsado('C'))
        self.botonc.grid(row=4,column=1)


        self.boton0=Button(self.digits,text='0',font=self.button_font,width=13,height=5,command=lambda:self.numero_pulsado('0'))
        self.boton0.grid(row=4,column=2)

        self.botonpunto=Button(self.digits,text='.',font=self.button_font,width=13,height=5)
        self.botonpunto.grid(row=4,column=3)

        self.botondivisor=Button(self.digits,text='/',width=13,font=font.Font(size=10),height=5,command=lambda:self.dividir(self.numero_pantalla.get()))
        self.botondivisor.grid(row=4,column=4)

        #--Fila 5-------------#

        self.botonc=Button(self.digits,text='=',font=self.button_font,height=4,width=55,command=lambda:self.result())
        self.botonc.grid(row=5,column=1,columnspan=4,pady=2)


        #Introducir el numero 0 al principio
        self.numero_pantalla.set('0')

        #Operacion igual
        self.operacion_actual=''

        #Variable n
        self.n_posi=0


        self.center_window()
        self.raiz.mainloop()

    def numero_pulsado(self,num):

        if self.numero_pantalla.get()=='0' and num=='0':
            
            pass
        
        elif num=='C':

            self.numero_pantalla.set('0')
            self.resultado=0
            self.n_posi=0
        
        elif self.operacion!='' or (self.numero_pantalla.get()=='0' and num in [str(i) for i in range(1,10)]):
            
            self.numero_pantalla.set(num)

            self.operacion=""

        else:

            self.numero_pantalla.set(self.numero_pantalla.get()+num)
    
    
    def suma(self,num):

        self.n_posi=1
        self.operacion_actual='suma'
        self.operacion='suma'
        self.resultado+=float(num)

        self.numero_pantalla.set(self.resultado)
    
    def resta(self,num):
        
        self.operacion_actual='resta'
        self.operacion='resta'

        if self.n_posi==0:
            self.resultado+=float(num)
            self.numero_pantalla.set(self.resultado)
            self.n_posi=1

        else:
            
            self.resultado-=float(num)
            self.numero_pantalla.set(self.resultado)
    
    def multiplicar(self,num):
        
        self.operacion_actual='multi'
        self.operacion='multi'

        if self.n_posi==0:
            self.resultado+=float(num)
            self.numero_pantalla.set(self.resultado)
            self.n_posi=1

        else:
            
            self.resultado=self.resultado*float(num)
            self.numero_pantalla.set(self.resultado)

    def dividir(self,num):
        
        self.operacion_actual='divi'
        self.operacion='divi'

        if self.n_posi==0:
            self.resultado+=float(num)
            self.numero_pantalla.set(self.resultado)
            self.n_posi=1

        else:
            
            self.resultado=self.resultado/float(num)
            self.numero_pantalla.set(self.resultado)
    


    def result(self):
        
        
        if self.operacion_actual=='suma':
            self.numero_pantalla.set(self.resultado+float(self.numero_pantalla.get()))
            self.resultado=0

        elif self.operacion_actual=='resta':
            self.numero_pantalla.set(self.resultado-float(self.numero_pantalla.get()))
            self.resultado=0
            self.n_posi=0
        
        elif self.operacion_actual=='multi':
            self.numero_pantalla.set(self.resultado*float(self.numero_pantalla.get()))
            self.resultado=0
            self.n_posi=0

        elif self.operacion_actual=='divi':
            self.numero_pantalla.set(self.resultado/float(self.numero_pantalla.get()))
            self.resultado=0
            self.n_posi=0




    #Centrar ventana
    def center_window(self,ancho=456,largo=600):
        self.screen_x=self.raiz.winfo_screenwidth()
        self.screen_y=self.raiz.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.raiz.geometry(f'{ancho}x{largo}+{x}+{y}')
