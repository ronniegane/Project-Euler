'''Project Euler problem 15: number of paths through a lattice
Lattice is size NxN and only choices at each fork are Right (R) and Down (D).
As we need N right movements and N down movements to get to the opposite corner,
we just need to find 40C20: choosing 20 of the 40 steps to be Right, and the rest to be Down.'''

'''(n choose k) is n! / (k! (n-k)!) which in this case is 40!/(20!)**2'''

def fact(x):
    '''Calculate factorial of x, also written x!'''
    product = 1
    index = x
    while index > 1:
        product *= index
        index -= 1
    return product

# testing
print(fact(1))
print(fact(3))
print(fact(10))

# main: find
n = 20 # size of square grid

numPaths = fact(2*n)// (fact(n))**2

print("There are %s possible paths in a %s x %s grid" % (numPaths, n, n))
