import streamlit as st
from modules.game import Game
from modules.player import Player

'''if "game" not in st.session_state :
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
    st.session_state['players'] = players'''

if 'game' not in st.session_state:
    st.session_state['game'] = Game()

st.image([card.image for card in st.session_state['game'].deck.cards], width=95)
st.image([card.image for card in st.session_state['game'].you.cards], width=95)
st.image([card.image for card in st.session_state['game'].opponent.cards], width=95)

if st.button("Reload"):
    st.rerun