'''Project Euler problem 16: power digits sum
2**15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26
what is the sum of the digits of 2**1000?'''

# naive approach
# try calculating 2**1000, see how it goes
bigNum = 2**1000
# convert to string and split
bigString = str(bigNum)
digitSum = 0
for i in range(len(bigString)):
    digitSum += int(bigString[i])

print("The sum of digits is %s" % digitSum)
