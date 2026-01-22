import string

password = "n1231ACASD@#!!#gofskmnkladalkadfsdoja"

### going through each letter in the password and check in each position if they
# have an the related character case. 
# If they one in ANY position then add 1 otherwise 0 for.

upper_case = any ([1 if c in string.ascii_uppercase else 0 for c in password ])

lower_case = any ([1 if c in string.ascii_lowercase else 0 for c in password ])

special = any ([1 if c in string.punctuation else 0 for c in password ]) #print(string.punctuation)clea

digits = any ([1 if c in string.digits else 0 for c in password ])

characaters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0 

# Criteria check commonality for score  

with open('common.txt', 'r') as f:
  common = f.read().splitlines()

if password in common:
  print("❌ This password is found in a common list. Score: 0 / 7")
  exit()

# Criteria check length for score  

print(f'#### password length ###')

if length > 8: # 8 is minimum more than 8 is plus 1 to score and so on
  score +=1

if length > 12:
  score +=1

if length > 17:
  score +=1

if length > 20:
  score +=1

print(f"Password length is {str(length)}, adding {str(score)} points! ")

  # Criteria check diversification of characters for score  
  # take characters sum to get amount of different types

print(f'#### Character variety ###')

if sum(characaters) > 1: # at least two types of characters list
    score +=1
if sum(characaters) > 2: 
    score +=1
if sum(characaters) > 3: 
    score +=1
  
print(f"Password has {str(sum(characaters))} different character types adding {str(sum(characaters) - 1)}") # if we have 2 character types we only get 1 point (existence != diversity

print(f'#### Total Score ###')

if score < 4:
   print(f"The password is weak! Score: {str(score)} / 7")

elif score == 4: 
   print(f"The password is okay! Score: {str(score)} / 7")

elif 4 < score <= 6:
   print(f"The password is decent! Score: {str(score)} / 7")

elif score > 6:
   print(f"The password is strong! Score: {str(score)} / 7")

   
