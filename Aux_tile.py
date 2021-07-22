import numpy as np
from matplotlib import pyplot as plt
from Aux_0 import *

def BuiltTile(itera, start_tile):       #Generates the num-th iteration of the table tiling patch according to initial patch
    n=2
    table = start_tile
    wid = 2**itera
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    while n < wid:
        newTable = [['e' for x in range(2*n)] for y in range(2*n)]
        for k in range(n):
            for l in range(n):
                if table[k][l] == 0:
                    newTable[2*k][2*l] = 1
                    newTable[2*k][2*l +1] = 0
                    newTable[2*k + 1][2*l +1] = 3
                    newTable[2*k + 1][2*l] = 0
                    if n*2 == wid :
                      a_count = a_count + 2
                      b_count = b_count + 1
                      d_count = d_count + 1
                elif table[k][l] == 1:
                    newTable[2*k][2*l] = 1
                    newTable[2*k][2*l +1] = 2
                    newTable[2*k + 1][2*l +1] = 1
                    newTable[2*k + 1][2*l] = 0
                    if n*2 == wid :
                      a_count = a_count + 1
                      b_count = b_count + 2
                      c_count = c_count + 1
                elif table[k][l] == 2:
                    newTable[2*k][2*l] = 1
                    newTable[2*k][2*l +1] = 2
                    newTable[2*k + 1][2*l +1] = 3
                    newTable[2*k + 1][2*l] = 2
                    if n*2 == wid :
                      b_count = b_count + 1
                      c_count = c_count + 2
                      d_count = d_count + 1
                elif table[k][l] == 3:
                    newTable[2*k][2*l] = 3
                    newTable[2*k][2*l +1] = 2
                    newTable[2*k + 1][2*l +1] = 3
                    newTable[2*k + 1][2*l] = 0
                    if n*2 == wid :
                      a_count = a_count + 1
                      c_count = c_count + 1
                      d_count = d_count + 2
        table = newTable.copy()
        n = n*2
    str(itera) + Suffix(itera) + " iterated tile"
    print("The staistics for the "+str(itera) +Suffix(itera) +" iterated is as follows:")
    print("Number of 'a' tiles is " + str(a_count))
    print("Number of 'b' tiles is " + str(b_count))
    print("Number of 'c' tiles is " + str(c_count))
    print("Number of 'd' tiles is " + str(d_count))
    return newTable

def gen_tile(itera, start_tile):
    file_name = str(itera) + Suffix(itera) + " iteration starting tile"
    tile = BuiltTile(itera, start_tile)
    textfile = open(file_name, "w")
    for element in tile:
        textfile.write(str(element) + "\n")
    np.savetxt(file_name + ".txt", tile, delimiter=",")

def subpatches(itera, tile_type, size):
    read_name = str(itera) + Suffix(itera) + " iteration starting tile"
                #+ str(tile_type)+Suffix(tile_type) + " starting tile"
    patch = np.loadtxt(read_name+".txt", delimiter=",")
    sub_patch = set()
    wid = 2**itera
    temp = np.zeros( (size,size) )
    for i in range(wid):
        for j in range(wid):
            for l in range(size):
                for k in range(size):
                    temp[l][k] = patch[(i+l)%wid][(j+k)%wid]
            temp2 = to_tuple(temp)
            sub_patch.add(temp2)
    write_name = str(size)+"x"+str(size)+ " subpatches of " + read_name
    sub_patch_list = list(sub_patch)
    textfile = open(write_name, "w")
    for element in  sub_patch_list:
        textfile.write(str(element) + "\n")
    textfile.close()
    return len(sub_patch)

def illegal_subpatch(itera, tile_type, size):
    if tile_type>2:
        if tile_type==3: tile_type='a'
        elif tile_type==4: tile_type='b'
        elif tile_type == 5: tile_type = 'c'
        elif tile_type == 6: tile_type = 'd'
    read_name = str(size)+"x"+str(size)+ " subpatches of "+str(itera) + Suffix(itera)\
                + " iteration," + str(tile_type) + " starting tile"
    file = open(read_name, "r")
    sub_patch_list = file.readlines()
    compare_name = str(size)+"x"+str(size)+ " subpatches of "+str(itera) + Suffix(itera)\
                   + " iteration," + str(1) + Suffix(1) + " starting tile"
    compare_list = open(compare_name, "r")
    sub_patch_set = set(sub_patch_list)
    compare_set = set(compare_list)
    illegal_set = sub_patch_set.difference(compare_set)
    illegal_list = list(illegal_set)
    write_name = str(size)+"x"+str(size)+ " subpatches of "+ str(tile_type)  \
     + " starting tile"+".txt"
    textfile = open(write_name, "w")
    for element in  illegal_list:
        textfile.write(str(element) + "\n")
    textfile.close()
    return len(illegal_list)

def print_tile(itera):
    start = itera
    fig, axs = plt.subplots()
    fig.suptitle(str(itera)+" iterated tile")
    read_name = str(itera)+Suffix(itera)+" iteration"+" starting tile"
    tile = np.loadtxt(read_name+".txt", delimiter=",")
    temp_arr = np.multiply(64, tile)
    plt.imshow(temp_arr, vmin=0, vmax=255)
    plt.show()
plt.show()