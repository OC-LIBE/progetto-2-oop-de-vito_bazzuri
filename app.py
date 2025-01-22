import streamlit as st
from modules.deck import Deck
from modules.player import Player

st.set_page_config(
   layout="wide",
)
card_width=95

if 'deck' not in st.session_state:
    deck = Deck()
    st.session_state['deck'] = deck

if 'players' not in st.session_state:
    cards = deck.starting_hand()
    players = [Player(cards[0]),Player(cards[1])]
    deck.backseventh()
    st.session_state['players'] = players


deck = st.session_state['deck']
players = st.session_state['players']

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Hand deck")
st.image([card.image for card in players[0].cards], width=card_width)
st.image([card.image for card in players[1].cards], width=card_width)