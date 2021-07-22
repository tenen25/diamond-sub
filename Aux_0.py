import cmath
import math
import numpy as np

def phase(x, y):                               #Converts a float array of length 2 to complex array of length 2
    xPhas = complex(0, x )
    yPhas = complex(0, y )
    return  [xPhas, yPhas]

def Suffix(num):                               #Generates proper suffix to ordinal number
    if num<0 or not isinstance(num,int):
        suffix = "!NO!"
    elif num>=10 and num<21:
        suffix="th"
    else:
        while(num>=10):
            num=int(num%10)
        if num == 1: suffix = "st"
        elif num == 2: suffix = "nd"
        elif num == 3: suffix = "rd"
        else: suffix = "th"
    return suffix

def print_mat(mat, size):               # prints 2d array in a more pleasing manner
    for i in range(size):
        print(mat[i])

def to_tuple(arr):
    return tuple(map(tuple, arr))

def index_to_loc( ind, x, y):               # translated index in array to location on the x-y plane and returns string
    loca = np.array([0.0,0.0])
    loca[0] = x[ind[0]]
    loca[1] = y[ind[1]]
    stri = "("+ str(  round(loca[0] ,4) )+","+str( round(loca[1] ,4))+")"
    return stri