'''Project Euler problem 9: Special Pythagorean Triplet

Pythagorean triplets are (a, b, c) such that a**2 + b**2 = c**2
and a+b+c = N.
There is exactly one Pythagorean triplet where N = 1000.

can test code by looking for 3, 4, 5 triangle (N = 12)'''


N = 1000

# c**2 > a**2 + b**2 so a**2 + b**2 < N/2
#
myNums = []
for a in range(1, N+1):
    for b in range(a, N-a):
        c = N - a - b
        #print("a: %s ; b: %s ; c: %s" %(a, b, c))
        if a**2 + b**2 == c**2:
            myNums = [a, b, c]
            print("solution is:")
            print(myNums)
            break

