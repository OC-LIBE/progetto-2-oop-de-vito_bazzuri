import random
from modules.card import Card


class Player:
    def __init__(self, cards):
        self.cards = cards

    def play(self, index):
        self.cards.pop(index)