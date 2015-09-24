'''Project Euler problem 67: Maximum Path Sum II
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:'''

'''This reuses most of the code from problem 18.'''

# import big pyramid
infile = open('p067_triangle.txt')
triangle = []
for row in infile:
    triangle.append([int(s) for s in row.split()])    
#close the file
infile.close()

### Test triangle
##pyramid = '''
##3
##7 4
##2 4 6
##8 5 9 3'''.strip().split('\n')




 # map to int after splitting at whitespace

#print(triangle)

n = len(triangle) # height of triangle
index = 0

pathLen = triangle
for y in range (n-2, -1, -1): # start at one row from bottom of triangle and work upwards
    for x in range(y+1): # there are 'y' elements in the row 'y'
        # replace each element with the sum of itself and the max of the two elements below it
        pathLen[y][x] += max(pathLen[y+1][x], pathLen[y+1][x+1])

print("Maximum path sum is %s" % pathLen[0][0])


