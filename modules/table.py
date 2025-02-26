import streamlit as st

class Table:
    def __init__ (self, briscola, first_card,second_card, first, second):
        self.briscola = briscola
        self.second_card =second_card
        self.first_card = first_card
        self.first = first 
        self.second = second
        self.winner = None
   
    def win_hand(self):
        if self.first_card.suit == self.second_card.suit:
            # this is for the same suit (also "briscola")
            if self.first_card.point >= self.second_card.point:
                self.first.score.extend([self.second_card, self.first_card])
                self.winner = 1
            else:
                self.second.score.extend([self.second_card, self.first_card])
                self.winner = 2
        elif self.first_card.suit != self.second_card.suit and self.first_card.suit !=  self.briscola.suit and self.second_card.suit !=  self.briscola.suit:
            # this is when in table there are two cards with differents suits (without "briscola")
                self.first.score.extend([self.second_card, self.first_card])
                self.winner = 1
        else:
            # this is when in table there are two cards with differents suits (with "briscola")
            if self.second_card.suit == self.briscola.suit:
                self.second.score.extend([self.second_card, self.first_card])
                self.winner = 2
            else:
                self.first.score.extend([self.second_card, self.first_card]) 
                self.winner = 1    
    
    def clean_table(self):
        self.second_card =None
        self.first_card = None
        self.first = None 
        self.second = None
        return "OK"
        
  