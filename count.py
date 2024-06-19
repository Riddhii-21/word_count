# Python3 code to demonstrate 
# to count words in string 
# using sum() + strip() + split()
import string

# initializing string 
test_string = "Hello @ World !! "

# printing original string
print ("The original string is : " + test_string)

# using sum() + strip() + split()
# to count words in string
res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])

# printing result
print ("The number of words in string are : " + str(res))
