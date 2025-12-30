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
            nums = userInput.rstrip().split(' ')
            nums.sort()


            if len(nums) == 1 and nums[0] == '':
                break


            for i in range(len(nums)):
                hand.pop(int(nums[i])-i-1)
                hand.append(deck.pop())
            count -=1
        except ValueError:
            print('please enter a valid number')
    for i in hand:
        print(i)


def score(hand):
    #royal flush            10
    #straight flush         9
    #four of a kind         8
    #full house             7
    #flush                  6
    #straight               5
    #three of a kind        4
    #two pair               3
    #pair                   2
    #high card              1

    hierarchy = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13}

    numSame = 0
    suitSame = 0
    numList = []
    suitList = []
    for i in hand:
        numList.append(i.getValue())
        suitList.append(i.getSuit())

    for i in numList:
        print(hierarchy[i])

    pass




hand = deal(d)
#extractData(hand)


swapCards(hand,d)

print('//////////')
print('FINAL HAND')
print('//////////')
hand.sort()
extractData(hand)


score(hand)