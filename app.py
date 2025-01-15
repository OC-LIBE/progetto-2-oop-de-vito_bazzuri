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
    players = deck.starting_hand()
    players = players[0]


st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Hand-Like View")
st.image([card.image for card in players.cards], width=card_width)

st.image([card.image for card in deck.cards], width=card_width)