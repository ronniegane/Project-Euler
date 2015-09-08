'''Project Euler problem 21: Amicable numbers
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10,
11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''

from math import sqrt, floor
def findDivisors(n):
    '''Returns a list of all divisors of n including n itself'''
    divisors = []
    for i in range(1, floor(sqrt(n))+1):
        if n % i == 0:
            divisors.extend([i, n//i])
    return divisors

# Testing
print(findDivisors(8))
result = findDivisors(8)
result.remove(8)
print(result)
# .remove returns nonetype. modifies the actual list

# go through all numbers 1 to 999. Create a dictionary mapping d(x) to numbers
divSumDict = {}
amicableList = []
for x in range(2, 10000): # only valid from n>1 
    divisors = findDivisors(x)
    divisors.remove(x) # remove the number itself from divisors
    divSum = sum(divisors)
    newDivs = findDivisors(divSum)
    newDivs.remove(divSum)
    if sum(newDivs) == x and divSum != x:
        amicableList.append(x)
    divSumDict[x] = divSum

print(sum(amicableList))
for num in amicableList:
    print('%s has divisor sum %s' % (num, divSumDict[num]))
    


    
    
