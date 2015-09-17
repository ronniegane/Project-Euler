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
from Euler_0027_Quadratic_Primes import isPrime


# Start with a list of primes up to 1 million
primeList = [str(x) for x in range(1000000) if isPrime(x)]

#print(primeList[:20])

# work through the primeList

leftTrunc = []
rightTrunc = []
bothTrunc = []

for prime in primeList:
    for index in range(1,len(prime)):
        left = prime[:-index]
        right = prime[index:]
        if (not isPrime(int(left))) or (not isPrime(int(right))):
            break
    else:
        bothTrunc.append(prime)

print(bothTrunc)

# sum up the last 11 of these
mySum = 0
for truncPrime in bothTrunc[-11:]:
    print(truncPrime)
    mySum += int(truncPrime)

print("Total sum is %s" % mySum)
