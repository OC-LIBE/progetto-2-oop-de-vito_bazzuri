import streamlit as st
from modules.deck import Deck
from modules.player import Player
from modules.table import Table

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        cards = self.starting_hand()
        self.player = Player(cards=cards[0],bot=False)
        self.bot = Player(cards=cards[1],bot=True)
        self.backseventh()

    def starting_hand(self):
        player_hand = []
        bot_hand = []
        for i in range(3):
            player_hand.append(self.deck.draw())
            bot_hand.append(self.deck.draw())
        return [player_hand,bot_hand]

    def backseventh(self):
        back = self.deck.draw()
        self.deck.cards.append(back)