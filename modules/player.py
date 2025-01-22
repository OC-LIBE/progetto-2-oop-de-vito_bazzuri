import random
from modules.card import Card


class Player:
    def __init__(self, cards, name):
        self.cards = cards
        self.name = name
        
    def play(self, index):
        self.cards.pop(index)