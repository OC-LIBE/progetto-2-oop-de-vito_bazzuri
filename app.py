import streamlit as st
import time
from modules.game import Game

# SETTING UP THE GAME
card_width = 90
if 'game' not in st.session_state:
    col1, col2, col3= st.columns([0.3,0.3,0.3])
    with col3:
        options = ["Inizio io" , "Inizia avversario"]
        selection = st.pills("Ordine di gioco", options, default= "Inizio io" ,selection_mode="single")
        if selection == "Inizio io":
            ordine = ["PlayerTime","BotTime"]
        else:
            ordine = ["BotTime","PlayerTime"]
    with col1:
        st.image("static/images2/1B.png",width=card_width)
        if st.button("Francesi"):
            card_type = 2
            st.session_state['turno'] = ordine[0]
            st.session_state['game'] = Game(card_type,ordine)
            st.rerun()
    with col2:
        st.image("static/images/1D.jpg",width=card_width)
        if st.button("Napoletane"):
            card_type = 1
            st.session_state['turno'] = ordine[0]
            st.session_state['game'] = Game(card_type,ordine)
            st.rerun()


if 'game' in st.session_state:
    st.set_page_config(layout="wide")
    game :Game= st.session_state['game']

    # Grafiche
    def colonna_bot(nr_col=0):
        if game.bot.cards[nr_col] != None:
            st.image("static/images/RETRO.png",width=card_width)
        else:
            st.image("static/images/VUOTO.png",width=card_width)

    def colonna_centro(nr_col=0):
        if nr_col == 0:
            if len(game.deck.cards) > 0:
                st.image("static/images/RETRO.png", caption= game.deck.remaining ,width=card_width)
            else:
                st.image("static/images/VUOTO.png",width=card_width)
        elif nr_col == 1:
            st.image("static/images/VUOTO.png",width=card_width) 
        elif nr_col == 2:
            if len(game.deck.cards) > 0:
                st.image(game.deck.last.image, caption = "Briscola",width=card_width)
            else:
                st.image("static/images/VUOTO.png",width=card_width)

    def colonna_player(nr_col=0):
        if game.player.cards[nr_col] != None:
            st.image(game.player.cards[nr_col].image,width=card_width)
            st.write(game.player.cards[nr_col])
            if st.session_state['turno'] == "PlayerTime": # Se tocca al Player giocare (per primo)
                if st.button("Gioca",key=nr_col):
                    if game.table.first_card == None:
                        game.table.first = game.player
                        game.table.second = game.bot
                        game.table.first_card = game.player.play_card(nr_col)
                        st.session_state['turno'] = "BotTime"
                        st.rerun()
                    else:
                        game.table.second_card = game.player.play_card(nr_col)
                        game.table.first = game.bot
                        game.table.second = game.player
                        st.session_state['turno'] = "MatchTime"
                        st.rerun()

    # GRAFICHE RACCHIUSE
    col1, col2, col3, col4, col5, col0 = st.columns([0.1,0.1,0.1,0.1,0.1,0.5]) # Col0 è vuota per lasciare spazio vuoto -> Grafica
    with col2:
        if game.table.first_card != None:
            st.image("static/images/VUOTO.png",width=card_width)
            st.image(game.table.first_card.image,width=card_width)
    with col4:
        if game.table.second_card != None:
            st.image("static/images/VUOTO.png",width=card_width)
            st.image(game.table.second_card.image,width=card_width)
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
        if game.table.first_card == None:
            game.table.first_card = game.bot.play_card(game.ai_bot.choose(game.bot.cards,game.table.briscola,game.table.first_card))
            st.session_state['turno'] = "PlayerTime"
            st.rerun()
        else:
            game.table.second_card = game.bot.play_card(game.ai_bot.choose(game.bot.cards,game.table.briscola,game.table.first_card))
            st.session_state['turno'] = "MatchTime"
            st.rerun()

    if st.session_state['turno'] == "MatchTime": # Se hanno entrambi giocato
        game.winner = game.table.win_hand()
        st.session_state['turno'] = "DrawTime"
        st.rerun()
            
    if st.session_state['turno'] == "DrawTime": # Se si devono ridare le carte
        if st.button("Avanti", key="next-4"):
            game.ai_bot.eval = [0,0,0] # FOR DEBUG HERE TODO
            game.table.clean_table()
            if len(game.deck.cards) > 0:
                game.player.add_card(card=game.deck.draw())
                game.bot.add_card(card=game.deck.draw())
                print(f"Carte giocatore  {game.player.cards}")
            game.new_turn()
            st.session_state['turno'] = game.ordine[0]
            st.rerun()    

    # FINE PARTITA
    if game.player.cards == [None,None,None] and (st.session_state['turno'] == "PlayerTime" or st.session_state['turno'] == "BotTime" ):
        if game.player.points_sum() > game.bot.points_sum():
            st.success("Vittoria!")
            st.balloons()
        elif game.player.points_sum() == game.bot.points_sum():
            st.warning("Pareggio.")
            st.snow()
        else:
            st.error("Sconfitta...")
        st.write("Punti:")
        st.write(game.player.points_sum())
        st.write("Punti avversari:")
        st.write(game.bot.points_sum())
        if st.button("Nuova partita"): # Rinizia la partita
            if len(game.player.score) > 0: # Se il player ha preso almeno una carta
                card_type = game.player.score[0].type # La grafica delle carte è uguale a quella del player
            else:
                card_type = game.bot.score[0].type # Sennò del Bot
            st.session_state['game'].__init__(card_type) # Rinizializa la partita
            st.session_state['turno'] = "PlayerTime" 
            st.rerun()