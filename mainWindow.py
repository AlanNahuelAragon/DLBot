from tkinter import Tk,Label,Button,Frame,messagebox,Entry
from tkinter.ttk import Combobox
import dlProcessor as dlp
import threading as th
import time

class MainWindow(Frame):
    resValues=["1152x648","1600x900","1920x1080"]
    selectedRes="1600x900"
    
    def setRes(self):
        selectedRes=cmbResSelector.current()
        print(selectedRes+" this")
        
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_elements()
        
    def testMethod(self):
        print('working')
        
    def showStartMessage(self):
        self.stateLbl2.config(text="Bot ejecutandose", bg='green', fg='black')
        self.startBtn.config(state="disabled")
        messagebox.showinfo(message="Push the P key to stop",title='Starting...')
        thread=th.Thread(target=dlp.StartBot.mainMethod(self.selectedRes))
        thread.start()
        self.stateLbl2.config(text="Bot detenido", bg='red', fg='white')
        self.startBtn.config(state="normal")
        
    def getRes(self,event):
        self.selectedRes=self.cmbResSelector.get()
        print(self.selectedRes)
            
    def create_elements(self):
        self.wellcomeLbl=Label(self,text="Bienvenido al Bot Duel Links")
        self.selectResLbl=Label(self,text="Selecciona la resolucion de tu juego")
        self.cmbResSelector=Combobox(self,width="10",values=self.resValues,state='readonly')
        self.cmbResSelector.bind("<<ComboboxSelected>>",self.getRes)
        
        self.selectWarn=Label(self,text="Recuerda correr DL en modo ventana!")
        self.startBtn=Button(self,text="START",command=self.showStartMessage)
        self.stateLbl=Label(self,text="Estado:")
        self.stateLbl2=Label(text="Bot detenido",bg='red',fg='white')
        
        self.wellcomeLbl.pack()
        self.selectResLbl.pack()
        self.cmbResSelector.pack()
        self.cmbResSelector.current(1)
        self.selectWarn.pack()
        self.startBtn.pack()
        self.stateLbl.pack()
        self.stateLbl2.pack()


#-------

