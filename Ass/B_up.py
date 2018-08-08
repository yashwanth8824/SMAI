import numpy as np
import random
import matplotlib.pyplot as plt
w1=[(2,7),(8,1),(7,5),(6,3),(7,8),(5,9),(4,5)]
w2=[(4,2),(-1,-1),(1,3),(3,-2),(5,3.25),(2,4),(7,1)]
Y_MAT=[[-1,-4,-2],[-1,1,1],[-1,-1,-3],[-1,-3,2],[-1,-5,-3.25],[-1,-2,-4],[-1,-7,-1],[1,2,7],[1,8,1],[1,7,5],[1,6,3],[1,7,8],[1,5,9],[1,4,5]]
#print Y_MAT
b=1000#margin
Str_WEI=[]
A_MAT=np.array(Y_MAT)
WEI_MAT=[1,-1,1]
WEI_MAT=np.array(WEI_MAT)
loop=100000
while loop:
    DotMat=np.dot(A_MAT,WEI_MAT)
    #print DotMat,'This is dot product------'
    Dot_Mat=A_MAT[DotMat<b]
    #print Dot_Mat,'This is values of y========'
    if len(Dot_Mat):
        WEI_MAT=WEI_MAT+Dot_Mat[random.randint(0,len(Dot_Mat)-1)]
        #print loop%100
        if int(loop%5000)==0:
            Str_WEI.append(WEI_MAT)
    else:
        break
    loop -=1
#print Str_WEI
Line_Mat_pt=[]#for storing weight matrix lines

x1=[]
y1=[]
x2=[]
y2=[]
for i in w1:
    x1.append(i[0])
    y1.append(i[1])
for i in w2:
    x2.append(i[0])
    y2.append(i[1])

_p1x=float(11)
_p2x=float(-3)
_p1y=float(_p1x*(float(-WEI_MAT[1])/WEI_MAT[2])+(float(-WEI_MAT[0])/WEI_MAT[2]))
_p2y=float(_p2x*(float(-WEI_MAT[1])/WEI_MAT[2])+(float(-WEI_MAT[0])/WEI_MAT[2]))

for i in Str_WEI:
    if i[2]!=0:
       _L1x=float(11)
       _L2x=float(-3)
       _L1y=float(_p1x*(float(-i[1])/i[2])+(float(-i[0])/i[2]))
       _L2y=float(_p2x*(float(-i[1])/i[2])+(float(-i[0])/i[2]))
       Line_Mat_pt.append([[_L1x,_L1y],[_L2x,_L2y]])

for i in Line_Mat_pt:
    plt.plot(i[0],i[1],'g--')

plt.scatter(x1,y1,color='r')
plt.scatter(x2,y2,color='b')
plt.plot([_p1x,_p1y],[_p2x,_p2y],'y--')
plt.show()
print WEI_MAT,loop
