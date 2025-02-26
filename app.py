import streamlit as st
import time
from modules.game import Game

# SETTING UP THE GAME
if 'game' not in st.session_state:
    st.session_state['turno'] = "PlayerTime" 
    st.session_state['game'] = Game()  


st.set_page_config(layout="wide")
game :Game= st.session_state['game']

# Grafiche
def colonna_bot(nr_col=0):
    if game.bot.cards[nr_col] != None:
        st.image(game.bot.cards[nr_col].image)
    else:
        st.image("static/images/VUOTO.png")

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
        if st.session_state['turno'] == "PlayerTime": # Se tocca al Player giocare (per primo)
            if st.button("Gioca",key=nr_col):
                if game.table.first_card == None:
                    game.table.first = game.player
                    game.table.second = game.bot
                    game.table.first_card = game.player.play_card(nr_col)
                    st.session_state['turno'] = "BotTime"
                else:
                    game.table.second_card = game.player.play_card(nr_col)
                    game.table.first = game.bot
                    game.table.second = game.player
                    st.session_state['turno'] = "MatchTime"

# GRAFICHE RACCHIUSE
col1, col2, col3, col4, col5, col6, col0 = st.columns([0.1,0.1,0.1,0.1,0.1,0.2,0.3]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
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

# COMANDI    
if st.session_state['turno'] == "BotTime": # Se tocca al Bot giocare
    if st.button("Next", key="next-2"): 
        if game.table.first_card == None:
            game.table.first_card = game.bot.play_card(game.ai_bot.choose(game.bot.cards,game.table.briscola,game.table.first_card))
            st.session_state['turno'] = "PlayerTime"
        else:
            game.table.second_card = game.bot.play_card(game.ai_bot.choose(game.bot.cards,game.table.briscola,game.table.first_card))
            st.session_state['turno'] = "MatchTime"

        
        

if st.session_state['turno'] == "MatchTime": # Se hanno entrambi giocato
    if st.button("Next", key="next-3"):
        game.winner = game.table.win_hand()
        st.session_state['turno'] = "DrawTime"
        

if st.session_state['turno'] == "DrawTime": # Se si devono ridare le carte
    if st.button("Next", key="next-4"):
        game.table.clean_table()
        game.player.add_card(card=game.deck.draw())
        game.bot.add_card(card=game.deck.draw())
        print(f"Carte giocatore  {game.player.cards}")
        #testare il vincitore della mano e settare il turno #TODO
        game.new_turn()
        st.session_state['turno'] = game.ordine[0]
        

if st.button("ripristina la partita"):
    game.player.score = []
    game.bot.score = []

if st.button("Reload"):
    st.rerun()

st.write(st.session_state['turno'])
st.write(game.player.score)
st.write(game.bot.score)
