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
    count = 13
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


    hierarchy = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13}

    numSame = 0
    numSame2 = 0
    suitSame = 1
    numList = []
    suitList = []
    royal = 0
    for i in hand:
        numList.append(hierarchy[i.getValue()])
        suitList.append(i.getSuit())
    numList.sort()
    numAsc = 0
    
    if numList == [1,10,11,12,13]:
        royal = 1
    
    flushCheck = set(suitList) # if len is 1 then its a flush so a set works well bc it removes duplicate entries and one left means all duplicates

    for i in range(1,len(numList)):
        if numList[i-1] == numList[i]-1:
            numAsc+=1
        if numList[i-1] == numList[i]:
            numSame+=1


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


    if royal == 1 and len(flushCheck) == 1:
        print("Royal Flush")
    elif numAsc == 4 and len(flushCheck) == 1:
        print("Straight Flush")
    elif numSame == 4:
        print("Four of a Kind")
    elif len(set(numList)) == 2:
        print("Full House")
    elif len(flushCheck) == 1:
        print("Flush")
    elif numAsc == 4:
        print("Straight")
    elif numSame == 3:
        print("Three of a Kind")

    ## NEED TWO PAIR
    
    elif numSame == 2:
        print("Pair")
    else:
        print("High Card")


    pass




hand = deal(d)
#extractData(hand)


swapCards(hand,d)

print('//////////')
print('FINAL HAND')
print('//////////')
#
# hand.sort()
#extractData(hand)


score(hand)