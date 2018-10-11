import itertools
import random
class Card():
    def __init__(self):
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.values = range(1,14)
        self.real_card = [] # empty list to append
        for card in itertools.product(self.suits,self.values):
            self.real_card.append(card)

    def GetRandomCard(self):
        random_num = random.randint(0,51)
        card_to_be_return = self.real_card[random_num]
        return card_to_be_return

    def shuffle(self):
        random.shuffle(self.real_card)


    def deal_card(self):
        card = self.real_card.pop(0)
        return card