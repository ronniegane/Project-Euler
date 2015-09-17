'''Project Euler problem 17: number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.'''

# Dictionary for looking up words
englishNums ={
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'one thousand'
    }
    
def transLetters(n):
    '''Translates integer n into a string of english words, then counts the letters in them'''
    #if it's in the dictionary, just return it
    if n in englishNums:
        return englishNums[n]
    # otherwise break it up into hundreds and tens if it's over 100. Tens component needs further processing
    elif n>=100:
        #if this is a round hundred, just return x hundred
        if n % 100 == 0:
            return englishNums[n//100] + ' hundred'
        else:
            return englishNums[n//100] + ' hundred and ' + transLetters(n % 100)
    # or if it's less than one hundred break it up by tens and ones
    else:
        return englishNums[(n//10)*10] + '-' + englishNums[n % 10]

### testing transLetters
##print(transLetters(5))
##print(transLetters(1000))
##print(transLetters(213))
##print(transLetters(543))
##

def countLetters(n):
    '''counts the letters in a number, ignoring hyphens and spaces'''
    numString = transLetters(n)
    shortString = numString.replace(' ','') #removing spaces
    shorterString = shortString.replace('-','') # removing hyphens
    return len(shorterString)

# main loop, counts total letters in all numbers from 1 to 1 thousand inclusive
letterSum = 0
for i in range(1, 1001):
    letterSum += countLetters(i)

print("Total sum of letters is %s" % letterSum)


###Test Cases
##print("There are %s letters in the phrase '342'" % countLetters(342))
###should be 23
##
##print("There are %s letters in the phrase '115'" % countLetters(115))
###should be 20
