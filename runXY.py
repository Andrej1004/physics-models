import makesysXY
import energyXY
import random
import math

def run(S,J,H,T,nstep):
    nx = len(S)
    ny = len(S[0])
    E0 = energyXY.calcE(S,J,H)
    E = E0
    for n in range(0,nstep):
        X = [[0,0,0],
             [0,0,0],
             [0,0,0]]
        i,j = random.randint(0,nx-1),random.randint(0,ny-1)
        S0 = S[i][j]
        if (i>0):
            X[0][1] = S[i-1][j]
        if (i<nx-1):
            X[2][1] = S[i+1][j]
        if (j>0):
            X[1][0] = S[i][j-1]
        if (j<ny-1):
            X[1][2] = S[i][j+1]
        X[1][1] = S[i][j]
        deltaE0 = energyXY.Echange(X,J,H,1,1)
        S[i][j]=2*math.pi*random.random()
        X[1][1] = S[i][j]
        deltaE = energyXY.Echange(X,J,H,1,1)
        if (deltaE < deltaE0 or deltaE > 0):
            if (deltaE < 0):
                E=E-deltaE0+deltaE
                #print(E,energyXY.calcE(S,J,H))
            elif (deltaE > 0):
                rnd = random.random()
                exp = math.exp(-deltaE/T)
                if (rnd<=exp):
                    E=E-deltaE0+deltaE
                    #print(E0,E,2*deltaE,rnd,exp)'''
                else:
                    S[i][j]=S0
        else:
            S[i][j]=S0
    '''print('')
    print('')
    print('')'''
    print("E_start",E0,"E_end=",E)
    #print(energyXY.calcE(S,J,H),deltaE)
    return S



