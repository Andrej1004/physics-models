import random
import math
from tkinter import *

def create_system (n_x,n_y):
    Y,X = [], []
    for i in range(0,n_x):
        for j in range(0,n_y):
            Y.append(2*math.pi*random.random())
        X.append(Y)
        Y = []
    return X

def calc_energy (system):
    E = 0
    J = 10
    n_x = len(system)-1
    n_y = len(system[1])-1
    for i in range(0,n_x):
        for j in range(0,n_y):
            if (j < n_y):
                E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i][j+1])+math.sin(system[i][j])*math.sin(system[i][j+1]))
            if (j > 0):
                E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i][j-1])+math.sin(system[i][j])*math.sin(system[i][j-1]))
            if (i < n_x):
                E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i+1][j])+math.sin(system[i][j])*math.sin(system[i+1][j]))
            if (i > 0):
                E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i-1][j])+math.sin(system[i][j])*math.sin(system[i-1][j]))
    return E

def calc_delta (system,i,j):
    E = 0
    J = 10
    n_x = len(system)-1
    n_y = len(system[1])-1
    if (j < n_y):
        E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i][j+1])+math.sin(system[i][j])*math.sin(system[i][j+1]))
    if (j > 0):
        E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i][j-1])+math.sin(system[i][j])*math.sin(system[i][j-1]))
    if (i < n_x):
        E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i+1][j])+math.sin(system[i][j])*math.sin(system[i+1][j]))
    if (i > 0):
        E += -0.5*J*(math.cos(system[i][j])*math.cos(system[i-1][j])+math.sin(system[i][j])*math.sin(system[i-1][j]))
    return E

N = 10000000

S = create_system(50,50)
n_x = len(S)-1
n_y = len(S[1])-1

E0 = calc_energy(S)

for n in range (0,N):
    i = random.randint(0,n_x)
    j = random.randint(0,n_y)
    S0 = S[i][j]
    DE0 = calc_delta(S,i,j)
    S[i][j] = 2*math.pi*random.random()
    DE = calc_delta(S,i,j)
    if (DE < 0 and DE<DE0):
        E0 = E0 - DE0 + DE
        if (n % 1000 == 0):
            print(n,E0)
    else:
        S[i][j] = S0

root = Tk()
c = Canvas(root, width=800, height=800, bg='white')
c.pack()
c.delete("all")
r = 10
size = 10
for i in range(len(S)):
    for j in range(len(S[0])):
        if (0 < S[i][j] < math.pi/2):
            c.create_line(10+size*i,10+size*j,10+size*i+int(r*math.cos(S[i][j])),10+size*j+int(r*math.sin(S[i][j])),fill='black',arrow=LAST,arrowshape="3 3 3")
        elif (math.pi/2 < S[i][j] < math.pi):
            c.create_line(10+size*i,10+size*j,10+size*i+int(r*math.cos(S[i][j])),10+size*j+int(r*math.sin(S[i][j])),fill='red',arrow=LAST,arrowshape="3 3 3")
        elif (math.pi < S[i][j] < 3*math.pi/2):
            c.create_line(10+size*i,10+size*j,10+size*i+int(r*math.cos(S[i][j])),10+size*j+int(r*math.sin(S[i][j])),fill='blue',arrow=LAST,arrowshape="3 3 3")
        else:
            c.create_line(10+size*i,10+size*j,10+size*i+int(r*math.cos(S[i][j])),10+size*j+int(r*math.sin(S[i][j])),fill='green',arrow=LAST,arrowshape="3 3 3")
c.update()
root.mainloop()
