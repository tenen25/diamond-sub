import math
import cmath
import numpy as np
from numpy import linalg as LA
from Aux_0 import *
from Aux_tile import BuiltTile

val1 = 0#0                      #assign potential value to letter 'a'
val2 = 6*math.sqrt(2)#9         #assign potential value to letter 'b'
val3 = 10*math.sqrt(3)#19       #assign potential value to letter 'c'
val4 = 9*math.pi#29             #assign potential value to letter 'd'

def SubDiag(lett):              #assign diagonal values to OpMat based on the tiling
    return{
        0 : val1,
        1 : val2,
        2 : val3,
        3 : val4
    }.get(lett, 0)

def Op_Mat_NoPhase(num, patch):     #Generates the Schroedinger operator into a square matrix
    wid= 2**(num)                   #wid denotes width of periodic patch
    size= wid**2                    #size generates the dimension of the operator matrix
    NewMat = [[0 for j in range(size)] for i in range(size)]
    for i in range(wid):
        for j in range(wid):
            if i != wid-1:
                NewMat[i*wid+j][(i+1)*wid+j] = 1
            if j != wid-1:
                NewMat[i*wid+j][i*wid+j+1] = 1
            if j != 0:
                NewMat[i*wid+j][i*wid+j-1] = 1
            if i != 0:
                NewMat[i*wid+j][(i-1)*wid+j] = 1
            NewMat[i * wid + j][i* wid + j] = SubDiag(patch[i][j])
    return NewMat

def Op_Mat_Phase(num, phase):     #Generates the Schroedinger operator into a square matrix
    wid= 2**(num)                 #wid denotes width of periodic patch
    size= wid**2                  #size generates the dimension of the operator matrix
    NewMat = [[0 for j in range(size)] for i in range(size)]
    for j in range(wid):
        NewMat[0*wid+j][wid*(wid-1)+j] = cmath.exp( phase[1]    )
        NewMat[(wid-1)*wid+j][0*wid+j] =  cmath.exp(- phase[1])
    for i in range(wid):
        NewMat[i*wid+0][i*wid+ wid-1] = cmath.exp(- phase[0])
        NewMat[i*wid+ wid-1][i*wid+0] = cmath.exp( phase[0])
    return NewMat

def sample_numth_eig_new(itera, res, num, start_tile): # iter is the iteration number,\
    # res is the sampling resolution, num is the eigenvlaue number
    x = np.linspace(-cmath.pi, cmath.pi, res+1 )
    y = np.linspace(-cmath.pi, cmath.pi, res+1 )
    size = 2**(2*itera)
    if num>size or num<0:
        print('num value is incorrect')
        return
    if num > 0:
        eig_mat = [[0 for a in range(res+1)] for b in range(res+1)  ]
    elif num == 0:
        eig_mat = [[0.0 for a in range(size)  ] for s in range(2)]
        #[ [[0 for a in range(res+1)] for b in range(res+1)  ] for j in range(size) ]
    Tile = BuiltTile(itera,start_tile)
    mat1 = np.array(Op_Mat_NoPhase(itera, Tile))
    for k in range(res+1):
        for l in range(res+1):
            mat2 = np.array( Op_Mat_Phase(itera,phase(x[k],y[l])) )
            mat = np.add(mat1, mat2)
            vect=LA.eigvalsh( mat )
            if num != 0:
                eig_mat[k][l] = vect[num - 1]
            elif num == 0:
                for  j in range(size):
                    if k==0 and l==0:
                        eig_mat[0][j] = vect[j]
                        eig_mat[1][j] = vect[j]
                    else:
                        eig_mat[0][j] = max(vect[j] , eig_mat[0][j] )
                        eig_mat[1][j] = min(vect[j], eig_mat[1][j])
                print("("+str(x[k])+","+str(y[l])+")"+" computed")
    return eig_mat