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
# calculating primes below 1,000,000 only takes 0.28 seconds, so not a huge bottleneck

from math import sqrt

# Timing code
import time
start_time = time.time()

# SEARCH PARAMETERS
primeMax = 1000000
minSize = 183

# create ordered list of primes
# Seive of Erastothenes approach
# Start with all numbers 2-1million (or other maximum)

mySieve = [False,False,True]+[True, False]*primeMax # all odd numbers and 2 start as prime

for i in range(3,int(sqrt(primeMax))+1,2):
    if mySieve[i]:
        for mult in range(2*i, primeMax, i):
            mySieve[mult] = False

primeList = [2] + [i for i in range(3, primeMax, 2) if mySieve[i]]
primeSet = set(primeList)  # Create a set for checking if a sum is prime

print("Primes up to %s: found %s primes" % (primeMax, len(primeList)))
print("---Completed in %s seconds---" %(time.time() - start_time))

# Making a dictionary for lookup
# primeDict = {x: mySieve[x] for x in range(primeMax)}
# Dictionaries don't work well because there are many values we try to lookup outside the prime range

'''
There are 78498 primes below 1 million.

BUT, we want our summed prime to be 1 million or below.
So really the maximum "end number" of our sequence
is one where it and the 20 previous numbers is just under a million, because we know
our max length of consecutive primes must be >= 21

This leaves us with 5144 primes.


number of possible consecutive combinations:
1 @ 5144 sequential numbers
2 @ 5143
3 @ 5142
...
5144 @ 1

so sum of 1 to n = n(n+1)/2 which in our case means
that we have 5144*5145/2 = 13,232,940 sequences to sum up and check.

If we use knowledge from prime sum under 100,000 we know we are looking for a
sequence of length >= 183, so we can put this as our minSize.
This cuts down the number of primes to cycle through to 818, which
means just 334,971 sequences to check.


The longest consecutive sequence for each max length:
100:
[2, 3, 5, 7, 11, 13]
6 primes with total sum: 41

1000:
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
21 primes with total sum: 953

10,000:
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
65 primes with total sum: 9521

100,000:
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]
183 primes with total sum: 92951

Maximum length sum of primes that is also prime below 1000000:
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931]
543 primes with total sum: 997651

Since we're looking for the longest consecutive sequence,
if we start with the longest possible sequence and loop through
making shorter sequences each time,
we can stop at the first one we find. 
'''


primeSums = [sum(primeList[x-minSize:x-1]) for x in range(minSize,len(primeList)+1)]
upToMax = [x for x in primeSums if (x < primeMax)]
primeIndex = len(upToMax)+minSize

print("Only need to consider first %s primes if sum < %s" % (primeIndex, primeMax))

# Trim primeList
primeList = primeList[:primeIndex]


start_time = time.time()

maxLen = len(primeList)

for seqSize in range(maxLen, 0, -1):

    sumList = [sum(primeList[a-seqSize:a]) for a in range(seqSize, maxLen+1)]

    if sumList[0] > primeMax:  # ignore this list if the smallest sum is still bigger than maximum prime
        continue

    offset = [sumList.index(x) for x in sumList if ((x < primeMax) and (x in primeSet))]

    if len(offset) > 0:
        # Found max sum
        maxList = primeList[offset[-1]:offset[-1]+seqSize]
        maxSum = sumList[offset[-1]]
        break
    else:
        continue
    break # Will exit the outer loop if the inner loop breaks

print("Maximum length sum of primes that is also prime below %s:" % primeMax)
print(maxList)
print("%s primes with total sum: %s " % (len(maxList),maxSum))
print("---Completed in %s seconds---" %(time.time() - start_time))




'''Time performance:
n       primeList    maxList  maxList(sets) maxList (dict) list comp
100       0.0156      0.0312   0.006                       -
1000      0.0156      0.1404   0.062                     0.001
10000     0.0156     14.2964   3.603        3.6604          0.002
100000    0.1248        -        -                      0.772
1000000

currently max list time is O(n**2) with n being max number.
the number of primes below n is roughly O(n) so 
'''
