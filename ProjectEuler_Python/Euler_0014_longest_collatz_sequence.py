'''Longest Collatz Sequence
n -> n/2 if n is even
n -> 3n + 1 if n is odd
which starting number n < 1 million gives the longest chain?'''

# naive approach : exhaustive search
# Cache a global dictionary of collatz sequence lengths for known numbers to speed things up
# if the dictionary already exists, do not make it
if 'collatzDict' not in globals():
    collatzDict = {1: 1}

def collatz(n):
    '''Produces the Collatz sequence length for starting number n'''
    originN = n
    colLength = 0
    intermediates = {}
    while 1==1:
        # if the current number is in the dictionary, do lookup
        if n in collatzDict:
            '''About a billion times faster to use "if n in dict" instead of
                "if n in dict.keys()"'''
            colLength += collatzDict[n]
            # record the new length to the dictionary
            collatzDict[originN] = colLength
            # record the lengths of the intermediates to the dictionary
            for number in intermediates.keys():
                collatzDict[number] = colLength - intermediates[number]
            return colLength
        elif n % 2 == 0:
            # even number
            # add to intermediates
            intermediates[n] = colLength
            n /= 2
            colLength +=1
        else:
            # odd number
            # add to intermediates
            intermediates[n] = colLength
            n = 3*n + 1
            colLength +=1

# want to cache intermediate numbers as well, ideally, to speed up dictionary build

# Testing collatz function

# check dictionary
print("dictionary")
print(collatzDict)
print("collatz length of 1 is %s" % collatz(1))
# should be 1 = 1
print("dictionary")
print(collatzDict)
print("collatz length of 5 is %s" % collatz(5))
# should be 5->16->8->4->2->1 = 6
print("dictionary")
print(collatzDict)
print("collatz length of 10 is %s" % collatz(10))
# should be 10->5->16->8->4->2->1 = 7
print("dictionary")
print(collatzDict)
print("collatz length of 3 is %s" % collatz(3))
# should be 3->10->5->16->8->4->2->1 = 8
print("dictionary")
print(collatzDict)

# main function: search numbers from 1 to 1 million for collatz length
maxChain = 0
maxStart = 0
for i in range(1, 1000001):
    chain = collatz(i)
    if chain > maxChain:
        # new longest chain
        maxChain = chain
        maxStart = i
        print("Max chain length is %s with starting number %s" % (maxChain, maxStart))
        print("Dictionary has %s entries" % len(collatzDict))
