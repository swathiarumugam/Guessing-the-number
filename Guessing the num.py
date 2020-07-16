##Guessing game
print("Welcome to the number one Guessing Game!")
uname  = input("Hello, What is your username?")

print("Hello", uname + ".", )

from random import randint
guessed= False
number= randint(0,100)

guesses= 0
while not guessed:
    ans=int (input("Try to guess the number I am thinking of!:"))
    #use tab to indent
    guesses +=1
    if int(ans)== number:
        print("Congrats! You guessed it correctly.")
        print("It took you {} guesses!".format(guesses))
        break
    elif int(ans) >number:
        print("The number is lower than what you guessed")
    elif int(ans)< number:
        print("The number is greater than what you guessed")