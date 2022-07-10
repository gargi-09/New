# Password generator Explaination:
        # Each time the program is run, a new password will be generated randomly.
            # The passwords generated will be 8 characters long and will have to include the following characters in any order:
                #  uppercase letters from A to Z,
                # lowercase letters from a to z,
                # digits from 0 to 9,
                # punctuation signs such as !, ?, “, # etc.

#Program:

#Importing random library
import random

#Function to generate random passwords
def shuffle_it(password):
    temp=list(password)
    random.shuffle(temp)
    pssword= ''.join(temp)
    return pssword

#Generating random uppercase letters
uppercase1=chr(random.randint(65,90))
uppercase2=chr(random.randint(65,90))

#Generating random punctuation symbols
exclamation1=chr(random.randint(33,152))
exclamation2=chr(random.randint(33,152))

#Generating random lowecase letters
lowercase1=chr(random.randint(97,122))
lowercase2=chr(random.randint(97,122))

#Generating random numbers letters
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))

#Combining all the letters and symbols
password =uppercase1+uppercase2+lowercase1+lowercase2+num1+num2+exclamation1+exclamation2
print(password)
#Passing the above variable in the function
print(f"Password is: {shuffle_it(password)}")