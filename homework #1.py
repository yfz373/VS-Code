# this imports a library into our code 
import random

secret_number = random.randint(1,101)

#none is an empty string
# we have to declare userguess because this variable wont exist UNTIL the first 'while' loop
#since you didnt declare it before the 'while' loop, it will show error, cuz the system doesnt know what that is
userGuess = None

#while is a loop. if it doesnt reach its 'condition', the 'while' loop will keep repeating itself 
#--> until it is met.
while userGuess != secret_number: 
    userGuess = int(input("Guess a number between 1 and 100: "))

    if userGuess < secret_number:
        print("oops~, the number is bigger than that!, please try again. ")

#elif is "else if"
    elif userGuess > secret_number:
        print("oops~, the number is smaller than that!, please try again")

    else: 
        print("yay~! You got it~!")
        break
