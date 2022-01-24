a = [2,6]
b = [16,32,64,96]

# return a bloody 3?

def findFactors(n):
    f = []
    for i in range(2,n):
        if n % i == 0:
            f.append(i)
    return f

for i in b:
    print(i, findFactors(i))