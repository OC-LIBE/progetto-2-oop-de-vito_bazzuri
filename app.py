import streamlit as st
from modules.game import Game
from modules.player import Player

# SETTING UP THE GAME
if 'game' not in st.session_state:
    st.session_state['game'] = Game()

game = st.session_state['game']

# MANO AVVERSARIO
st.image([card.image for card in game.opponent.cards], width=95)

# MANO TUA
st.image([card.image for card in game.you.cards], width=95)

if st.button("Reload"):
    st.rerun