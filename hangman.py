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
    #print(set(secretWord))
    #check if the intersection of sets is equal in length to the length of the set of secret word
    if len(set(secretWord).intersection(set(lettersGuessed))) == len(set(secretWord)):
        return True
    else:
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
        return "Hey! Only letters are valid in this game."

    if currentGuess in previousGuesses:
        return "You already guessed that letter brah."

    if len(currentGuess) > 1:
        return "So which letter is it? Only one guess at a time allowed. \n\nTRY AGAIN!"
    
    #correct user input return no errors
    if len(currentGuess) == 1:
        return ""

    #Catch all for unforseen circumstances
    return "I literally can't even right now. Try again."

#Output game data to player
#All inputs must be strings
def displayGameState(board, guessedLetters, remainingGuesses, feedback = ""):
    os.system("clear")
    print("Makeschool Deathmatch Hangman!\n\n")
    print("You have " + str(remainingGuesses) + " remaining.\t\tCurrent Guesses: " + str(guessedLetters))
    print("\n\n" + board)
    print(feedback)

#convert game data to output string
def drawBoard(secretWord, guessedLetters):
    board = ""
    for c in secretWord:
        if c in guessedLetters:
            board = board + c
        else:
            board = board + " _ "
    return board

def winScreen( word ):
    os.system("clear")
    print("Has anyone told you how smart you are?")
    print("***You WON!****")
    print("The secret word was: ", word)
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
    #get terminal width and height for no reason at the moment :(
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
    user_feedback = ""
    while(ingame):
        if newGame:
            #Initialize New Game
            secretWord = loadWord()
            newGame = False
        if not gameOver:
            displayGameState(drawBoard(secretWord, guesses), guesses, str(total_guesses-guessNum), user_feedback)
            user_feedback = ""
            newGuess = input("\n\nGuess a letter: ")
            #Verify user input to continue
            user_feedback = checkGuess(newGuess, guesses)

            #If there are no errors continue
            if not user_feedback:
                guesses = guesses + newGuess
                
                gameWin = isWordGuessed(secretWord, guesses)
                #check if guess is incorrect
                if newGuess not in secretWord:
                    guessNum = guessNum + 1

                if gameWin:
                    gameOver = True
                    winScreen( secretWord )
                    
                #trigger end of game loss
                if guessNum == total_guesses:
                    gameOver = True

        else:
            #Game Over
            #Check for Win
            if(gameWin):
                #Display you win game screen
                winScreen(secretWord)
            else:
                print("You're DEAD!")
            replay = input("Would you like to play again? y or n: ") 
            if(replay == 'y'):
                #reset board
                board = ""
                guesses = ""
                guessNum = 0
                newGame = True
                gameOver = False
                gameWin = False
            else:
                ingame = False

hangman(loadWord())