import random
from modules.card import Card


class Player:
    def __init__(self, cards):
        self.cards = []
        self.cards.extend(cards)