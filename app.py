import streamlit as st
from modules.game import Game
from modules.player import Player

# SETTING UP THE GAME
if 'game' not in st.session_state:
    st.session_state['game'] = Game()

st.set_page_config(layout="wide")
game = st.session_state['game']

# MANO AVVERSARIO
col1, col2, col3, col4,col5, col0 = st.columns([0.1,0.1,0.1,0.1,0.1,0.5]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col1:
    st.image(game.bot.cards[0].image)
with col3:
    st.image(game.bot.cards[1].image)    
with col5:
    st.image(game.bot.cards[2].image)
    

# CENTRO TAVOLA
col1, col2, col3 = st.columns([0.2,0.2,0.6])
with col1: #MAZZO
    st.image("static/images/RETRO.png", caption= game.deck.remaining)

with col3: #BRISCOLA
    st.image(game.deck.last.image)

with col5: #TABLE
    st.write("Nulla Ancora")

# MANO TUA
col1, col2, col3, col4, col5, col0 = st.columns([0.1,0.1,0.1,0.1,0.1,0.5]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col1:
    st.image(game.player.cards[0].image)
    st.write(game.player.cards[0])
    if st.button("Gioca",key=0):
        del(game.player.cards[0])
        game.table.first_card = game.player.cards[0]
with col3:
    st.image(game.player.cards[1].image)
    st.write(game.player.cards[1])
    if st.button("Gioca",key=1):
        del(game.player.cards[1])
        game.table.first_card = game.player.cards[1]
with col5:
    st.image(game.player.cards[2].image)
    st.write(game.player.cards[2])
    if st.button("Gioca",key=3):
        del(game.player.cards[2])
        game.table.first_card = game.player.cards[2]


if st.button("Reload"):
    st.rerun