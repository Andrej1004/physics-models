from tkinter import *
from strings import *
import math

class BallVis:
    def __init__ ( self , Id, x , y , r , zero_x , zero_y , ParentRoot ):
        self.Id = Id
        self.x = x
        self.y = y
        self.r = r
        self.zero_x = zero_x
        self.zero_y = zero_y
        self.BindTag = None
        self.modelBall = Ball ( self.Id , self.x , self.y )
        self.ParentRoot = ParentRoot
    def DrawBall (self , c):
        self.BindTag = c.create_oval( int( self.zero_x + self.x - self.r ) , int( self.zero_y + self.y - self.r) , int( self.zero_x + self.x + self.r ) , int( self.zero_y + self.y + self.r) , fill="orange")
        c.tag_bind(self.BindTag,'<Button-1>',self.printcords)
    def printcords(self,e):
        BindingVar = App.returnBindingVar(self.ParentRoot)
        CanFix = App.ReturnCanFixBallVar(self.ParentRoot)
        if (CanFix):
            self.modelBall.IsFixed = True
            c = App.ReturnCanva(self.ParentRoot)
            c.itemconfig(self.BindTag, fill='red')
            App.CanFixSetFalse(self.ParentRoot)
        if ( BindingVar[0] == True and BindingVar[1] == None ):
            App.setBallOne(self.ParentRoot,self.Id)
            return 0
        if ( BindingVar[0] == True and BindingVar[2] == None ):
            App.setBallTwo(self.ParentRoot,self.Id)
            return 0

class App:
    def __init__(self, master):
        # переменные модели
        self.CanRun = False
        self.modelBalls = []
        self.Ball_Id = 0
        self.Balls = []
        self.radius = 10
        self.addingBallsFlag = False
        self.canBindBalls = False
        self.canFixBall = False
        self.BallOne = None
        self.BallTwo = None
        # флаги
        # размеры холста
        self.canvas_width = 600
        self.canvas_height = 400
        self.scale = 20
        self.point_width = 4
        self.zero_x = self.canvas_width/2
        self.zero_y = self.canvas_height/2
        # фреймы
        # виджеты
        self.addBallButton = Button(master, text="добавить шар")
        self.bindBallsButton = Button(master, text="связать шары пружиной")
        self.makeBallFixedButton = Button(master, text="сделать шар фикированным")
        self.c = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.RunButton = Button(master, text="Запустить модель")
        self.StopButton = Button(master, text="Отановить модель")
        # размещение виджетов
        self.addBallButton.grid(row=0,column=0)
        self.bindBallsButton.grid(row=1,column=0)
        self.makeBallFixedButton.grid(row=2,column=0)
        self.c.grid(row=3,column=0)
        self.RunButton.grid(row=4,column=0)
        self.StopButton.grid(row=5,column=0)
        # размещение фреймов
        # привязка событий
        self.addBallButton.bind( '<Button-1>' , self.permitAddBall )
        self.bindBallsButton.bind( '<Button-1>' , self.permitBindBalls )
        self.makeBallFixedButton.bind( '<Button-1>' , self.FixBall )
        self.c.bind( '<Button-1>' , self.createBall )
        self.RunButton.bind( '<Button-1>' , self.runModel )
        self.StopButton.bind( '<Button-1>' , self.stopModel )
        # переменные
    def ReturnCanva (self):
        return self.c
    def FixBall (self,e):
        self.canFixBall = True
    def ReturnCanFixBallVar (self):
        return self.canFixBall
    def CanFixSetFalse (self):
        self.canFixBall = False
    def createBall (self,e):
        if (self.addingBallsFlag):
            x , y = e.x - self.zero_x , e.y - self.zero_y
            b = BallVis( self.Ball_Id , x , y , self.radius , self.zero_x , self.zero_y, self )
            self.Ball_Id += 1
            self.Balls.append(b)
            b.DrawBall(self.c)
            self.permitAddBall('<Button-1>')
    def permitAddBall (self,e):
        self.addingBallsFlag = not self.addingBallsFlag
    def permitBindBalls (self,e):
        if (self.canBindBalls == False):
            self.canBindBalls = True
    def returnBindingVar (self):
        return [ self.canBindBalls, self.BallOne , self.BallTwo ]
    def setBallOne (self,Id):
        self.BallOne = Id
        print(self.canBindBalls, self.BallOne , self.BallTwo)
    def setBallTwo (self,Id):
        self.BallTwo = Id
        if (self.BallTwo == self.BallOne):
            self.BallTwo = None
            return 0
        self.Balls[self.BallOne].modelBall.Bounds.append(self.Balls[self.BallTwo].modelBall)
        self.Balls[self.BallTwo].modelBall.Bounds.append(self.Balls[self.BallOne].modelBall)
        # string
        self.drawString(self.Balls[self.BallOne].modelBall,self.Balls[self.BallTwo].modelBall)
        #
        print(self.canBindBalls, self.BallOne , self.BallTwo)
        self.canBindBalls = False
        self.BallOne = None
        self.BallTwo = None
        print(self.canBindBalls, self.BallOne , self.BallTwo)
    def runModel(self,e):
        self.copy()
        for ball_1 in self.modelBalls:
            for ball_2 in self.modelBalls:
                if (ball_2.id != ball_1.id):
                    ball_1.colisionCheck.append(ball_2)
        self.CanRun = True
        while (self.CanRun):
            self.c.delete("all")
            for ball in self.modelBalls:
                ball.setCurrentAx()
                ball.setNextCords()
            for ball in self.modelBalls:
                ball.setNextAx()
                ball.setNextVel()
            for ball in self.modelBalls:
                ball.checkColis()
                ball.update()
            for ball in self.modelBalls:
                if (ball.IsFixed == False):
                    self.c.create_oval( int( self.zero_x + ball.x - self.radius ) , int( self.zero_y + ball.y - self.radius) , int( self.zero_x + ball.x + self.radius ) , int( self.zero_y + ball.y + self.radius) , fill="orange")
                else:
                    self.c.create_oval( int( self.zero_x + ball.x - self.radius ) , int( self.zero_y + ball.y - self.radius) , int( self.zero_x + ball.x + self.radius ) , int( self.zero_y + ball.y + self.radius) , fill="red")
                for bound in ball.Bounds:
                    self.drawString(ball,bound)
            self.c.update()
    def stopModel(self,e):
        self.CanRun = False
        self.modelBalls = []
        self.Ball_Id = 0
        self.Balls = []
        self.addingBallsFlag = False
        self.canBindBalls = False
        self.BallOne = None
        self.BallTwo = None
        self.c.delete("all")
    def copy (self):
        for ball in self.Balls:
            self.modelBalls.append(ball.modelBall)
        self.Balls = []
    def drawString (self,ball_1,ball_2):
        r = pow ( pow ( ball_2.x - ball_1.x , 2 ) + pow ( ball_2.y - ball_1.y , 2 ) , 0.5 )
        cosAlph = (ball_2.x - ball_1.x)/r
        sinAlph = (ball_2.y - ball_1.y)/r
        delta_x = r/10
        for i in range (0,9):
            x1 = (i*delta_x)
            x2 = ((i+1)*delta_x)
            y1 = (10*math.sin(i*delta_x*5*3.14/r))
            y2 = (10*math.sin((i+1)*delta_x*5*3.14/r))
            x_1 = int ( ball_1.x + self.radius + self.zero_x + cosAlph*x1 - sinAlph*y1 )
            x_2 = int ( ball_1.x + self.radius + self.zero_x + cosAlph*x2 - sinAlph*y2 )
            y_1 = int( ball_1.y + self.radius + self.zero_y + sinAlph*x1 + cosAlph*y1 )
            y_2 = int( ball_1.y + self.radius + self.zero_y + sinAlph*x2 + cosAlph*y2 )
            self.c.create_line(x_1,y_1,x_2,y_2)
