import string

password = "helloWorld"

### going through each letter in the password and check in each position if they
# have an the related character case. 
# If they one in ANY position then add 1 otherwise 0 for.

upper_case = any ([1 if c in string.ascii_uppercase else 0 for c in password ])

lower_case = any ([1 if c in string.ascii_lowercase else 0 for c in password ])

special_case = any ([1 if c in string.punctuation else 0 for c in password ])

digits = any ([1 if c in string.digits else 0 for c in password ])

