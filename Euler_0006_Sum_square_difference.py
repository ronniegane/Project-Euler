'''Project Euler 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.'''

maxN = 100
sumSquare = 0
squareSum = 0
for x in range(1, maxN+1):
    sumSquare += x
    squareSum += x**2

sumSquare = sumSquare ** 2

print("The sum of squares is " + str(squareSum))
print("The square of the sum is " + str(sumSquare))
difference = sumSquare - squareSum
print("The difference is " + str(difference))
