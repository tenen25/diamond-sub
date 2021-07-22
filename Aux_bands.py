import math
import cmath
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from numpy import linalg as LA
from Aux_0 import *
from Aux_matrix import val1, val2, val3, val4
from Aux_matrix import sample_numth_eig_new

def spec_bands_gen(itera, res, start_tile):
        size = 2 ** (2 * itera)
        mat = sample_numth_eig_new(itera, res, 0, start_tile)
        file_name = str(itera)+Suffix(itera)+" spec bands, "+\
                    "diag "+str( round(val1,3) )+" "+str( round(val2,3) )+" " \
                    +str( round(val3,3) ) + " " + str( round(val4,3) )
        np.savetxt(file_name+".txt", mat, delimiter=',')

def print_tot_band(init_itera, fin_itera, res, start_tile, tileType):
    plt.xlabel('Spectrum values')
    plt.ylabel('Iteration number')
    plt.title("Tile "+str(tileType)+" spectrum, "+ str(init_itera)\
              +"-"+str(fin_itera-1)+" iterations")
    for l in range(init_itera, fin_itera):
        size = 2 ** (2 * l)
        file_name = str(l) + Suffix(l) + " spec bands, " + "diag " \
                    + str(round(val1, 3)) + " " + str(round(val2, 3)) + " " \
                    + str(round(val3, 3)) + " " + str(round(val4, 3))
        mat = np.loadtxt(file_name+".txt", delimiter=',')
        x = [[0.0 for j in range(2)] for i in range(size)]
        y = [0.0 for i in range(size)]
        for i in range(size):
            x[i] = np.linspace(mat[1][i], mat[0][i], 3)
            y[i] = [l for j in range(3)]
            plt.plot(x[i], y[i])
    plt.show()