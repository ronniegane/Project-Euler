'''Project Euler problem 523 - First Sort 1
Consider the following algorithm for sorting a list:

1. Starting from the beginning of the list, check each pair of adjacent elements in turn.
2. If the elements are out of order:
a. Move the smallest element of the pair at the beginning of the list.
b. Restart the process from step 1.
3. If all pairs are in order, stop.
For example, the list { 4 1 3 2 } is sorted as follows:

4 1 3 2 (4 and 1 are out of order so move 1 to the front of the list)
1 4 3 2 (4 and 3 are out of order so move 3 to the front of the list)
3 1 4 2 (3 and 1 are out of order so move 1 to the front of the list)
1 3 4 2 (4 and 2 are out of order so move 2 to the front of the list)
2 1 3 4 (2 and 1 are out of order so move 1 to the front of the list)
1 2 3 4 (The list is now sorted)
Let F(L) be the number of times step 2a is executed to sort list L. For example, F({ 4 1 3 2 }) = 5.

Let E(n) be the expected value of F(P) over all permutations P of the integers {1, 2, ..., n}.
You are given E(4) = 3.25 and E(10) = 115.725.

Find E(30). Give your answer rounded to two digits after the decimal point.'''
from itertools import permutations

stepDict = {} # working with dictionaries, the keys need to be a hashable type.
# this excludes lists, but allows tuples and strings

def sortTime(myList):
    '''Returns the time taken to sort the given list'''
    steps = 0
    index = 0
    # make sure myList is a list
    myList = tuple(myList)
    listCopy = myList
    maxIndex = len(myList)
    
    while index < maxIndex-1:
        # if we have seen this permutation before, use the dictionary value
        if myList in stepDict:
            steps += stepDict[myList]
            break
        elif myList[index] <= myList[index+1]:
            # in order, just move along
            index += 1
        else:
            # move smaller number (index+1) to front of list
            myList = (myList[index+1],)+myList[0:index+1]+myList[index+2:maxIndex]
            
            # Start from first position again
            index = 0
            # Add to the count of steps
            steps += 1
    # add this permutation to the dictionary
    stepDict[listCopy] = steps
    return steps

### Testing sortTime function
##testList = [4,1,3,2]
##index = 0
##print(sortTime(testList)) # should be 5

# finding expected value of permutations
def expectedSteps(n):
    '''expected steps to sort a list of 1-n'''
    # create list of permutations
    startList=range(1,n+1)
    permList = list(permutations(startList)) #permlist is a list of lists or list of tuples??
    #print("There are %s permutations" % len(permList))
    timeList = []
    counter = 0
    for perm in permList:
        timeList.append(sortTime(perm))
        if counter % 1000 == 0:
            # progress bar
            #print("%s permutations processed" % counter)
            counter += 1
    return sum(timeList)/len(timeList) # return average value

#print(expectedSteps(4)) #4! permutations which is 24
#print(expectedSteps(10)) #10! permutations is 3628800
#print(expectedSteps(30)) # 30! permutations which is 2.6525286e32

### looking for a pattern
##print(expectedSteps(2))
##print(expectedSteps(3))
##print(expectedSteps(4))
##print(expectedSteps(5))
##print(expectedSteps(6))
##print(expectedSteps(7))
##print(expectedSteps(8))
##print(expectedSteps(9))
##print(expectedSteps(10))

# putting data into excel, it very closely fits y = 0.2001e0.6513x
# what is significant about these numbers? is y = 0.2e0.65 close enough?
    
# takes a very long time even for 10 steps. There must be a way to improve.
# Have used a dictionary cache of permutation solve lengths, which greatly
# speeds up the process and makes n = 10 possible in ~15 seconds.
# Trying this approach with n=30 leads to a memory error- the number of
# permutations is just ridiculously large. 
'''Possible bottlenecks:
-doing tons of permutations: maybe there is some kind of pattern?
-Maybe cache/record numSteps for each permutation in a dictionary so if a
  permutation has been found before we can just add that number of steps
-Is list concatenation with + slow? Is there a faster alternative?
'''
