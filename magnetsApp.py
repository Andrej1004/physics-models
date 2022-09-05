from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from subprocess import Popen
import math

class App:
    def __init__(self, master):
        # параметры отрисовки
        self.size = 10
        self.x0 = 0
        self.y0 = 0
        self.first_x = 0
        self.first_y = 0
        self.viewModel = ''
        # выбор модели
        self.labelChooseModel = Label(master, bg='white', fg = 'black', text='выберите модель:', width=25, font=("Courier", 14))
        self.comboChooseModel = ttk.Combobox(master, values=["Ising2d","IsingXY"], font=("Courier", 14))
        self.comboChooseModel.current(0)
        # задание размеров
        # по x
        self.labelNX = Label(master, bg='white', fg = 'black', text='число спинов по оси x:', width=25, font=("Courier", 14))
        self.entryNX = Entry(master,width=20, font=("Courier", 14))
        # по y
        self.labelNY = Label(master, bg='white', fg = 'black', text='число спинов по оси y:', width=25, font=("Courier", 14))
        self.entryNY = Entry(master,width=20, font=("Courier", 14))
        # ввод параметров
        # обменный интеграл
        self.labelJ = Label(master, bg='white', fg = 'black', text='введите J:', width=20, font=("Courier", 14))
        self.entryJ = Entry(master,width=20, font=("Courier", 14))
        # напряженность магнитного поля
        self.labelH = Label(master, bg='white', fg = 'black', text='введите H:', width=20, font=("Courier", 14))
        self.entryH = Entry(master,width=20, font=("Courier", 14))
        # температура начальная
        self.labelTStart = Label(master, bg='white', fg = 'black', text='введите начальную T:', width=25, font=("Courier", 14))
        self.entryTStart = Entry(master,width=20, font=("Courier", 14))
        # температура Конечная
        self.labelTEnd = Label(master, bg='white', fg = 'black', text='введите конечную T:', width=25, font=("Courier", 14))
        self.entryTEnd = Entry(master,width=20, font=("Courier", 14))
        # температура шаг изменения температуры
        self.labelDT = Label(master, bg='white', fg = 'black', text='введите шаг изменения T:', width=25, font=("Courier", 14))
        self.entryDT = Entry(master,width=20, font=("Courier", 14))
        # число шагов
        self.labelNSteps = Label(master, bg='white', fg = 'black', text='введите число шагов:', width=25, font=("Courier", 14))
        self.entryNSteps = Entry(master,width=20, font=("Courier", 14))
        # запуск
        self.buttonRun = Button(master, text="Запустить", font=("Courier", 14))
        # посмотреть
        self.buttonView = Button(master, text="посмотреть", font=("Courier", 14))
        # привязка событий
        self.buttonRun['command'] = self.Run
        self.buttonView['command'] = self.View
        # располагаем элементы
        self.labelChooseModel.grid(row=0,column=0)
        self.comboChooseModel.grid(row=0,column=1)
        self.labelNX.grid(row=1,column=0)
        self.entryNX.grid(row=1,column=1)
        self.labelNY.grid(row=2,column=0)
        self.entryNY.grid(row=2,column=1)
        self.labelJ.grid(row=3,column=0)
        self.entryJ.grid(row=3,column=1)
        self.labelH.grid(row=4,column=0)
        self.entryH.grid(row=4,column=1)
        self.labelTStart.grid(row=5,column=0)
        self.entryTStart.grid(row=5,column=1)
        self.labelTEnd.grid(row=6,column=0)
        self.entryTEnd.grid(row=6,column=1)
        self.labelDT.grid(row=7,column=0)
        self.entryDT.grid(row=7,column=1)
        self.labelNSteps.grid(row=8,column=0)
        self.entryNSteps.grid(row=8,column=1)
        self.buttonRun.grid(row=9,column=0)
        self.buttonView.grid(row=9,column=1)
    def Run (self):
        try:
            if (self.comboChooseModel.get()=="Ising2d"):
                nx = int(self.entryNX.get())
                ny = int(self.entryNY.get())
                J = float(self.entryJ.get())
                H = float(self.entryH.get())
                TStart = float(self.entryTStart.get())
                TEnd = float(self.entryTEnd.get())
                DT = float(self.entryDT.get())
                NSteps = int(self.entryNSteps.get())
                string="start.py "+"Ising2d "+str(nx)+" "+str(ny)+" "+str(J)+" "+str(H)+" "+str(TStart)+" "+str(TEnd)+" "+str(DT)+" "+str(NSteps)
                Popen(string,shell=True)
                print("ok")
            if (self.comboChooseModel.get()=="IsingXY"):
                nx = int(self.entryNX.get())
                ny = int(self.entryNY.get())
                J = float(self.entryJ.get())
                H = float(self.entryH.get())
                TStart = float(self.entryTStart.get())
                TEnd = float(self.entryTEnd.get())
                DT = float(self.entryDT.get())
                NSteps = int(self.entryNSteps.get())
                string="startXY.py "+"IsingXY "+str(nx)+" "+str(ny)+" "+str(J)+" "+str(H)+" "+str(TStart)+" "+str(TEnd)+" "+str(DT)+" "+str(NSteps)
                Popen(string,shell=True)
                print("ok")
        except ValueError:
            print("введите число")
    def View (self):
        self.view=Toplevel()
        self.view.title("график. масштабировать - колесо мыши. преместить - зажать ЛКМ")
        self.view.geometry("500x500")
        self.c = Canvas(self.view, width=450, height=450, bg='white')
        self.c.bind("<MouseWheel>",self.SizePic)
        self.c.bind("<B1-Motion>",self.MovePic)
        self.c.bind("<Button-1>",self.GetClick)
        self.c.grid(row=0,column=1)
        self.buttonPrev = Button(self.view, text="<", command=self.Prev)
        self.buttonNext = Button(self.view, text=">", command=self.Next)
        self.labelCurrentT = Label(self.view, bg='white', fg = 'black', text='температура: ', width=50)
        self.buttonPrev.grid(row=1,column=0)
        self.buttonNext.grid(row=1,column=2)
        self.labelCurrentT.grid(row=1,column=1)
        self.mainmenu = Menu(self.view)
        self.view.config(menu=self.mainmenu)
        self.mainmenu.add_command(label="Открыть", command=self.OpenFile)
        self.System = []
        self.currentShoot = 0
    def OpenFile (self):
        writeXY = False
        System = []
        SystemState = []
        XY = []
        file_name = fd.askopenfilename(filetypes=(("XY files","*.xy"),("All files","*.*")))
        f = open(file_name,'r')
        for line in f:
            if (line[0]=="M"):
                self.viewModel = line[line.find(" ")+1:line.find("\n")]
            if (line[0]=="T"):
                Temp = float(line[line.find(" ")+1:line.find("\n")])
                SystemState.append(Temp)
            if (line[0]=="x"):
                writeXY = True
                continue
            if (line[0]=="e"):
                writeXY = False
                SystemState.append(XY)
                System.append(SystemState)
                XY = []
                SystemState = []
            if (writeXY == True):
                addElem = []
                for el in line.replace('\n',"").split(" "):
                    addElem.append(float(el))
                XY.append(addElem)
        f.close()
        self.System = System
        self.Draw(System[0][1])
    def Draw (self,S):
        if (self.viewModel=="Ising2d"):
            size = self.size
            self.c.delete("all")
            for i in range(len(S)):
                for j in range(len(S[0])):
                    if (S[i][j]<0):
                        self.c.create_rectangle(int(self.x0)+size*i,int(self.y0)+size*j,int(self.x0)+size*i+size,int(self.y0)+size*j+size,fill='black', tags=("spin"))
            self.c.bind("spin",self.MovePic)
            self.c.update()
        if (self.viewModel=="IsingXY"):
            self.c.delete("all")
            r = self.size-2
            size = self.size
            for i in range(len(S)):
                for j in range(len(S[0])):
                    if 0<S[i][j]<math.pi/2:
                        self.c.create_line(int(self.x0)+10+size*i,int(self.y0)+10+size*j,int(self.x0)+10+size*i+int(r*math.cos(S[i][j])),int(self.y0)+10+size*j+int(r*math.sin(S[i][j])),fill='black',arrow=LAST,arrowshape="3 3 3", tag="spin")
                    elif math.pi/2<S[i][j]<math.pi:
                        self.c.create_line(int(self.x0)+10+size*i,int(self.y0)+10+size*j,int(self.x0)+10+size*i+int(r*math.cos(S[i][j])),int(self.y0)+10+size*j+int(r*math.sin(S[i][j])),fill='red',arrow=LAST,arrowshape="3 3 3", tag="spin")
                    elif math.pi<S[i][j]<3*math.pi/2:
                        self.c.create_line(int(self.x0)+10+size*i,int(self.y0)+10+size*j,int(self.x0)+10+size*i+int(r*math.cos(S[i][j])),int(self.y0)+10+size*j+int(r*math.sin(S[i][j])),fill='blue',arrow=LAST,arrowshape="3 3 3", tag="spin")
                    else:
                        self.c.create_line(int(self.x0)+10+size*i,int(self.y0)+10+size*j,int(self.x0)+10+size*i+int(r*math.cos(S[i][j])),int(self.y0)+10+size*j+int(r*math.sin(S[i][j])),fill='green',arrow=LAST,arrowshape="3 3 3", tag="spin")
            self.c.tag_bind("spin",self.MovePic)
            self.c.update()
    def Next(self):
        if (self.currentShoot+1<len(self.System)):
            self.currentShoot += 1
            self.labelCurrentT['text']='температура: '+str(self.System[self.currentShoot][0])
        SystemState = self.System[self.currentShoot][1]
        self.Draw(SystemState)
    def Prev(self):
        if (self.currentShoot-1>=0):
            self.currentShoot -= 1
            self.labelCurrentT['text']='температура: '+str(self.System[self.currentShoot][0])
        SystemState = self.System[self.currentShoot][1]
        self.Draw(SystemState)
    def UpdatePic(self):
        SystemState = self.System[self.currentShoot][1]
        self.Draw(SystemState)
    def SizePic (self,event):
        if event.num == 5 or event.delta == -120:
            if (self.size > 4):
                self.size -= 1
            self.UpdatePic()
        if event.num == 4 or event.delta == 120:
            self.size += 1
            self.UpdatePic()
    def MovePic (self,event):
        self.x0 += (event.x-self.first_x)/10
        self.y0 += (event.y-self.first_y)/10
        coords = self.c.coords("spin")
        x = int(self.x0)-coords[0]
        y = int(self.y0)-coords[1]
        self.c.move("spin",x,y)
    def GetClick(self,event):
        self.first_x = event.x
        self.first_y = event.y
