import math

def calcE (S,J,H):
    E = 0
    for i in range(0,len(S)):
        for j in range(0,len(S[0])):
            if (i!=0 and i<(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
            if (i!=0 and i<(len(S)-1)) and (j==(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
            if (i!=0 and i<(len(S)-1)) and (j==0):
                E = E-0.5*J*(S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
            if (i==(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j])
            if (i==0) and (j!=0 and j<(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i+1][j])
            if (i==0) and (j==0):
                E = E-0.5*J*(S[i][j]*S[i][j+1]+S[i][j]*S[i+1][j])
            if (i==0) and (j==(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i+1][j])
            if (i==(len(S)-1)) and (j==0):
                E = E-0.5*J*(S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j])
            if (i==(len(S)-1)) and (j==(len(S[0])-1)):
                E = E-0.5*J*(S[i][j]*S[i][j-1]+S[i][j]*S[i-1][j])
            E = E-H*S[i][j]
    return E

def Echange (S,J,H,i,j):
    deltaE = 0
    if (i!=0 and i<(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
    if (i!=0 and i<(len(S)-1)) and (j==(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
    if (i!=0 and i<(len(S)-1)) and (j==0):
        deltaE = -J*(S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j])
    if (i==(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j])
    if (i==0) and (j!=0 and j<(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1]+S[i][j]*S[i+1][j])
    if (i==0) and (j==0):
        deltaE = -J*(S[i][j]*S[i][j+1]+S[i][j]*S[i+1][j])
    if (i==0) and (j==(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i+1][j])
    if (i==(len(S)-1)) and (j==0):
        deltaE = -J*(S[i][j]*S[i][j+1]+S[i][j]*S[i-1][j])
    if (i==(len(S)-1)) and (j==(len(S[0])-1)):
        deltaE = -J*(S[i][j]*S[i][j-1]+S[i][j]*S[i-1][j])
    deltaE = deltaE-H*S[i][j]
    return deltaE
