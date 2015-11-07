'''Project Euler Problem 28: Number spiral diagonals
Starting with the number 1 and moving to the right in
a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
'''

# the pattern seems to be: start at 1, add 2, 2, 2, 2, then 4, 4, 4, 4, then 6, 6, 6, 6,...
# and square grows 1x1 -> 3x3 -> 5x5... odd numbers with the square as the last number

size = 1001 # side length of the square

count = 1 # start at 1
currentNum = 1
addNum = 2 # At first, add two to the count for each corner

for currentSize in range(3,size+1, 2):
    for i in range(4):
        currentNum += addNum
        count += currentNum
    addNum += 2

print(count)



