class Ball:
    def __init__ ( self , Id , x , y ):
        # id
        self.id = Id
        # params
        self.Bounds = []
        self.l0 = 20
        self.k = 50
        self.dt = 0.01
        # current
        self.x = x
        self.y = y
        self.a_x = 0
        self.a_y = 0
        self.v_x = 0
        self.v_y = 0
        # next
        self.x_next = 0
        self.y_next = 0
        self.a_x_next = 0
        self.a_y_next = 0
        self.v_x_next = 0
        self.v_y_next = 0
    # Current a:
    def setCurrentAx (self):
        a_x , a_y = 0 , 0
        for b in self.Bounds:
            r = pow ( pow ( b.x - self.x , 2 ) + pow ( b.y - self.y , 2 ) , 0.5 )
            a_x += a_x + self.k * ( self.l0 - r ) * (  b.x - self.x ) / r
            a_y += a_y + self.k * ( self.l0 - r ) * (  b.y - self.y ) / r
        self.a_x , self.a_y = a_x , a_y
    def getCurrentAx (self):
        return [ self.a_x , self.a_y ]
    # Next a:
    def setNextAx (self):
        a_x_next , a_y_next = 0 , 0
        for b in self.Bounds:
            r = pow ( pow ( b.x_next - self.x_next , 2 ) + pow ( b.y_next - self.y_next , 2 ) , 0.5 )
            a_x_next += a_x_next + self.k * ( self.l0 - r ) * (  b.x_next - self.x_next ) / r
            a_y_next += a_y_next + self.k * ( self.l0 - r ) * (  b.y_next - self.y_next ) / r
        self.a_x_next , self.a_y_next = a_x_next , a_y_next
    def getNextAx (self):
        return [ self.a_x_next , self.a_y_next ]
    # Next v:
    def setNextVel (self):
        self.v_x_next = self.v_x + 0.5 * ( self.a_x + self.a_x_next ) * self.dt
        self.v_y_next = self.v_y + 0.5 * ( self.a_y + self.a_y_next ) * self.dt
    def getNextVel (self):
        return [ self.v_x_next , self.v_y_next ]
    # Next cords:
    def setNextCords (self):
        self.x_next = self.x + self.v_x * self.dt + 0.5 * self.a_x * pow ( self.dt , 2 )
        self.y_next = self.y + self.v_y * self.dt + 0.5 * self.a_y * pow ( self.dt , 2 )
    def getNextCords (self):
        return [ self.x_next , self.y_next ]
    # Update:
    def update (self):
        self.x = self.x_next
        self.y = self.y_next
        self.a_x = self.a_x_next
        self.a_y = self.a_y_next
        self.v_x = self.v_x_next
        self.v_y = self.v_y_next
    def resetL (self,L):
        self.l0 = L -1


Balls = [ Ball ( 1 , -1 , 0 ) , Ball ( 2 , 1 , 0 ) ]
for ball_1 in Balls:
    for ball_2 in Balls:
        if ( ball_2.id != ball_1.id ):
            ball_1.Bounds.append ( ball_2 )

NSteps = 100

for step in range (0, NSteps):
    print("Step:",step)
    for ball in Balls:
        print( [ ball.x , ball.y ] )
        ball.setCurrentAx()
        ball.setNextCords()
    for ball in Balls:
        ball.setNextAx()
        ball.setNextVel()
    for ball in Balls:
        ball.update()
