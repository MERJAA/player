#  HigherOrLower

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS= 8
def getCard(decklistIn):
    thisCaed= decklistIn.pop()
    return thisCaed
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut
#main
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()
startingDeckList = []
for suit in SUIT_TUPLE:
    for value,rank in enumerate(RANK_TUPLE):
        cardDict= {'rank': rank , 'suit':suit , 'value': value+1}
        startingDeckList.append(cardDict)
score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()
    for cardNumber in range(0, NCARDS):  # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' +
                       currentCardRank + ' of ' +
                       currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')

"""import random

def GameCard(arr):
    counter = 0
    for i in range(len(arr)):
        ran= random.choice(arr)
        print("This is the current item : ",ran)
        player = input(" Enter your predict : ")
        predict= random.choice(arr)
        if player == "higher" :
            if predict>ran:
                print("correct")
                counter+=20
            else:
                print("incorrect")
                counter-=15
        elif player == "lower":
            if predict<ran:
                 print("correct")
                 counter+=20
            else:
                 print("incorrect")
                 counter-=15
        else:
             print("you put a wrong predict")
             counter -= 15
    print(" The score is : ", counter)
arr = []
for i in range(8):
    firstit = random.randint(0,100)
    lastit = random.randint(999,1000)
    item=random.randint(firstit,lastit)
    arr.append(item)

GameCard(arr)"""