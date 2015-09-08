# finding prime factors
# Trial division maybe?

from math import sqrt, floor
myNum = 600851475143
halfway = int(floor(sqrt(myNum)))
print(sqrt(600851475143))
factorsOfNum = []
for possible in range(2, halfway):
    if myNum % possible == 0:
        # prime factor
        factorsOfNum.append(possible)

maxFactor = 0
print("Factors of number")
print(factorsOfNum)
# check factors for primality
for factor in factorsOfNum:
    for x in range(2, floor(sqrt(factor))):
        if factor % x == 0:
            # not prime
            break
    else:
        maxFactor = factor


print(str(maxFactor) + " is the largest prime factor")
