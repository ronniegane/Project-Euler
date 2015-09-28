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
primeMax = 10000

mySieve = [True]*primeMax # all numbers start as prime

for i in range(3,int(sqrt(primeMax))+1,2):
    if mySieve[i]:
        for mult in range(2*i, primeMax, i):
            mySieve[mult] = False

primeList = [2] + [i for i in range(3, primeMax, 2) if mySieve[i]]

print("Primes up to %s: found %s primes" % (primeMax, len(primeList)))
print("---Completed in %s seconds---" %(time.time() - start_time))

# print(primeList[-50:])

''' there are 78498 primes below 1 million.
number of possible consecutive combinations:
1 @ 78498 sequential numbers
2 @ 78497
3 @ 78496
...
78498 @ 1

so sum of 1 to n = n(n+1)/2 which in our case means
that we have 78498*78499/2 = 3,081,007,251 sequences to sum up and check.

for primeMax = 1000, there are 168 primes,
so 14,196 sequences to sum up and check.

Since we're looking for the longest consecutive sequence,
if we start with the longest possible sequence and loop through
making shorter sequences each time,
we can stop at the first one we find. 
'''

start_time = time.time()
maxLen = len(primeList)
maxSum = 0

for seqSize in range(maxLen,0,-1):
    for offset in range(maxLen-seqSize+1):
        if offset == 0:
            thisList = primeList[-seqSize:]
        else:            
            thisList = primeList[-offset-seqSize:-offset] # has problems when offset = 0
           
        thisSum = sum(thisList)
        #if seqSize == 6:
            #print(thisList)
            #print("Checking %s length sequence at offset %s: sum %s" % (seqSize, offset, thisSum))
        #print(thisSum)

        if thisSum in primeList:  # getting the right sums, but not recognising them as prime
            # thisSum is a prime
            maxSum = thisSum
            maxList = thisList
            break
    else:
        continue
    break # Will exit the outer loop if the inner loop breaks

print("Maximum length sum of primes that is also prime below %s:" % primeMax)
print(maxList)
print("%s primes with total sum: %s " % (len(maxList),maxSum))
print("---Completed in %s seconds---" %(time.time() - start_time))




'''Time performance:
n       primeList    maxList
100       0.0156      0.0312
1000      0.0156      0.1404
10000     0.0156     14.2964
100000
1000000
'''
