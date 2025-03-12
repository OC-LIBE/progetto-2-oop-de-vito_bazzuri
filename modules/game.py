import streamlit as st
from modules.deck import Deck
from modules.player import Player
from modules.table import Table
from modules.bot import Bot

class Game:
    def __init__(self): #qua diciamo cosa serve per questo classe
        self.deck:Deck = Deck()
        self.deck.shuffle()
        cards = self.starting_hand()
        self.player:Player = Player(cards=cards[0],bot=False)
        self.bot:Player = Player(cards=cards[1],bot=False)
        self.ai_bot:Bot = Bot()
        self.backseventh()
        self.table:Table = Table(briscola=self.deck.last,first_card=None,second_card=None,first=None,second=None)
        self.winner = None
        self.ordine = ["PlayerTime","BotTime"]
        
    def starting_hand(self): # qui facciamo in modo che tutti i giocatori, una volta cominciata una partita, abbiano le carte per iniziare
        player_hand = []
        bot_hand = []
        for i in range(3):  # 3 perche ci servono 3 carte in mano
            player_hand.append(self.deck.draw())
            bot_hand.append(self.deck.draw())
        return [player_hand,bot_hand]

    def backseventh(self):  # serve per mettere la settima carta infondo al mazzo, che sarebbe poi la briscola
        back = self.deck.draw() 
        self.deck.cards.append(back)

    def new_turn(self): # con questo facciamo in modo che il vincitore nel prossimo turno giochi o rigiochi
        if self.winner == 2: # Rigira l'ordine dei giocatori
            temp = self.ordine[0]
            self.ordine[0] = self.ordine[1]
            self.ordine[1] = temp
        else: #NON Rigira l'ordine
            pass