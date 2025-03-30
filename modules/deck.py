import random
from modules.card import Card
from modules.player import Player

class Deck :
    def __init__(self, card_type):
     #qua diciamo cosa serve per questo classe
        self.cards = []
        self.create(card_type)

    def __repr__(self):#serve per vedere quante carte rimangono al mazzo
        return 'Game deck has {} cards remaining'.format(len(self.cards))

    def create(self,card_type):# creamo il mazzo formato da carte
        if card_type == 1:
            suits = ('Denari', 'Coppe', 'Spade', 'Bastoni')
        elif card_type == 2:
            suits = ('Cuori', 'Quadri', 'Fiori', 'Picche')
        decks = [Card(rank, suit, card_type) for suit in suits for rank in range(1, 11)]
        self.cards.extend(decks)

    def shuffle(self):#questa è la funzione che mischia ogni nuovo game
        self.cards = random.sample(self.cards, len(self.cards))

    def draw(self):# questa è la funzione che ti permette di pescare una carta dal mazzo
        if len(self.cards) == 0:   #in caso non ci fossero più carte nbon mi fa pescare ulteriormente
            return False
        drawn_card = self.cards[0]  #questo serve per far pescare automaticamente la prima carta del mazzo(quella più in alto)
        self.cards.remove(self.cards[0])
        print(len(self.cards))
        return drawn_card

    def reset(self): 
        self.cards = []
        self.create(self.number_of_decks)

    @property
    def remaining(self):
        return len(self.cards)
    
    @property
    def last(self):
        return self.cards[self.remaining-1]