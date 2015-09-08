# Palindrome product
# two three digit numbers
# Biggest possible product is 998001
# Run exhaustively through three-digit factors? 1m calculations
from math import sqrt, floor
maxPalindrome = 0
for a in range(100,999):
    for b in range(100,999):
        product = str(a*b) # make it a string
        # check if product is palindrome
        for index in range(floor(len(product)/2)):
            if product[index] != product[len(product)-index-1]:
                # not a palindrome
                break
        # is a palindrome, check value
        else:
            print(product + " is a palindrome number")
            productInt = int(product)
            maxPalindrome = max(maxPalindrome, productInt)
        
print(maxPalindrome)      
