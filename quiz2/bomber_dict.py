#  Bomber Man clean from scratch with dictionaries

g = ['...','.O.','...']

r = len(g)
c = len(g[0])

def show(g):
    for row in g:
        print(row)

def showHash(d):
    display = []
    for i in range(r):
        row = ''
        for j in range(c):
            if d.get((i,j)):
                row += 'O'
            else:
                row+= '.'
        display.append(row)
    for row in display:
        print(row)

def toHash(g):
    d = {}
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == 'O':
                d[(row,col)] = True
    return d

def new(g):
    d = {}
    for row in range(r):
        for col in range(c):
            if not g.get((row,col)):
                d[(row,col)] = True
    return d

print(g)
show(g)
b_old = toHash(g)
print(b_old)
b_new = new(b_old)
print('Old', b_old)
print('New', b_new)
showHash(b_old)