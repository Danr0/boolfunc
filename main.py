import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def to_bin(x, n):
    d = bin(x)[2:]
    return '0'*(n-len(d))+d

def contiguity(a,b):
    t = str(int(a)+int(b))
    s = 0
    for i in range(0,len(t)):
        if t[i] == '1':
                s+=1
    if (s==1):
        return True
    return False

def geom1():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),0,0,c="black")
        else:
            ax.scatter(int(tmp[0]),0,0,c="red")
        ax.text(int(tmp[0]),0,0+0.01, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [0,0],zs=[0,0],color='grey')
    fig.savefig('geom.png')

def graph1():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),0,0,c="black")
        else:
            ax.scatter(int(tmp[0]),0,0,c="red")
        ax.text(int(tmp[0]),0,0+0.01, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if data[fir]==1 and data[sec]==1 and contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [0,0],zs=[0,0],color='grey')
    fig.savefig('graph.png')

def geom2():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1]),0,c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1]),0,c="red")
        ax.text(int(tmp[0]),int(tmp[1]),0+0.01, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1]),int(sec[1])],zs=[0,0],color='grey')
    fig.savefig('geom.png')

def graph2():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1]),0,c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1]),0,c="red")
        ax.text(int(tmp[0]),int(tmp[1]),0+0.01, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if data[fir]==1 and data[sec]==1 and contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1]),int(sec[1])],zs=[0,0],color='grey')
    fig.savefig('graph.png')    
    
def geom3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1]),int(tmp[2]),c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1]),int(tmp[2]),c="red")
        ax.text(int(tmp[0]),int(tmp[1]),int(tmp[2])+textd, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1]),int(sec[1])],zs=[int(fir[2]),int(sec[2])],color='grey')
    fig.savefig('geom.png')

def graph3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1]),int(tmp[2]),c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1]),int(tmp[2]),c="red")
        ax.text(int(tmp[0]),int(tmp[1]),int(tmp[2])+textd, tmp)
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if data[fir]==1 and data[sec]==1 and contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1]),int(sec[1])],zs=[int(fir[2]),int(sec[2])],color='grey')
    fig.savefig('graph.png')
    

def geom4():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+d*int(tmp[3]),c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+d*int(tmp[3]),c="red")
        ax.text(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+textd+d*int(tmp[3]), tmp)         
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1])+d*int(fir[3]),int(sec[1])+d*int(sec[3])],zs=[int(fir[2])+d*int(fir[3]),int(sec[2])+d*int(sec[3])],color='grey')
    fig.savefig('geom.png')
    
def graph4():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,2**N):
        tmp=to_bin(i,N)
        if(data[tmp]==1):
            ax.scatter(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+d*int(tmp[3]),c="black")
        else:
            ax.scatter(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+d*int(tmp[3]),c="red")
        ax.text(int(tmp[0]),int(tmp[1])+d*int(tmp[3]),int(tmp[2])+textd+d*int(tmp[3]), tmp) 
    for i in range(0,2**N):
        for j in range(i+1,2**N):
            fir = to_bin(i,N)
            sec = to_bin(j,N)
            if data[fir]==1 and data[sec]==1 and contiguity(fir,sec):
                ax.plot([int(fir[0]),int(sec[0])], [int(fir[1])+d*int(fir[3]),int(sec[1])+d*int(sec[3])],zs=[int(fir[2])+d*int(fir[3]),int(sec[2])+d*int(sec[3])],color='grey')
    fig.savefig('graph.png')


d=0.5
textd=0.1
data = dict()
N=0
while N == 0:
    print('Enter a vector of Boolean function values')
    inp=input()
    for i in range(5):
        if len(inp)==2**i:
            N=i
            for i in inp:
                if i!='1' and i!='0':
                    N=0

for i in range(0,2**N):
    data[to_bin(i,N)]=int(inp[i])
    
for i in range(0,2**N):
    for j in range(i+1,2**N):
        fir = to_bin(i,N)
        sec = to_bin(j,N)
        if data[fir]==1 and data[sec]==1 and contiguity(fir,sec):
            ax.plot([fir[0],sec[0]], [0,0],zs=[0,0])

if N == 1: 
    geom1()
    graph1()
elif N == 2:
    geom2()
    graph2()
elif N==3:
    geom3()
    graph3()
elif N==4:
    geom4()
    graph4()

print('Images in graph.png and geom.png')
