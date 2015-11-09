''' Project Euler problem 59: XOR decryption
Each character on a computer is assigned a unique code
and the preferred standard is ASCII
(American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file,
convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that
using the same encryption key on the cipher text, restores the plain text;
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated
cyclically throughout the message. The balance for this method
is using a sufficiently long password key for security, but short
enough to be memorable.

Your task has been made easy, as the encryption key consists of
three lower case characters. Using cipher.txt (right click and
'Save Link/Target As...'), a file containing the encrypted ASCII
codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII
values in the original text.


'''

# Need a dictionary of common English words so we can score the produced cleartext
# based on how much it resembles English.

# Alternate approaches- letter frequency? Like in the python crypto book?

# Timing code
import time
start_time = time.time()

# Import cyphertext as a list of digits. The format in the .txt file is integers separated by commas. 

inFile = open('p059_cipher.txt','r')


cyphertext = [int(x) for x in inFile.read().split(',')]
print("cyphertext is %s characters" % len(cyphertext))
print(cyphertext[:20])
print(chr(cyphertext[3]))

# The chr() function turns integers into Unicode characters (of which ASCII is a subset)

inFile.close()

# Brute-force approach
# Decryption loop just needs to loop through all possible keys
# Three lower-case characters (in ASCII, lower case alphabet characters are 97 to 122 inclusive)
# This approach tries 26^3 = 17576 keys



for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            key = [a, b, c]
            # Cycle over cyphertext to create new cleartext
            cleartext = [cyphertext[i] ^ key[i % 3] for i in range(len(cyphertext))]
            # Test cleartext for English words
            lettertext = ''.join([chr(x) for x in cleartext])

print(cleartext[:20])

print(lettertext)
    
print("---Completed in %s seconds---" %(time.time() - start_time))


'''Time performance
1201 chars in cyphertext
completes in 7.9 seconds with .append() in for loop
completes in 4.93 seconds with list comprehension

after adding in list-to-string code with list comprehensions, takes 7.9 seconds 
'''
