import random

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def getSuit(self):
        return self.suit
    
    def getValue(self):
        return self.value
    
    def setSuit(self,newSuit):
        self.suit = newSuit

    def setValue(self,newValue):
        self.suit = newValue

    def __lt__(self,other):
        return self.value < other.value

    def __eq__(self,other):
        return (self.value == other.value) and (self.suit == other.suit)
    
    
    def __str__(self):
        return str(str(self.value) + ' of ' + str(self.suit))


    def __repr___(self):
        return str(self)

   

def initializeDeck():
    Deck = []

    valueList = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    #valueList = ['Ace','10','Jack','Queen','King']
    suitList = ['Clubs','Hearts','Diamonds','Spades']
    #suitList = ['Clubs']


    for i in valueList:
        for j in suitList:
            Deck.append(Card(i,j))
    return Deck

def shuffleDecks(*args):
    bigDeck = []
    for i in args:
        for j in i:
            bigDeck.append(j)
    random.shuffle(bigDeck)
    return bigDeck

def printDeck(Deck):
    for i in Deck:
        print(i)


def main():
    Deck = initializeDeck()
    Deck = shuffleDecks(Deck)
    printDeck(Deck)

if __name__ == '__main__':
    main()