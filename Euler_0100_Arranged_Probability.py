'''Project Euler problem 100: Arranged probability
If a box contains twenty-one coloured discs,
composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that
the probability of taking two blue discs,
P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly
50% chance of taking two blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain
over 10**12 = 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.'''

# want B/T * (B-1)/(T-1) = 1/2 where B and T are whole numbers
# so T(T-1) = 2B(B-1)
# or in quadratic form with B constant:
# T**2 - T -2B(B-1) = 0
# Quadratic
# Loop up through numbers of B: B has to be odd
from math import sqrt, ceil, floor
T = 1
B = 1
while T < 10000000:
    coeff = 1 + 8 * (B**2 - B)
    # print(coeff)
    if (sqrt(coeff) % 2) - 1 < 0.00000001:
        #valid B and T
        T = (1 + sqrt(1+8*(B**2 - B)))/2
        if T % 1 <0.00000001:
            T = int(round(T,0))
            print("%s blue discs in %s total (%s red)" % (B, T, T-B))
    # increment
    B+=1

# TO DO:
# -Code is pretty slow for T > 10 m.
# -Different approach: treat as a solving algorithm like newton's method or
# whatever equivalent for 3D problems (as we are trying to solve a 3D quadratic)
# Could even just use binary approach for now
# Compare T and B and adjust to get fraction closer to a goal.
