import makesys
import energy
import random
import math

def run(S,J,H,T,nstep):
    nx = len(S)
    ny = len(S[0])
    E = energy.calcE(S,J,H)
    E0 = E
    for n in range(0,nstep):
        X = [[0,0,0],
             [0,0,0],
             [0,0,0]]
        i,j = random.randint(0,nx-1),random.randint(0,ny-1)
        S[i][j]=-S[i][j]
        if (i>0):
            X[0][1] = S[i-1][j]
        if (i<nx-1):
            X[2][1] = S[i+1][j]
        if (j>0):
            X[1][0] = S[i][j-1]
        if (j<ny-1):
            X[1][2] = S[i][j+1]
        X[1][1] = S[i][j]
        deltaE = energy.Echange(X,J,H,1,1)
        if (deltaE<=0):
            E=E+2*deltaE
            #print(E0,E,)
        elif (deltaE>0):
            rnd = random.random()
            exp = math.exp(-deltaE/T)
            if (rnd<=exp):
                E=E+2*deltaE
                #print(E0,E,2*deltaE,rnd,exp)
            else:
                S[i][j]=-S[i][j]
        #print("step",n,"E_=",E)
    '''print('')
    print('')
    print('')'''
    print("E_start",E0,"E_end=",E)
    #print(energy.calcE(S,J,H),deltaE)
    return S



