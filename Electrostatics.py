import math

class Charge:
    def __init__ (self,x,y,Q):
        self.x = x
        self.y = y
        self.Q = Q

class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.E = []

def E_field (charge , point):
    x1 , y1 , Q = charge.x , charge.y , charge.Q
    x2 , y2 = point.x , point.y
    r = pow ( pow(x2 - x1 , 2) + pow(y2 - y1 , 2) , 0.5)+0.0001
    return [ (x2 - x1) * Q / pow(r,3) , (y2 - y1) * Q / pow(r,3) ]

def calc_current_field (charges,points):
    E = [0,0]
    for point in points:
        for charge in charges:
            E_i = E_field (charge, point)
            E[0] += E_i[0]
            E[1] += E_i[1]
        E_val = pow( pow(E[0],2) + pow(E[1],2) , 0.5)
        if (E_val != 0):
            E[0] = E[0]/E_val
            E[1] = E[1]/E_val
        point.E = E
        #print(E)
        E = [0,0]
    print('done')
    return points

def create_points (x1 , x2 , y1 , y2 , nx , ny):
    dx = (x2 - x1) / nx
    dy = (y2 - y1) / ny
    points = []
    count = 0
    for i in range(0,nx):
        for j in range(0,ny):
            points.append(Point( x1 + i * dx , y1 + j * dy ))
            count += 1
    print(count,"poinst was created\n")
    return points

def create_charges (params):
    '''
    ожидаемый ввод:
    create_charges ([ [x1,y1,Q1],
                      [x2,y2,Q2],
                      ...
                      [xn,y,Qn]
                    ])
    '''
    charges = []
    count = 0
    for param in params:
        charges.append(Charge(param[0],param[1],param[2]))
        count += 1
    print(count,"charges was created\n")
    return charges

def write_to_file (points):
    f = open('field.txt','w')
    for point in points:
        f.write(str(point.x)+' '+str(point.y)+' '+str(point.E[0])+' '+str(point.E[1])+'\n')
    f.close()

