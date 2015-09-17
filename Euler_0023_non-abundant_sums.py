'''Project Euler problem 23: non-abundant sums
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the sum of
two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.'''

# find divisors
from math import sqrt, floor
def findDivisors(n):
    '''Returns a list of all divisors of n including n itself'''
    divisors = []
    for i in range(1, floor(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return divisors

# find sum of a numbers divisors
def divisorSum(n):
    myDivisors = findDivisors(n)
    myDivisors.remove(n)
    #print(myDivisors)
    return sum(myDivisors)

###Testing
##print("The sum of divisors of %s is %s" % (3, divisorSum(3)))
##print("The sum of divisors of %s is %s" % (4, divisorSum(4)))
##print("The sum of divisors of %s is %s" % (12, divisorSum(12)))
##print("The sum of divisors of %s is %s" % (28, divisorSum(28)))

abundantList = []
# build a list of abundant numbers from 1 to 28123
for x in range(1, 28124):
    if x < divisorSum(x):
        # x is abundant
        abundantList.append(x)

#print(abundantList)
print("there are %s abundant numbers." % len(abundantList))
'''There are 6965 abundant numbers in this list. Therefore there are 6965**2 = 48511225
possible combinations of two abundant numbers.'''

# start with a set of numbers
numSet = set(range(1,28124))
for i in range(len(abundantList)):
    for j in range(len(abundantList)):
        thisSum = abundantList[i] + abundantList[j]
        if thisSum in numSet:
            numSet.remove(thisSum)

print(numSet)
print("The sum of these numbers is %s" % sum(numSet))
        
