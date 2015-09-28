'''Project Euler Problem 50: Consecutive Prime Sums
The prime 41, can be written as the sum of six
consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that
adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum
of the most consecutive primes?'''

# naive approach: Work out all primes below 1 million first
# maybe cache this list to disk to keep around?
# if cached file is present, and checksum matches, then carry on
# otherwise, overwrite

from math import sqrt

# Timing code
import time
start_time = time.time()


# create ordered list of primes
# Seive of Erastothenes approach
# Start with all numbers 2-1million
primeMax = 1000000

mySieve = [True]*primeMax # all numbers start as prime

for i in range(3,int(sqrt(primeMax))+1,2):
    if mySieve[i]:
        for mult in range(2*i, primeMax, i):
            mySieve[mult] = False

primeList = [2] + [i for i in range(3, primeMax, 2) if mySieve[i]]

print("Primes up to %s: found %s primes" % (primeMax, len(primeList)))
print("---Completed in %s seconds---" %(time.time() - start_time))

''' there are 78498 primes below 1 million.
number of possible consecutive combinations:
1 x 78498 sequential numbers
2 x 78497
3 x 78496
...
78498 x 1'''

# stop if the current biggest number is larger than the largest
# possible sum of the current length

