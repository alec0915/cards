import card
import io



def deal(deck):
    return [deck.pop(),deck.pop(),deck.pop(),deck.pop(),deck.pop()]

def extractData(hand):
    for i in hand:
        print(i)








def swapCards(hand,deck):
    count = 3
    while count > 0:
        print()
        score(hand)
        for i in range(len(hand)):
            print(str(i+1)+'.',hand[i])
        try: 
            print()
            if count == 1:
                print(count,'swap left')
            else:
                print(count,"swaps left")
            userInput = input("Type the numbers next to cards to swap out in one line separated by spaces then hit enter to swap. \nHit enter with nothing typed to finish. ")
            nums = userInput.lstrip().rstrip().split(' ')
            nums.sort()


            if len(nums) == 1 and nums[0] == '':
                break


            for i in range(len(nums)):
                hand.pop(int(nums[i])-i-1)
                hand.append(deck.pop())
            count -=1
        except ValueError:
            print('\nPlease enter a valid number\n')
        except IndexError:
            print("\nPlease type only numbers 1-5 with only spaces between each number\n")
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

    valueDict = {}
    for i in numList:
        if i in valueDict:
            valueDict[i] = valueDict[i]+1
        else:
            valueDict[i] = 1

    #print('valdict:', valueDict)
    twopaircheck = []
    tripscheck = 0
    fourcheck = 0
    for i in valueDict:
        #print('valuedict',i,valueDict[i])
        if valueDict[i] == 2:
            twopaircheck.append(i)
        if valueDict[i] == 3:
            tripscheck = 1
        if valueDict[i] == 4:
            fourcheck = 1



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
        return "Royal Flush"
    elif numAsc == 4 and len(flushCheck) == 1:
        print("Straight Flush")
        return "Straight Flush"
    elif fourcheck == 1:
        print("Four of a Kind")
        return "Four of a Kind"
    #elif len(set(numList)) == 2:
    elif tripscheck == 1 and len(twopaircheck) == 1:
        print("Full House")
        return "Full House"
    elif len(flushCheck) == 1:
        print("Flush")
        return "Flush"
    elif numAsc == 4 or royal == 1:
        print("Straight")
        return "Straight"
    elif tripscheck == 1:
        print("Three of a Kind")
        return "Three of a Kind"
    elif len(twopaircheck) == 2:
        print("Two Pair")    
        return "Two Pair"
    elif len(twopaircheck) == 1:
        print("Pair")
        return "Pair"
    else:
        print("High Card")
        return "High Card"


    pass



d = card.initializeDeck()
d = card.shuffleDecks(d)
currentRound = 0
print("\n")

hand = deal(d)
#extractData(hand)


swapCards(hand,d)

print('\n//////////')
print('FINAL HAND')
print('//////////\n')
#
# hand.sort()
#extractData(hand)
score(hand)
extractData(hand)
print()
