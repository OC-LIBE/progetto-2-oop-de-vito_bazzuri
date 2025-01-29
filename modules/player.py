import random
from modules.card import Card


class Player:
    def __init__(self,card):
        self.cards = []
        self.cards.extend(card)


    def add_card(self,card):
        self.cards.extend(card)