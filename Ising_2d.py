import makesys
import energy
import run

'''
создать двумерную решетку спинов Nx на Ny
с рандомной ориентацией спинов
'''
def makeSys(nx,ny):
    return makesys.makesys(nx,ny)
'''
вывести в консоль систему спинов
1 - ориентация вверх
-1 - ориентация вниз
'''
def printSys(S):
    makesys.printsys(S)
'''
вывести в консоль систему спинов
1 - ориентация вверх
-1 - ориентация вниз
'''
def printToFile(S,T,name):
    makesys.printtofile(S,T,name)
'''
посчитать энергию системы S
J - обменный интеграл
H - напряженность внешнего магнитного поля
'''
def CalcE(S,J,H):
    return energy.calcE(S,J,H)
'''
посчитать изменение энергии при переорентации одного спина
'''
def EChange(S,J,H,i,j):
    return energy.Echange(S,J,H,i,j)
'''
запустить моделирование МК-методом
на N шагов при заданной температуре
'''
def Run(S,J,H,T,nstep):
    return run.run(S,J,H,T,nstep)
'''
указать модель
'''
def prinModel (model,name):
    return makesys.prinmodel(model,name)
