import streamlit as st
from modules.deck import Deck
from modules.player import Player

if "game" not in st.session_state :
      st.session_state['game'] = False

if not st.session_state['game']:
    if st.button("new game"):
        st.session_state['game'] = True
        st.write("bravo fra")
    else:
         st.write("starta un game brother")
else:
     if st.button("quit_game"):
        st.write("mannaggia briscola è così bella, dove vai???")

if 'deck' not in st.session_state:
    deck = Deck()
    st.session_state['deck'] = deck

if 'players' not in st.session_state:
    cards = deck.starting_hand()
    players = [Player(cards[0]),Player(cards[1])]
    deck.backseventh()
    st.session_state['players'] = players

st.image([card.image for card in deck.cards], width=95)