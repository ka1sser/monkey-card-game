import random

class Cards:
    
    whole_deck = []
    suits = ["clubs", "spades", "hearts", "diamonds"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    def __init__(self):

        for suit in self.suits:
            for value in self.values:
                card = {suit: value}
                if card not in self.whole_deck:
                    self.whole_deck.append(card)
