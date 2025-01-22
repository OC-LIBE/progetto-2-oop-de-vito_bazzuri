import random
from modules.card import Card
from modules.player import Player
suits = ('Denari', 'Coppe', 'Spade', 'Bastoni')


class Deck :
    def __init__(self):
        self.cards = []
        self.create()

    def __repr__(self):
        return 'Game deck has {} cards remaining'.format(len(self.cards))

    def create(self):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 11)]
        self.cards.extend(decks)

    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))

    def starting_hand(self):
        your_cards = []
        other_cards = []
        for i in range(3):
            your_cards.append(self.draw)
            f"{your_cards}"
            other_cards.append(self.draw)
            f"{your_cards[0]}"
        players = [Player(your_cards),Player(other_cards)]
        return players

    def draw(self):
        if len(self.cards) == 0:
            return False
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        print(len(self.cards))
        return drawn_card

    def reset(self):
        self.cards = []
        self.create(self.number_of_decks)

    @property
    def remaining(self):
        return len(self.cards)