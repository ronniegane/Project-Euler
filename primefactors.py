'''Project Euler problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

# finding prime factors


from math import sqrt, floor
myNum = 600851475143
halfway = int(floor(sqrt(myNum)))

print(sqrt(600851475143))
factorsOfNum = []
for possible in range(2, halfway): # possible factors of myNum
    if myNum % possible == 0:
        #this is a factor, prime or otherwise
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
