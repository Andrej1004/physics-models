import random
# создать начальную конфигурацию спинов
def makesys (nx,ny):
    X = []
    Y = []
    for i in range(0,nx):
        for j in range(0,ny):
            Y.append(2*random.randint(0,1)-1)
        X.append(Y)
        Y = []
    return X
# вывести конфигурацию на консоль
def printsys (S):
    for i in S:
        for j in i:
                print(j,end="")
        print()
# Запись в файл
def printtofile (S,T,name):
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
# указать модель
def prinmodel (model,name):
    file = open(name,'a')
    toFile = "M: "+model+"\n"
    file.write(toFile)
    file.close()
