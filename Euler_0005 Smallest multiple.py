'''Project Euler problem 5: Smallest multiple
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?'''


# Greatest common divisor function (needed for finding LCM)
def gcd(a, b):
    ''' finds the greatest common divisor of two integers a and b using Euclidean algorithm. '''
    minNum = min(a,b)
    maxNum = max(a,b)

    while maxNum % minNum != 0:
        maxNum, minNum = minNum, maxNum - minNum * (maxNum//minNum)
        #print(minNum)
    return minNum

# print(gcd(12, 8))

# Lowest common multiple function
def lcm(a, b):
    ''' Finds the lowest common multiple of a and b'''
    return int(a*b/gcd(a, b))

# print(lcm(21, 6))

# go through from 1 to N
# first find lowest common multiple of 1 to 2, then of this LCM to 3, and so on

N = 20  # set this
myLCM = 1
for x in range(1, N+1):
    myLCM = lcm(myLCM, x)

print(myLCM)
