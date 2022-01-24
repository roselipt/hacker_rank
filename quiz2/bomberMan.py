# Bomber Man problem from HankerRank.com

import string


g = ['...', '.O.', '...']
h = []

def show(grid):
    for row in grid:
        print(row)

def showFromSet(grid, r, c):
    #display = [['.']*c]*r
    display = []
    for i in range(r):
        row = ['.']*c
        display.append(row)
    print(display)
    print(grid)
    for pair in grid:
        rowe, col = pair
        print(rowe, col)
        display[rowe][col] = '0'
    print(display)
    for row in display:
        row_str = ''.join(row)
        print(row_str)
    #print(display)

def countGrid(r,c):
    first = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(i*c+j)
        first.append(row)
    print (first)
    second = []
    for i in range(r):
        row = []
        for j in range(c):
            print('assigning', i*c+j)
            row.append(i*c+j)
        second.append(row)
    print(second)

def toSet(grid):
    s = set()
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        this_row = grid[row]
        for col in range(cols):
            if this_row[col] == 'O':
                s.add((row,col))
    return s

all = set()
for i in range(3):
    for j in range(3):
        all.add((i,j))

show(g)
g_as_set = toSet(g)
print(g_as_set)
print(all)
comp_g = all.difference(g_as_set)
print(comp_g)
print(all)
showFromSet(comp_g, 3, 3)
showFromSet(g_as_set,3,3)
countGrid(3,3)
#l = ['.','O','.']
#print(l, ''.join(l))