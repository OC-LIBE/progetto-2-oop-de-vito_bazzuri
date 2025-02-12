import streamlit as st
from PIL import Image
from modules.game import Game
from modules.player import Player

# SETTING UP THE GAME
if 'game' not in st.session_state:
    st.session_state['game'] = Game()

st.set_page_config(layout="wide")
game = st.session_state['game']

# MANO AVVERSARIO
col1, col2, col3, col0 = st.columns([0.1,0.1,0.1,0.7]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col1:
    st.image(game.bot.cards[0].image)
with col2:
    st.image(game.bot.cards[1].image)
with col3:
    st.image(game.bot.cards[2].image)

# CENTRO TAVOLA
col1, col2, col3, col0 = st.columns([0.1,0.1,0.1,0.7]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col1: #MAZZO
    st.image("static/images/RETRO.png", caption= game.deck.remaining)

with col2: #BRISCOLA
    if 'grafica' in st.session_state:
        st.image(game.player.cards[2].image)
        st.write(game.player.cards[2])
    
with col3: #TABLE
    st.image(game.deck.last.image)

# MANO TUA
col1, col2, col3, col0 = st.columns([0.1,0.1,0.1,0.7]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col1:
    st.image(game.player.cards[0].image)
    st.write(game.player.cards[0])
    st.button("Gioca",key=0)
with col2:
    st.image(game.player.cards[1].image)
    st.write(game.player.cards[1])
    st.button("Gioca",key=1)
with col3:
    if 'grafica' not in st.session_state:
        st.image(game.player.cards[2].image)
        st.write(game.player.cards[2])
        if st.button("Gioca",key=2):
            st.session_state['grafica'] = 1
            st.rerun
    

  
# Opening the primary image (used in background) 

  
