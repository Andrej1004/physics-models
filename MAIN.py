from tkinter import *
import stringApp
import ElectrostaticsApp
import magnetsApp

class LaunherApp:
    def __init__(self, master):
        # виджеты
        self.frameTop = Frame(master)
        self.frameMain = Frame(master)
        self.frameMain_1 = Frame(self.frameMain)
        self.frameMain_2 = Frame(self.frameMain)
        self.frameMain_3 = Frame(self.frameMain)
        self.buttonStringApp = Button(self.frameTop, text="Пружины")
        self.buttonElectrostaticsApp = Button(self.frameTop, text="Электротатика")
        self.buttonMagnetsApp = Button(self.frameTop, text="Магнетизм")
        stringApp.App(self.frameMain_1)
        ElectrostaticsApp.App(self.frameMain_2)
        magnetsApp.App(self.frameMain_3)
        # размещение виджетов
        self.buttonStringApp.grid(row=0,column=0)
        self.buttonElectrostaticsApp.grid(row=0,column=1)
        self.buttonMagnetsApp.grid(row=0,column=2)
        self.frameTop.grid(row=0,column=0)
        self.frameMain.grid(row=1,column=0)
        self.frameMain_1.grid(row=0,column=0)
        self.frameMain_2.grid(row=0,column=0)
        self.frameMain_3.grid(row=0,column=0)
        # привязка событий
        self.buttonStringApp.bind('<Button-1>',self.startStringApp)
        self.buttonElectrostaticsApp.bind('<Button-1>',self.startElectrostaticsApp)
        self.buttonMagnetsApp.bind('<Button-1>',self.startMagnetsApp)
        self.StartClear()
    def startStringApp (self,e):
        self.frameMain_1.grid(row=0,column=0)
        self.frameMain_2.grid_forget()
        self.frameMain_3.grid_forget()
    def startElectrostaticsApp (self,e):
        self.frameMain_2.grid(row=0,column=0)
        self.frameMain_1.grid_forget()
        self.frameMain_3.grid_forget()
    def startMagnetsApp (self,e):
        self.frameMain_3.grid(row=0,column=0)
        self.frameMain_1.grid_forget()
        self.frameMain_2.grid_forget()
    def StartClear (self):
        self.frameMain_1.grid_forget()
        self.frameMain_2.grid_forget()
        self.frameMain_3.grid_forget()
    

root = Tk()
root.title("Физические модели")
root.geometry("650x700")
#root.resizable(0,0)
app = LaunherApp(root)
root.mainloop()
