'''Project Euler problem 25: 1000-digit Fibonacci number
What is the index of the first term in
the Fibonacci sequence to contain 1000 digits?'''

# Build a dictionary of fibonacci numbers as we go to improve time
fibDict = {}
def fib(n):
    if n <3:
        fibDict[n] = 1
        return 1
    else:
        fibSum = fibDict[n-1] + fibDict[n-2]
        # record this new value in the dictionary
        fibDict[n] = fibSum
        return fibSum

digs = 1000 # goal digits

i = 1
while len(str(fib(i))) < digs:
    i+=1

print("The %sth fibbonaci number has %s digits" % (i, digs))
