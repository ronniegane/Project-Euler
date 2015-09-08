# sum of squares of natural numbers vs square of sum

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
