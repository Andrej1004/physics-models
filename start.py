import Ising_2d as Is
from sys import argv

def StartCalc(model,nx, ny, J, H, TStart, TEnd, DT, NSteps):
    name = str(TStart)+"-"+str(TEnd)+"-"+str(DT)+".xy"
    T = TStart
    S = Is.makeSys(nx,ny)
    #Is.printSys(S)
    print("Начальная энергия:", Is.CalcE(S,J,H))
    if (T==TStart):
        Is.prinModel(model,name)
    while T <= TEnd:
        S = Is.Run(S,J,H,T,NSteps)
        '''print("{")
        Is.printSys(S)
        print("}")'''
        Is.printToFile(S,T,name)
        T += DT

try:
    script, model, nx, ny, J, H, TStart, TEnd, DT, NSteps = argv
    StartCalc(model,int(nx),int(ny),float(J),float(H),float(TStart),float(TEnd),float(DT),int(NSteps))
    print("END")
except ValueError:
    print(argv)
    print("вы ввели некорректные значения")
