import streamlit as st

class Table:
    def __init__ (self, briscola, first_card,second_card, first, second):   #qua diciamo cosa serve per questo classe
        self.briscola = briscola
        self.second_card =second_card
        self.first_card = first_card
        self.first = first 
        self.second = second
   
    def win_hand(self):  #funziona in cui abbiamo le regole per far capire alla macchina chi vince la mano
        if self.first_card.suit == self.second_card.suit:
            # questo è per le carte dello stesso seme (anche le carte del seme di "briscola")
            if self.first_card.point >= self.second_card.point:
                self.first.score.extend([self.second_card, self.first_card])
                return 1
            else:
                self.second.score.extend([self.second_card, self.first_card])
                return 2
        elif self.first_card.suit != self.second_card.suit and self.first_card.suit !=  self.briscola.suit and self.second_card.suit !=  self.briscola.suit:
            # questo è quando nel tavolo  abbiamo due carte di diverso seme (senza "briscola")
                self.first.score.extend([self.second_card, self.first_card])
                return 1
        else:
            # questo è quando nel tavolo abbiamo due carte di diverso seme  (con "briscola")
            if self.second_card.suit == self.briscola.suit:
                self.second.score.extend([self.second_card, self.first_card])
                return 2
            else:
                self.first.score.extend([self.second_card, self.first_card]) 
                return 1  
    
    def clean_table(self): 
        self.second_card = None
        self.first_card = None
        self.first = None 
        self.second = None
        return "OK"
        
  