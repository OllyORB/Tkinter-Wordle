import random
from tkinter import *
# Functions
def getRandomWord():
    with open('words.txt') as file:
        words = file.read().splitlines()
        

    word = words[random.randint(0, (len(words)-1))]
    return word.upper()

def wordIsValid(word):
    word = word.lower()
    with open('words.txt') as file:
        words = file.read().splitlines()
        if word in words:
            return True
        else:
            return False

# Get Input Data
def attemptGuess():
    global gameOver
    if gameOver:
        resetGame()
        return None
    guess = guessEntry.get()
    guess = guess.upper()
    guessEntry.delete(0, 'end')
    if len(guess) != 5:
        displayError('Guess must be 5 letters')
    elif not guess.isalpha():
        displayError('Guess must only be letters')
    else:
        clearError()
        if wordIsValid(guess):
            updateGuess(guess)
            return None
        else:
            displayError('Word not in dictionary')

# Manage Errors
def displayError(error):
    errorMessageLabel.config(text=error)

def clearError():
    errorMessageLabel.config(text='')

#Update Guess Frames
def updateGuess(word):
    l1 = word[0]
    l2 = word[1]
    l3 = word[2]
    l4 = word[3]
    l5 = word[4]
    global currentGuess
    global gameOver
    boxes = findBoxColours(word)
    b1 = boxes[0]
    b2 = boxes[1]
    b3 = boxes[2]
    b4 = boxes[3]
    b5 = boxes[4]
    if currentGuess == 1:
        g1b1L.config(text = l1, bg=b1)
        g1b2L.config(text = l2, bg=b2)
        g1b3L.config(text = l3, bg=b3)
        g1b4L.config(text = l4, bg=b4)
        g1b5L.config(text = l5, bg=b5)
        g1b1.config(bg=b1)
        g1b2.config(bg=b2)
        g1b3.config(bg=b3)
        g1b4.config(bg=b4)
        g1b5.config(bg=b5)
    elif currentGuess == 2:
        g2b1L.config(text = l1, bg=b1)
        g2b2L.config(text = l2, bg=b2)
        g2b3L.config(text = l3, bg=b3)
        g2b4L.config(text = l4, bg=b4)
        g2b5L.config(text = l5, bg=b5)
        g2b1.config(bg=b1)
        g2b2.config(bg=b2)
        g2b3.config(bg=b3)
        g2b4.config(bg=b4)
        g2b5.config(bg=b5)
    elif currentGuess == 3:
        g3b1L.config(text = l1, bg=b1)
        g3b2L.config(text = l2, bg=b2)
        g3b3L.config(text = l3, bg=b3)
        g3b4L.config(text = l4, bg=b4)
        g3b5L.config(text = l5, bg=b5)
        g3b1.config(bg=b1)
        g3b2.config(bg=b2)
        g3b3.config(bg=b3)
        g3b4.config(bg=b4)
        g3b5.config(bg=b5)
    elif currentGuess == 4:
        g4b1L.config(text = l1, bg=b1)
        g4b2L.config(text = l2, bg=b2)
        g4b3L.config(text = l3, bg=b3)
        g4b4L.config(text = l4, bg=b4)
        g4b5L.config(text = l5, bg=b5)
        g4b1.config(bg=b1)
        g4b2.config(bg=b2)
        g4b3.config(bg=b3)
        g4b4.config(bg=b4)
        g4b5.config(bg=b5)
    elif currentGuess == 5:
        g5b1L.config(text = l1, bg=b1)
        g5b2L.config(text = l2, bg=b2)
        g5b3L.config(text = l3, bg=b3)
        g5b4L.config(text = l4, bg=b4)
        g5b5L.config(text = l5, bg=b5)
        g5b1.config(bg=b1)
        g5b2.config(bg=b2)
        g5b3.config(bg=b3)
        g5b4.config(bg=b4)
        g5b5.config(bg=b5)
    elif currentGuess == 6:
        g6b1L.config(text = l1, bg=b1)
        g6b2L.config(text = l2, bg=b2)
        g6b3L.config(text = l3, bg=b3)
        g6b4L.config(text = l4, bg=b4)
        g6b5L.config(text = l5, bg=b5)
        g6b1.config(bg=b1)
        g6b2.config(bg=b2)
        g6b3.config(bg=b3)
        g6b4.config(bg=b4)
        g6b5.config(bg=b5)
        if {b1, b2, b3, b4, b5} == {'green'}:
            displayError(f'You win, the word was {targetWord}, press the submit guess button to restart')
            gameOver = True
        else:
            displayError(f'You lost, the word was {targetWord}, press the submit guess button to restart')
            gameOver = True
    if {b1, b2, b3, b4, b5} == {'green'}:
        displayError(f'You win, the word was {targetWord}, press the submit guess button to restart')
        gameOver = True
    elif currentGuess < 6:
        currentGuess +=1
        return None

def findBoxColours(word):
    global targetWord
    global guessProgress
    guessProgress = targetWord
    guessProgress = list(guessProgress)
    for i in range(len(word)):
        if word[i] == targetWord[i]:
            guessProgress[i] = '*'
    if word[0] == targetWord[0]:
        b1 = 'green'
    elif word[0] in targetWord and word[0] in guessProgress:
        b1 = 'yellow'
    else: 
        b1 = 'gray'
    if word[1] == targetWord[1]:
        b2 = 'green'
    elif word[1] in targetWord and word[1] in guessProgress:
        b2 = 'yellow'
    else: 
        b2 = 'gray'
    if word[2] == targetWord[2]:
        b3 = 'green'
    elif word[2] in targetWord and word[2] in guessProgress:
        b3 = 'yellow'
    else: 
        b3 = 'gray'
    if word[3] == targetWord[3]:
        b4 = 'green'
    elif word[3] in targetWord and word[3] in guessProgress:
        b4 = 'yellow'
    else: 
        b4 = 'gray'
    if word[4] == targetWord[4]:
        b5 = 'green'
    elif word[4] in targetWord and word[4] in guessProgress:
        b5 = 'yellow'
    else: 
        b5 = 'gray'
    return [b1, b2, b3, b4, b5]
        



# Reset Game
def resetGame(firstTime = False):
    if firstTime == False:
        g1b1.config(bg='white')
        g1b2.config(bg='white')
        g1b3.config(bg='white')
        g1b4.config(bg='white')
        g1b5.config(bg='white')
        g2b1.config(bg='white')
        g2b2.config(bg='white')
        g2b3.config(bg='white')
        g2b4.config(bg='white')
        g2b5.config(bg='white')
        g3b1.config(bg='white')
        g3b2.config(bg='white')
        g3b3.config(bg='white')
        g3b4.config(bg='white')
        g3b5.config(bg='white')
        g4b1.config(bg='white')
        g4b2.config(bg='white')
        g4b3.config(bg='white')
        g4b4.config(bg='white')
        g4b5.config(bg='white')
        g5b1.config(bg='white')
        g5b2.config(bg='white')
        g5b3.config(bg='white')
        g5b4.config(bg='white')
        g5b5.config(bg='white')
        g6b1.config(bg='white')
        g6b2.config(bg='white')
        g6b3.config(bg='white')
        g6b4.config(bg='white')
        g6b5.config(bg='white')
        g1b1L.config(text='', bg='white')
        g1b2L.config(text='', bg='white')
        g1b3L.config(text='', bg='white')
        g1b4L.config(text='', bg='white')
        g1b5L.config(text='', bg='white')
        g2b1L.config(text='', bg='white')
        g2b2L.config(text='', bg='white')
        g2b3L.config(text='', bg='white')
        g2b4L.config(text='', bg='white')
        g2b5L.config(text='', bg='white')
        g3b1L.config(text='', bg='white')
        g3b2L.config(text='', bg='white')
        g3b3L.config(text='', bg='white')
        g3b4L.config(text='', bg='white')
        g3b5L.config(text='', bg='white')
        g4b1L.config(text='', bg='white')
        g4b2L.config(text='', bg='white')
        g4b3L.config(text='', bg='white')
        g4b4L.config(text='', bg='white')
        g4b5L.config(text='', bg='white')
        g5b1L.config(text='', bg='white')
        g5b2L.config(text='', bg='white')
        g5b3L.config(text='', bg='white')
        g5b4L.config(text='', bg='white')
        g5b5L.config(text='', bg='white')
        g6b1L.config(text='', bg='white')
        g6b2L.config(text='', bg='white')
        g6b3L.config(text='', bg='white')
        g6b4L.config(text='', bg='white')
        g6b5L.config(text='', bg='white')
        errorMessageLabel.config(text='')
    global targetWord
    global currentGuess
    global gameOver
    targetWord = getRandomWord()
    currentGuess = 1
    gameOver = False

# Tkinter UI

# Root
root = Tk()
root.title('Wordle!')
root.geometry('600x900')#
root.configure(background = 'black')
root.resizable(False, False)

# Set up UI
# Set up guess frames and title label
wordleTitleFrame = Frame(root, bg='white', width=600, height=100)
guess1Frame = Frame(root, bg='white', width=600, height=100)
guess2Frame = Frame(root, bg='white', width=600, height=100)
guess3Frame = Frame(root, bg='white', width=600, height=100)
guess4Frame = Frame(root, bg='white', width=600, height=100)
guess5Frame = Frame(root, bg='white', width=600, height=100)
guess6Frame = Frame(root, bg='white', width=600, height=100)
guessEntryFrame = Frame(root, bg='white', width=600, height=50)
errorMessageFrame = Frame(root, bg='black', width=600, height=50)
wordleTitle = Label(wordleTitleFrame, text = 'Wordle!', font=('Arial Black', 40), bg= 'black', fg = 'white')
g1b1 = Frame(guess1Frame, bg = 'white', width = 120, height = 100)
g1b2 = Frame(guess1Frame, bg = 'white', width = 120, height = 100)
g1b3 = Frame(guess1Frame, bg = 'white', width = 120, height = 100)
g1b4 = Frame(guess1Frame, bg = 'white', width = 120, height = 100)
g1b5 = Frame(guess1Frame, bg = 'white', width = 120, height = 100)
g2b1 = Frame(guess2Frame, bg = 'white', width = 120, height = 100)
g2b2 = Frame(guess2Frame, bg = 'white', width = 120, height = 100)
g2b3 = Frame(guess2Frame, bg = 'white', width = 120, height = 100)
g2b4 = Frame(guess2Frame, bg = 'white', width = 120, height = 100)
g2b5 = Frame(guess2Frame, bg = 'white', width = 120, height = 100)
g3b1 = Frame(guess3Frame, bg = 'white', width = 120, height = 100)
g3b2 = Frame(guess3Frame, bg = 'white', width = 120, height = 100)
g3b3 = Frame(guess3Frame, bg = 'white', width = 120, height = 100)
g3b4 = Frame(guess3Frame, bg = 'white', width = 120, height = 100)
g3b5 = Frame(guess3Frame, bg = 'white', width = 120, height = 100)
g4b1 = Frame(guess4Frame, bg = 'white', width = 120, height = 100)
g4b2 = Frame(guess4Frame, bg = 'white', width = 120, height = 100)
g4b3 = Frame(guess4Frame, bg = 'white', width = 120, height = 100)
g4b4 = Frame(guess4Frame, bg = 'white', width = 120, height = 100)
g4b5 = Frame(guess4Frame, bg = 'white', width = 120, height = 100)
g5b1 = Frame(guess5Frame, bg = 'white', width = 120, height = 100)
g5b2 = Frame(guess5Frame, bg = 'white', width = 120, height = 100)
g5b3 = Frame(guess5Frame, bg = 'white', width = 120, height = 100)
g5b4 = Frame(guess5Frame, bg = 'white', width = 120, height = 100)
g5b5 = Frame(guess5Frame, bg = 'white', width = 120, height = 100)
g6b1 = Frame(guess6Frame, bg = 'white', width = 120, height = 100)
g6b2 = Frame(guess6Frame, bg = 'white', width = 120, height = 100)
g6b3 = Frame(guess6Frame, bg = 'white', width = 120, height = 100)
g6b4 = Frame(guess6Frame, bg = 'white', width = 120, height = 100)
g6b5 = Frame(guess6Frame, bg = 'white', width = 120, height = 100)
# Create labels
g1b1L = Label(g1b1, text='', font=('Arial Black', 40), bg='white')
g1b2L = Label(g1b2, text='', font=('Arial Black', 40), bg='white')
g1b3L = Label(g1b3, text='', font=('Arial Black', 40), bg='white')
g1b4L = Label(g1b4, text='', font=('Arial Black', 40), bg='white')
g1b5L = Label(g1b5, text='', font=('Arial Black', 40), bg='white')
g2b1L = Label(g2b1, text='', font=('Arial Black', 40), bg='white')
g2b2L = Label(g2b2, text='', font=('Arial Black', 40), bg='white')
g2b3L = Label(g2b3, text='', font=('Arial Black', 40), bg='white')
g2b4L = Label(g2b4, text='', font=('Arial Black', 40), bg='white')
g2b5L = Label(g2b5, text='', font=('Arial Black', 40), bg='white')
g3b1L = Label(g3b1, text='', font=('Arial Black', 40), bg='white')
g3b2L = Label(g3b2, text='', font=('Arial Black', 40), bg='white')
g3b3L = Label(g3b3, text='', font=('Arial Black', 40), bg='white')
g3b4L = Label(g3b4, text='', font=('Arial Black', 40), bg='white')
g3b5L = Label(g3b5, text='', font=('Arial Black', 40), bg='white')
g4b1L = Label(g4b1, text='', font=('Arial Black', 40), bg='white')
g4b2L = Label(g4b2, text='', font=('Arial Black', 40), bg='white')
g4b3L = Label(g4b3, text='', font=('Arial Black', 40), bg='white')
g4b4L = Label(g4b4, text='', font=('Arial Black', 40), bg='white')
g4b5L = Label(g4b5, text='', font=('Arial Black', 40), bg='white')
g5b1L = Label(g5b1, text='', font=('Arial Black', 40), bg='white')
g5b2L = Label(g5b2, text='', font=('Arial Black', 40), bg='white')
g5b3L = Label(g5b3, text='', font=('Arial Black', 40), bg='white')
g5b4L = Label(g5b4, text='', font=('Arial Black', 40), bg='white')
g5b5L = Label(g5b5, text='', font=('Arial Black', 40), bg='white')
g6b1L = Label(g6b1, text='', font=('Arial Black', 40), bg='white')
g6b2L = Label(g6b2, text='', font=('Arial Black', 40), bg='white')
g6b3L = Label(g6b3, text='', font=('Arial Black', 40), bg='white')
g6b4L = Label(g6b4, text='', font=('Arial Black', 40), bg='white')
g6b5L = Label(g6b5, text='', font=('Arial Black', 40), bg='white')
# Create entry box and button
guessEntry = Entry(guessEntryFrame, bg='gray', font=('Arial Black', 20), cursor='tcross', justify=CENTER)
guessButton = Button(guessEntryFrame, bg='white', font=('Arial Black', 14), activebackground='gray',text='Submit Guess', command=attemptGuess)
# Create error message label
errorMessageLabel = Label(errorMessageFrame, bg='black', font=('Arial Black', 10), fg='red', text='', justify=CENTER)
# Disable propagate for all letter frames
g1b1.grid_propagate(False)
g1b2.grid_propagate(False)
g1b3.grid_propagate(False)
g1b4.grid_propagate(False)
g1b5.grid_propagate(False)
g2b1.grid_propagate(False)
g2b2.grid_propagate(False)
g2b3.grid_propagate(False)
g2b4.grid_propagate(False)
g2b5.grid_propagate(False)
g3b1.grid_propagate(False)
g3b2.grid_propagate(False)
g3b3.grid_propagate(False)
g3b4.grid_propagate(False)
g3b5.grid_propagate(False)
g4b1.grid_propagate(False)
g4b2.grid_propagate(False)
g4b3.grid_propagate(False)
g4b4.grid_propagate(False)
g4b5.grid_propagate(False)
g5b1.grid_propagate(False)
g5b2.grid_propagate(False)
g5b3.grid_propagate(False)
g5b4.grid_propagate(False)
g5b5.grid_propagate(False)
g6b1.grid_propagate(False)
g6b2.grid_propagate(False)
g6b3.grid_propagate(False)
g6b4.grid_propagate(False)
g6b5.grid_propagate(False)
guessEntryFrame.grid_propagate(False)
errorMessageFrame.grid_propagate(False)
# Grid for title and guess rows
wordleTitleFrame.grid(column=0, row=0, pady=5)
wordleTitle.grid(column=0, row=0)
guess1Frame.grid(column=0, row=1, pady=5)
guess2Frame.grid(column=0, row=2, pady=5)
guess3Frame.grid(column=0, row=3, pady=5)
guess4Frame.grid(column=0, row=4, pady=5)
guess5Frame.grid(column=0, row=5, pady=5)
guess6Frame.grid(column=0, row=6, pady=5)
guessEntryFrame.grid(column=0, row=7)
errorMessageFrame.grid(column=0, row=8)
# Grid for letter frames
g1b1.grid(column=0, row=1)
g1b2.grid(column=1, row=1)
g1b3.grid(column=2, row=1)
g1b4.grid(column=3, row=1)
g1b5.grid(column=4, row=1)
g2b1.grid(column=0, row=1)
g2b2.grid(column=1, row=1)
g2b3.grid(column=2, row=1)
g2b4.grid(column=3, row=1)
g2b5.grid(column=4, row=1)
g3b1.grid(column=0, row=1)
g3b2.grid(column=1, row=1)
g3b3.grid(column=2, row=1)
g3b4.grid(column=3, row=1)
g3b5.grid(column=4, row=1)
g4b1.grid(column=0, row=1)
g4b2.grid(column=1, row=1)
g4b3.grid(column=2, row=1)
g4b4.grid(column=3, row=1)
g4b5.grid(column=4, row=1)
g5b1.grid(column=0, row=1)
g5b2.grid(column=1, row=1)
g5b3.grid(column=2, row=1)
g5b4.grid(column=3, row=1)
g5b5.grid(column=4, row=1)
g6b1.grid(column=0, row=1)
g6b2.grid(column=1, row=1)
g6b3.grid(column=2, row=1)
g6b4.grid(column=3, row=1)
g6b5.grid(column=4, row=1)
# Grid for letter labels
g1b1L.grid(padx=33, pady=10)
g1b2L.grid(padx=33, pady=10)
g1b3L.grid(padx=33, pady=10)
g1b4L.grid(padx=33, pady=10)
g1b5L.grid(padx=33, pady=10)
g2b1L.grid(padx=33, pady=10)
g2b2L.grid(padx=33, pady=10)
g2b3L.grid(padx=33, pady=10)
g2b4L.grid(padx=33, pady=10)
g2b5L.grid(padx=33, pady=10)
g3b1L.grid(padx=33, pady=10)
g3b2L.grid(padx=33, pady=10)
g3b3L.grid(padx=33, pady=10)
g3b4L.grid(padx=33, pady=10)
g3b5L.grid(padx=33, pady=10)
g4b1L.grid(padx=33, pady=10)
g4b2L.grid(padx=33, pady=10)
g4b3L.grid(padx=33, pady=10)
g4b4L.grid(padx=33, pady=10)
g4b5L.grid(padx=33, pady=10)
g5b1L.grid(padx=33, pady=10)
g5b2L.grid(padx=33, pady=10)
g5b3L.grid(padx=33, pady=10)
g5b4L.grid(padx=33, pady=10)
g5b5L.grid(padx=33, pady=10)
g6b1L.grid(padx=33, pady=10)
g6b2L.grid(padx=33, pady=10)
g6b3L.grid(padx=33, pady=10)
g6b4L.grid(padx=33, pady=10)
g6b5L.grid(padx=33, pady=10)
# Grid for entry button and box
guessEntry.grid(column=0, row=1, ipady=5)
guessButton.grid(column=1, row=1, padx=30)
# Grid for error message
errorMessageLabel.grid()
# Mainloop
resetGame(True)
root.mainloop()
