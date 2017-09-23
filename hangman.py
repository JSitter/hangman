import os
import random

#Load words from document
def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
def checkGuess(currentGuess, previousGuesses):
    #check if guess is a letter
    if not currentGuess.isalpha():
        print("Hey! Only letters are valid in this game.")
        return False

    if(currentGuess in previousGuesses):
        print("You already guessed that letter brah.")
        return False

    if len(currentGuess) > 1:
        print("So which letter is it? Only one guess at a time allowed. \n\nTRY AGAIN!")
        return False

    if(len(currentGuess) == 1):
        return True

    print("I literally can't even right now. Try again.")
    return False
    

#Output game data to player
#All inputs must be strings
def displayGameState(board, guessedLetters, remainingGuesses):
    print("Makeschool Deathmatch Hangman!\n\n\nYou have " + str(remainingGuesses) + " remaining.\t\tCurrent Guesses: " + str(guessedLetters) + "\n\n" + board, end='\r')

#convert game data to output string
def drawBoard(secretWord, guessedLetters):
    board = ""
    for c in secretWord:
        if c in guessedLetters:
            board = board + c
        else:
            board = board + " _ "
    return board

def winScreen():
    os.system("clear")
    print("Has anyone told you how smart you are?")
    print("***You WON!****")
    print("Now is a good time to enter your wizarding skillz into hangman tournament deathmatch.")


#Main Game functionality
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed
    '''
    #get terminal width and height
    rows, columns = os.popen('stty size', 'r').read().split()
    os.system("clear")
    #flag to indicate whether player is in game
    ingame = True

    #current board represented as String
    board = ""

    #letters guessed by player
    guesses = ""

    #number of guesses used by player
    guessNum = 0

    #number of guesses allowed in game
    total_guesses = 9

    #Flag New game
    newGame = True

    #Flag to check for game over
    gameOver = False

    #Flag for game win
    gameWin = False

    while(ingame):
        if newGame:
            #Initialize New Game
            secretWord = loadWord()
            newGame = False
        if not gameOver:
            displayGameState(drawBoard(secretWord, guesses), guesses, str(total_guesses-guessNum))
            newGuess = input("\n\n\nGuess a letter: ")
            #Verify user input to continue
            if(checkGuess(newGuess, guesses)):
                guesses = guesses + newGuess
                guessNum = guessNum + 1

                #trigger end of game
                if(guessNum <= total_guesses):
                    if(isWordGuessed(secretWord, guesses)):
                        #set game win
                        gameOver == True
                        gameWin == True
                else:
                    gameOver = True
                    
        else:
            #Game Over
            #Check for Win
            if(gameWin):
                #Display you win game screen
                winScreen()
            else:
                print("You're DEAD!")
            replay = input("Would you like to play again? y or n: ") 
            if(replay == 'y'):
                #reset board
                board = ""
                guesses = ''
                guessNum = 0
                newGame = True
                gameOver = False
                gameWin = False


hangman(loadWord())
