'''Finding factors of triangle numbers'''


def factors(n):
        '''Returns the factors of x as a list'''
        return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
# naive trial division factorising algorithm may be too slow, is order O(n)

# main: loop through triangle numbers
triangle = 1
index = 2
while len(factors(triangle)) <= 500:
    # keep searching
    triangle += index
    index += 1

print(triangle)
