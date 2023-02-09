# Hangman
import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)

playAgain = True

#introduction to the game - asking for first name
print("Welcome to the Hangman Game!")
print(Fore.LIGHTMAGENTA_EX + "The theme is cities")
Username = input("Enter your FIRST name: ").upper()

while Username.isalpha() == False:
    print(Fore.RED + "Please use LETTERS only. No spaces, special characters or numbers. ")
    Username = input("Enter your FIRST name: ").upper()   
if Username.isalpha() == True:
    print("Hello, ", Username)
    print(Fore.RED + "You'll be playing against the computer")

def game():
    # List Of Words 
    WordList = list(["LONDON", "DUBAI", "TOKYO", "PARIS", "BERLIN", 
                     "MOSCOW", "RIO", "DENVER", "CARDIFF", "SHANGHAI", 
                     "DHAKA", "CAIRO", "DALLAS", "ATLANTA", "MIAMI", 
                     "CHICAGO", "BOSTON", "WASHINGTON", "HOUSTON", "SEATTLE"])

    # Declaring Variables 
    Word = random.choice(WordList)
    CurrentGuess = "_" * len(Word)
    MaxWrong = 5
    WrongGuesses = 0
    UsedLetters = []

    #Main Loop - Current Guess will fill up if it's right and it'll go in used letter. If not right, it'll go in used letter.
    while WrongGuesses < MaxWrong and CurrentGuess != Word:
        print(Fore.LIGHTCYAN_EX + "\nYou have used the following letters: ", UsedLetters)
        print("So far, the word is ", CurrentGuess)
        print("If this number reaches 5, you lose -> " + str(WrongGuesses)) #Wrong Guesses go up until 5 where you lose
        Guess = input("Enter a Letter: ").upper()

        while Guess.isalpha() == False: #Guess has be to only letters
            print(Fore.RED + "\nPlease use letters") #important infomation is in red
            Guess = input("Enter a letter:").upper()
            if Guess.isalpha() == True:
                Guess = Guess.upper()  

        while len(Guess) != 1: #Guess has to be one letter
            print(Fore.RED + "\nPlease use one letter at a time") #important infomation is in red
            Guess = input("Enter a letter:").upper()
            if Guess.isalpha() == True:
                Guess = Guess.upper()

        while Guess in UsedLetters:
            print(Fore.RED + "\nYou have already guessed that letter", Guess) #Guessed letter can't be guessed again 
            Guess = input("Enter a letter: ").upper()      
        UsedLetters.append(Guess)
        if Guess in Word:
            print(Fore.GREEN + "\nYou have guessed correctly!") #praises user which shows user has submitted right answer
        NewCurrentGuess = ""
        for letter in range(len(Word)):
            if Guess == Word[letter]:
                NewCurrentGuess += Guess
            else:
                NewCurrentGuess += CurrentGuess[letter] 

        CurrentGuess = NewCurrentGuess

        if Guess not in Word:
            print(Fore.LIGHTRED_EX + "\nSorry that was incorrect") #tells user the input was wrong 
            WrongGuesses += 1
    if WrongGuesses == MaxWrong:   #Endgame
        print("If this number reaches 5, you lose -> " + str(WrongGuesses))
        print(Fore.LIGHTRED_EX + "\nYou've been HUNG x_x") 
        print(Fore.LIGHTGREEN_EX + "The correct word is ", Word)
    else:
        print(Fore.GREEN + "The word is", Word)
        print(Fore.GREEN + "You have won. Congratulations!") #praises user

#Play Again 
def hangman():
    global playAgain
    global wrongGuesses

    while playAgain == True:
        Answer = True
        game()
        print("")
    
        while Answer == True:
            ans = input("Would you like to play again? (yes/no) ").upper() #asks user if they would like to play again
            if ans == str("YES"):
                wrongGuesses = 0
                Answer = False
                playAgain = True
                print(Fore.MAGENTA + "\nHello Again! The theme is Cities") #welcomes user again
            elif ans == str("NO"):
                Answer = False
                playAgain = False
                print("Bye. Hope to see you soon.") #farewell to user
            else:
                print(Fore.RED + "Please Enter Yes or No")

#can play in command prompt or terminal
if __name__ == "__main__":
    hangman()
