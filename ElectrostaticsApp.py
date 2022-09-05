from tkinter import *
from Electrostatics import *
import math
from tkinter.simpledialog import askstring

class App:
    def __init__(self, master):
        # переменные модели
        self.points = []
        self.charges = []
        self.number_of_charges = 0
        # флаги
        self.can_set_charges = False
        # размеры холста
        self.canvas_width = 600
        self.canvas_height = 400
        self.scale = 20
        self.point_width = 4
        self.zero_x = self.canvas_width/2
        self.zero_y = self.canvas_height/2
        # фреймы
        self.f_top = Frame(master)
        self.f_bot = Frame(master)
        # виджеты
        self.label_scale_nx = Label(self.f_top, bg='white', fg = 'black', text='число точек по оси x:', width=25, font=("Courier", 14))
        self.entry_scale_nx = Entry(self.f_top,width=20, font=("Courier", 14))
        self.label_scale_ny = Label(self.f_top, bg='white', fg = 'black', text='число точек по оси y:', width=25, font=("Courier", 14))
        self.entry_scale_ny = Entry(self.f_top,width=20, font=("Courier", 14))
        self.button_set_field = Button(self.f_top, text="построить точки")
        self.label_number_of_charges = Label(self.f_top, bg='white', fg = 'black', text='число зарядов: 0', width=25, font=("Courier", 14))
        self.c = Canvas(self.f_bot, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.button_calc = Button(self.f_top, text="расчитать")
        self.button_reset = Button(self.f_top, text="сбросить")
        # размещение виджетов
        self.label_scale_nx.grid(row=0,column=0)
        self.entry_scale_nx.grid(row=0,column=1)
        self.label_scale_ny.grid(row=1,column=0)
        self.entry_scale_ny.grid(row=1,column=1)
        self.button_set_field.grid(row=2,column=0)
        self.label_number_of_charges.grid(row=3,column=0)
        self.button_calc.grid(row=4,column=0)
        self.button_reset.grid(row=4,column=1)
        self.c.grid(row=0,column=0)
        # размещение фреймов
        self.f_top.grid(row=0,column=0)
        self.f_bot.grid(row=1,column=0)
        # привязка событий
        self.button_set_field.bind('<Button-1>',self.SetPoints)
        self.c.bind('<Button-1>',self.SetCharge)
        self.button_calc.bind('<Button-1>',self.calc)
        self.button_reset.bind('<Button-1>',self.Reset)
        # переменные
        self.field = []
    def Reset (self, event):
        self.can_set_charges = False
        self.points = []
        self.charges = []
        self.number_of_charges = 0
        self.label_number_of_charges['text'] = 'число зарядов: 0'
        self.c.delete("all")
    def Draw (self,points):
        self.c.delete("all")
        for point in self.points:
            x1 = self.zero_x + point.x * self.scale
            y1 = self.zero_y + point.y * self.scale
            x2 = self.zero_x + point.x * self.scale + point.E[0] * self.scale
            y2 = self.zero_y + point.y * self.scale + point.E[1] * self.scale
            self.c.create_line(int(x1),int(y1),int(x2),int(y2),arrow=LAST,arrowshape="3 3 3")
        for charge in self.charges:
            x , y = self.zero_x + charge.x * self.scale , self.zero_y + charge.y * self.scale
            radius = 5
            if (charge.Q > 0):
                self.c.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),width=1,fill="red")
            if (charge.Q < 0):
                self.c.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),width=1,fill="blue")
    def SetCharge (self, event):
        if (self.can_set_charges):
            nx = int(self.entry_scale_nx.get())
            ny = int(self.entry_scale_ny.get())
            radius = 5
            x , y = event.x , event.y
            try:
                q = float(askstring('Заряд', 'введите величину заряда:'))
            except:
                q = 0
            if (q > 0):
                self.c.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),width=1,fill="red")
            if (q < 0):
                self.c.create_oval(int(x-radius),int(y-radius),int(x+radius),int(y+radius),width=1,fill="blue")
            x = (x - self.zero_x)/self.scale
            y = (y - self.zero_y)/self.scale
            if (q != 0):
                self.charges.append(Charge(x,y,q))
                self.number_of_charges += 1
                self.label_number_of_charges['text'] = 'число зарядов: '+str(self.number_of_charges)
    def SetPoints (self, event):
        self.Reset('<Button-1>')
        try:
            nx = int(self.entry_scale_nx.get())
            ny = int(self.entry_scale_ny.get())
            self.points = create_points (-10, 10, -10, 10, nx, ny)
            self.can_set_charges = True
            for point in self.points:
                x1 = self.zero_x + point.x * self.scale
                y1 = self.zero_y + point.y * self.scale
                x2 = self.zero_x + point.x * self.scale + self.point_width
                y2 = self.zero_y + point.y * self.scale
                self.c.create_line(int(x1),int(y1),int(x2),int(y2),width=self.point_width)
        except:
            print()
    def calc (self, event):
        self.Draw(calc_current_field(self.charges,self.points))
