'''Project Euler Problem 39: Integer Right Triangles
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly
three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'''

def rightTriangles(p):
    '''Returns the number of possible right angled triangles and their dimensions,
    given a total perimeter p.'''
    # we have to have c>b>=a
    countSols = 0
    triangles = []
    # loop through values of a
    for a in range(1,p/2+1): # only need to go halfway to avoid repeating calcs
        # loop through values of b
        for b in range(1,p-a):
            # c is determined by the first two
            c = a-b-c
            # check if right angled
            if (c**2) == (a**2 + b**2):
                countSols+=1
                triangles.append((a,b,c)) # record the possible triangles
    return countSols, triangles

# main loop
maxSols = 0
bestP = 0
bestTris = []

for perim in range(3,1000):
    count, tris = rightTriangles(perim)
    if count > maxSols:
        maxSols = count
        bestTris = tris
        bestP = perim

print("Max solutions is %s at total perimeter of %s." % (maxSols, bestP))
print("Solutions are:")
print(bestTris)
