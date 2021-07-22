import math
import cmath
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from numpy import linalg as LA
from Aux_0 import *
from Aux_tile import *
from Aux_bands import *
from Aux_matrix import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import interactive


tile1 = [ [3,0],[2,1] ]

val1 = 0                      #assign potential value to letter 'a'
#9
val2 = 6*math.sqrt(2)         #assign potential value to letter 'b'
#19
val3 = 10*math.sqrt(3)       #assign potential value to letter 'c'
#29
val4 = 9*math.pi             #assign potential value to letter 'd'

start_tile = tile1
tileType = 1
itera = 3
res = 10
eig_num=0
init_itera=2
fin_itera=7
size = 2
tile_type=1

#for j in range(10,16):
    #gen_tile(j, start_tile)

#print_tile(itera)
temp = subpatches(itera, tile_type, size)
print(temp)

#Tile = BuiltTile(itera,start_tile)
#sample_numth_eig_new(itera, res, eig_num, start_tile)
#M=Op_Mat_NoPhase(itera, Tile)
#print_mat(M, 2**(2*itera) )

#spec_bands_gen(itera, res, start_tile)

#print_tot_band(init_itera, fin_itera, res, start_tile, tileType)