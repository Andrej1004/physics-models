import math

def calcE (S,J,H):
    E = 0
    n_x = len(S)-1
    n_y = len(S[1])-1
    for i in range(0,n_x):
        for j in range(0,n_y):
            if (j < n_y):
                E += -0.5*J*(math.cos(S[i][j])*math.cos(S[i][j+1])+math.sin(S[i][j])*math.sin(S[i][j+1]))
            if (j > 0):
                E += -0.5*J*(math.cos(S[i][j])*math.cos(S[i][j-1])+math.sin(S[i][j])*math.sin(S[i][j-1]))
            if (i < n_x):
                E += -0.5*J*(math.cos(S[i][j])*math.cos(S[i+1][j])+math.sin(S[i][j])*math.sin(S[i+1][j]))
            if (i > 0):
                E += -0.5*J*(math.cos(S[i][j])*math.cos(S[i-1][j])+math.sin(S[i][j])*math.sin(S[i-1][j]))
            E = E-H*math.cos(S[i][j])
    return E

def Echange (S,J,H,i,j):
    deltaE = 0
    n_x = len(S)-1
    n_y = len(S[1])-1
    if (j < n_y):
        deltaE += -J*(math.cos(S[i][j])*math.cos(S[i][j+1])+math.sin(S[i][j])*math.sin(S[i][j+1]))
    if (j > 0):
        deltaE += -J*(math.cos(S[i][j])*math.cos(S[i][j-1])+math.sin(S[i][j])*math.sin(S[i][j-1]))
    if (i < n_x):
        deltaE += -J*(math.cos(S[i][j])*math.cos(S[i+1][j])+math.sin(S[i][j])*math.sin(S[i+1][j]))
    if (i > 0):
        deltaE += -J*(math.cos(S[i][j])*math.cos(S[i-1][j])+math.sin(S[i][j])*math.sin(S[i-1][j]))
    deltaE = deltaE-H*math.cos(S[i][j])
    return deltaE
