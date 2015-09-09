'''Project Euler problem 22: Names scores
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''

# import names.txt into a list of strings
infile = open('p022_names.txt', 'r')
nameList = infile.read().replace('"',"").split(',')
nameList.sort() # put in alphabetical order
print(nameList[:10])

# make a dictionary for alphabetical scoring
alphaScore = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(alphabet)):
    alphaScore[alphabet[i]] = i+1

# print(alphaScore)

# score each name
scores = []
for name in nameList:
    pass

#close the file
infile.close()
