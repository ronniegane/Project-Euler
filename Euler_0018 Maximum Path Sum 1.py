'''Project Euler problem 18: Maximum Path Sum I
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:'''

pyramid = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.strip().split('\n')

### Test triangle
##pyramid = '''
##3
##7 4
##2 4 6
##8 5 9 3'''.strip().split('\n')

# Pyramid is imported as a list of (row) strings
# print(pyramid)
# split up the rows
triangle = []
for row in pyramid:
    triangle.append([int(s) for s in row.split()]) # map to int after splitting at whitespace

#print(triangle)

n = len(triangle) # height of triangle
index = 0

pathLen = triangle
for y in range (n-2, -1, -1): # start at bottom of triangle and work upwards
    for x in range(y+1):
        # replace each element with the sum of itself and the max of the two elements below it
        pathLen[y][x] += max(pathLen[y+1][x], pathLen[y+1][x+1])

print(pathLen)
