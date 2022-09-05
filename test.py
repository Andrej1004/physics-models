import random
import math

def calcE (S,J,H):
    E = 0
    for i in range(0,len(S)):
        for j in range(0,len(S[0])):
            if (i!=0 and i<(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
                E = E-J*(math.cos(S[i][j])*math.cos(S[i-1][j])+math.sin(S[i][j])*math.sin(S[i-1][j])+
                         math.cos(S[i][j])*math.cos(S[i+1][j])+math.sin(S[i][j])*math.sin(S[i+1][j])+
                         math.cos(S[i][j])*math.cos(S[i][j-1])+math.sin(S[i][j])*math.sin(S[i][j-1])+
                         math.cos(S[i][j])*math.cos(S[i][j+1])+math.sin(S[i][j])*math.sin(S[i][j+1]))
            E = E-H*math.cos(S[i][j])
    return E

def Echange (S,J,H,i,j):
    deltaE = 0
    if (i!=0 and i<(len(S)-1)) and (j!=0 and j<(len(S[0])-1)):
        deltaE = -J*(math.cos(S[i][j])*math.cos(S[i-1][j])+math.sin(S[i][j])*math.sin(S[i-1][j])+
                     math.cos(S[i][j])*math.cos(S[i+1][j])+math.sin(S[i][j])*math.sin(S[i+1][j])+
                     math.cos(S[i][j])*math.cos(S[i][j-1])+math.sin(S[i][j])*math.sin(S[i][j-1])+
                     math.cos(S[i][j])*math.cos(S[i][j+1])+math.sin(S[i][j])*math.sin(S[i][j+1]))
    deltaE = deltaE-H*math.cos(S[i][j])
    return deltaE

def makeSys (nx,ny):
    X = []
    Y = []
    for i in range(0,nx):
        for j in range(0,ny):
            Y.append(2*math.pi*random.random())
        X.append(Y)
        Y = []
    return X

def Run(S,J,H,T,nstep):
    nx = len(S)
    ny = len(S[0])
    E = calcE(S,J,H)
    E0 = E
    for n in range(0,nstep):
        i,j = random.randint(0,nx-1),random.randint(0,ny-1)
        S0 = S[i][j]
        deltaE0 = Echange(S,J,H,i,j)
        S[i][j]=2*math.pi*random.random()
        deltaE = Echange(S,J,H,i,j)
        if (deltaE<=0):
            E=E-deltaE0+deltaE
            #print(E,energyXY.calcE(S,J,H))
        elif (deltaE>0):
            rnd = random.random()
            exp = math.exp(-deltaE/T)
            if (rnd<=exp):
                E=E-deltaE0+deltaE
                #print(E0,E,2*deltaE,rnd,exp)
            else:
                S[i][j]=S0
    '''print('')
    print('')
    print('')'''
    print("E_start",E0,"E_end=",E)
    #print(energyXY.calcE(S,J,H),deltaE)
    return S

def printToFile (S,T,name):
    file = open(name,'a')
    data=""
    toFile = "T: "+str(T)+"\n"+"xy:\n"
    file.write(toFile)
    toFile = ""
    for i in S:
        for j in i:
            data += str(j)+" "
        data = data[0:len(data)-1]
        toFile += data+'\n'
        data=""
    file.write(toFile)
    toFile = "end\n"
    file.write(toFile)
    file.close()

def StartCalc(nx, ny, J, H, TStart, TEnd, DT, NSteps):
    name = str(TStart)+"-"+str(TEnd)+"-"+str(DT)+".xy"
    T = TStart
    S = makeSys(nx,ny)
    #Is.printSys(S)
    print("Начальная энергия:", calcE(S,J,H))
    while T <= TEnd:
        S = Run(S,J,H,T,NSteps)
        '''print("{")
        Is.printSys(S)
        print("}")'''
        printToFile(S,T,name)
        T += DT

StartCalc(100,100,10,0,0.001,0.5,0.01,5000000)
