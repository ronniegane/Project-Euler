'''Project Euler problem 20: factorial digit sum
find the sum of the digits in the numebr 100!'''


def fact(x):
    '''Calculate factorial of x, also written x!'''
    product = 1
    index = x
    while index > 1:
        product *= index
        index -= 1
    return product

n = 100
bigFact = fact(n)
strFact = str(bigFact)
digitSum = 0

for i in range(len(strFact)):
    digitSum += int(strFact[i])

print("Sum of digits in %s! is %s" % (n, digitSum))
