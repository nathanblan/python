import random
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = {
    'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
    'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}


def displayBoard(hangman_pics, missedLetters, correctLetters, secretWord):
    print(hangman_pics[len(missedLetters)])
    print(secretWord)

    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter.upper(),end = ',')
    print()

    blanks  = []
    for i in range(len(secretWord)):
        if secretWord[i]  in correctLetters:
            blanks.append(secretWord[i])
        else:
            blanks.append('_')


    for i in blanks:
        print(i, end = ' ')
    print()
    return blanks

def getGuess():
    while True:
        print('Guess a letter.')
        guess = input()
        if not guess.isalpha():
            print('Please guess a LETTER')
        elif len(guess) != 1:
            print('Please guess ONE letter only')
        elif guess in used_letter_list:
            print('You already guessed that')
        else:
            return guess.lower()

randKey = random.choice(list(words.keys()))
randIndex = random.randint(0,len(words[randKey])-1)

used_letter_list = []
missedLetters = []
correctLetters = []

print('H A N G M A N')
while True:
    blanks = displayBoard(hangman_pics,missedLetters,correctLetters,words[randKey][randIndex])

    g = getGuess()

    if g in words[randKey][randIndex]:
        correctLetters.append(g)
        if '_' not in blanks:
            print('Yes! The secret word is "' + words[randKey][randIndex] + '"! You have won!')
    else:
        missedLetters.append(g)

        if len(missedLetters) == 6:
            blanks = displayBoard(HANGMANPICS, missedLetters, correctLetters, words[randKey][randIndex])
            print('You have run out of guesses!')
            print('After '+ str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + words[randKey][randIndex] + '"')
