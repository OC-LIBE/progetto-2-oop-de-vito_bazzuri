import streamlit as st
from modules.deck import Deck
from modules.player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        card = self.starting_hand()
        self.you = Player(card[0])
        self.opponent = Player(card[1])
        self.backseventh()

    def starting_hand(self):
        your = []
        oppon = []
        for i in range(3):
            your.append(self.deck.draw())
            oppon.append(self.deck.draw())
        return [your,oppon]

    def backseventh(self):
        back = self.deck.draw()
        self.deck.cards.append(back)