'''Project Euler problem 27: Quadratic Primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes
for the consecutive values n = 0 to 39. However,
when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the
maximum number of primes for consecutive values of n,
starting with n = 0.'''


# Check primality (and build up a dictionary of primes for quick checking)
from math import sqrt, floor

primeDict = {}

def isPrime(a):
    '''Returns True if a number is prime, False if not
    (calculated through trial division)'''
    # numbers <=1 can't be prime
    global primeDict
    if a <= 1:
        primeDict[a] = False
        return False
    if a in primeDict: # if we have encountered this number before, save some time
        return primeDict[a]
    else:
        for x in range(2, int(floor(sqrt(a)))+1):
            if a % x == 0:
                #not prime
                # Record in dictionary
                primeDict[a] = False
                return False
        # Record in dictionary
        primeDict[a] = True
        return True

def main():
    maxN = 0
    maxA = 0
    maxB = 0

    # Loop through coefficients
    for b in range(1,1000): # note that b must be >1 otherwise the first result with n=0 is non-prime
        for a in range(-b,1000): # a must be > -b for n=1 =. 1 + a + b to make a prime >1
            # print("a: %s b: %s" % (a,b))
            # Work out the results of n**2 + an + b, stopping when a non-prime is found
            n = 0
            s = b
            while isPrime(s):
                # print("%s is a prime" % s)
                n += 1
                s = n**2 + a*n + b
            # Check if this is a new max
            #print("Reached %s consecutive primes." % n)
            if n > maxN:
                maxN = n
                maxA = a
                maxB = b
                print("New max N: %s with a = %s and b = %s" % (maxN, maxA, maxB))

    print("Product of the coefficients is %s" % (maxA*maxB))
    
if __name__ == '__main__':
    main()



