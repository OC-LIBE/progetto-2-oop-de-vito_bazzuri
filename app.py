import streamlit as st
from modules.game import Game
from modules.player import Player

# SETTING UP THE GAME
if 'game' not in st.session_state:
    st.session_state['turno'] = -1
    st.session_state['game'] = Game()

st.set_page_config(layout="wide")
game = st.session_state['game']

def colonna_bot(nr_col=0):
    if game.bot.cards[nr_col] != None:
        st.image(game.bot.cards[nr_col].image)
        game.first = game.bot
    else:
        st.image("static/images/VUOTO.png")
        game.second = game.bot


def colonna_centro(nr_col=0):
    if nr_col == 0:
        st.image("static/images/RETRO.png", caption= game.deck.remaining)
    elif nr_col == 1:
        st.image("static/images/VUOTO.png",width=89) # Width per motivi estetici
    elif nr_col == 2:
        st.image(game.deck.last.image, caption = "Briscola")

def colonna_player(nr_col=0):
    if game.player.cards[nr_col] != None:
        st.image(game.player.cards[nr_col].image)
        st.write(game.player.cards[nr_col])
        if st.session_state['turno'] == -1:
            if st.button("Gioca",key=nr_col):
                st.session_state['turno'] = 0
                if game.table.first_card == None:
                    game.first = game.player
                    game.table.first_card = game.player.cards[nr_col]
                else:
                    game.table.second_card = game.player.cards[nr_col]
                    game.second = game.player
                game.player.cards[nr_col] = None

# MANO TUA
col1, col2, col3, col4, col5, col0 = st.columns([0.1,0.1,0.1,0.1,0.1,0.5]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
with col2:
    if game.table.first_card != None:
        st.image("static/images/VUOTO.png")
        st.image(game.table.first_card.image)
with col4:
    if game.table.second_card != None:
        st.image("static/images/VUOTO.png")
        st.image(game.table.second_card.image)
with col1:
    colonna_bot(0)
    colonna_centro(0)
    colonna_player(0)
with col3:
    colonna_bot(1)
    colonna_centro(1)
    colonna_player(1)
with col5:
    colonna_bot(2)
    colonna_centro(2)
    colonna_player(2)

if st.session_state['turno'] == 0: # Se tocca al Bot giocare
    st.session_state['turno'] = 1 
    if game.table.first_card == None:
        game.table.first_card = game.bot.cards[0]
    else:
        game.table.second_card = game.bot.cards[0]
    game.bot.cards[0] = None

if st.button("Reload"):
    st.rerun