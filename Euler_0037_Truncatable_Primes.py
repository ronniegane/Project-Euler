'''Project Euler Problem 37: Truncatable Primes
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# Use isPrime code from previous works
import Euler_0027_Quadratic_Primes as eu
import time
start_time = time.time()


# Start with a list of primes up to 1 million. We use step = 2 to get only odd numbers
# primeSet = set([str(x) for x in range(1,1000000,2) if isPrime(x)])

# work through the primeList

leftTrunc = set([2,3,5,7])
rightTrunc = set([2,3,5,7])
bothTrunc = set()

# can't seem to make the dictionary building thing work when the script is imported

x = 11 # starting prime
while len(bothTrunc) < 11: # find 11 of these things
    x+= 2
    if eu.isPrime(x):
        prime = str(x)
        if len(prime) > 1: # ignore single digit primes
            for index in range(1,len(prime)):
                left = int(prime[index:]) # truncated from left to right
                right = int(prime[:-index]) #truncated from right to left
                # left truncated prime must be left-truncatable itself
                # and similar for right truncated primes - can we include this?
                if (not eu.isPrime(left)) or (not eu.isPrime(right)):
                    break
            else:
                bothTrunc.add(prime)

print(bothTrunc)

# sum up the last 11 of these
mySum = 0
for truncPrime in bothTrunc:
    print(truncPrime)
    mySum += int(truncPrime)

print("Total sum is %s" % mySum)

print("---Completed in %s seconds---" %(time.time() - start_time))
