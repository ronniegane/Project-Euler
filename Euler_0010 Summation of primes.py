'''Project Euler problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

from math import sqrt, floor

def isPrime(a):
    '''Returns True if a number is prime, False if not
    (calculated through trial division)'''
    for x in range(2, int(floor(sqrt(a)))+1):
        if a % x == 0:
            #not prime
            return False
    return True

# print ("7 " + str(isPrime(7)))
# print ("4 " + str(isPrime(4)))

# Finding the nth prime
def findNthPrime(nth):
    '''Returns the nth prime starting from 2 as the first prime onwards'''
    index = 2
    primes = []
    nth = 10001
    # brute force
    while len(primes) < nth:
        # check next number
        if isPrime(index):
            primes.append(index)
        index +=1

    print("List of primes:")
    print(primes)
    print(primes[-1]) # print the last entry in primes array

def findPrimesUpTo(maxNum):
    '''Finds primes below a certain number and returns a list.'''
    primes = []
    index = 2
    # currently just naively checking. Could do a lot better with a sieve of Eratosthenes.
    while index <= maxNum:
        if isPrime(index):
            primes.append(index)
        index +=1

    return primes

print(sum(findPrimesUpTo(2000000)))
