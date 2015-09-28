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



# create ordered list of primes
# Seive of Erastothenes approach
# Start with all numbers 2-1million
primeMax = 100
primeList = list(range(2,primeMax+1))
index = 0
while index < len(primeList):
    pNum = primeList[index] # this will be the next prime number
    for nonPrime in range(2*pNum, primeMax+1, pNum):
        # Remove all multiples of this number from the list
        if nonPrime in primeList:
            primeList.remove(nonPrime)
    index += 1

print(primeList)
    


# read primes from disk into list
