import random
from modules.card import Card
from modules.player import Player
import streamlit as st

if "game" not in st.session_state :
      giocando = False

if not giocando:
    if st.button("new game"):
        st.write("bravo fra")
    else:
         st.write("starta un game brother")

else:
     if st.button("quit_game"):
        st.write("mannaggia briscola è così bella, dove vai???")
     
                

        
            
        
    
        
    
    