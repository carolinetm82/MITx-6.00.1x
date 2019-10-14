# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
     # We initialize a new word, complete it with common letters between secretWord and lettersGuessed    
    word_g=''
    for i in secretWord:
       if i in lettersGuessed:
          word_g+=i
 
     # and compared it with secretWord
    if word_g==secretWord:
          return True
    else:
          return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   # We initialize a new word, complete it with common letters between secretWord and lettersGuessed  
    guess=[]
    WordToFind=''
    secret=list(secretWord)
 
    for char in secretWord:
       guess+=['_ ']

    for i in range(len(secret)):
      if secret[i] in lettersGuessed:
           guess[i]=secret[i]
      else:
           guess[i]='_ '
      
      WordToFind+=guess[i]

    if WordToFind[-1]=='_ ':
       WordToFind=WordToFind[:-1]+'_'

    return WordToFind


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    strin=''
    for i in alphabet:
        if i not in lettersGuessed:
            strin+=i
    return strin
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord),'letters long.')
    print('-----------')

    num_round=8
    num_guess=num_round
    lettersGuessed = []
    mistakesMade = []

    while num_guess <= num_round :
                                
        print('You have',num_guess,'guesses left')
        print('Available letters :', getAvailableLetters(lettersGuessed))
        letter=input('Please guess a letter: ').lower()
        
        if (letter in secretWord)and(letter not in lettersGuessed) :            
            lettersGuessed+=letter
            print('Good guess :',getGuessedWord(secretWord, lettersGuessed))
            print('---------------------')
            
        elif (letter in lettersGuessed)or (letter in mistakesMade):
            print('Oops! You \'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            print('---------------------')            

        else :            
            mistakesMade +=letter
            lettersGuessed +=letter
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
            num_guess-=1
            print('---------------------')



        if isWordGuessed(secretWord, lettersGuessed)==True:
             print('Congratulations, you won!')
             break
        else:
             if num_guess==0:
               print('Sorry, you ran out of guesses. The word was', secretWord,'.')
               break
            



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
