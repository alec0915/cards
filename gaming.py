import card
import io

d = card.initializeDeck()
d = card.shuffleDecks(d)
currentRound = 0

def deal(deck):
    return [deck.pop(),deck.pop(),deck.pop(),deck.pop(),deck.pop()]

def extractData(hand):
    for i in hand:
        print(i)

def swapCards(hand,deck):
    count = 3
    while count > 0:
        for i in range(len(hand)):
            print(str(i+1)+'.',hand[i])
        try: 
            print(count,"swaps left")
            userInput = input("Pick cards to swap out in one line separated by spaces (type d when you're done swapping)")
            nums = userInput.split(' ')
            nums.sort()
            for i in range(len(nums)):
                hand.pop(int(nums[i])-i-1)
                hand.append(deck.pop())
            count -=1
        except ValueError:
            print('please enter a valid number')


hand = deal(d)
#extractData(hand)


swapCards(hand,d)

extractData(hand)
