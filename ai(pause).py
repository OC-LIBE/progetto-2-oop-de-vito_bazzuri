import random
import math
from modules.card import Card

#Input Layer: le tre carte, la briscola, la carta giù sul tavolo (+ Le carte già giocate a difficoltà massima)
inputs_lenght = 5
init = True
weights = []
for i in range(inputs_lenght+1): # Uno per input + il Bias.
    weights.append(random.random())

def activation_function(value):
   value = 1/(1+math.exp(-value))
   if value : #activation function (here Heaviside)
      out = 0
   elif value > 0.33 and value < 0.66:
      out = 1
   elif value > 0.66:
      out = 2
   return out

def learn(inputs, output) :
   outputP = 0
   for i in range(inputs_lenght):
      outputP += inputs[i].code*weights[i]
   outputP += weights[-1]

   outputP = activation_function(outputP)
   
   error = output - outputP
   print(error)
   print(weights)
   for i in range(inputs_lenght):
      weights[i] += error*inputs[i].code

def play(inputs) :
   outputP = 0
   for i in range(inputs_lenght):
      outputP += inputs[i].code*weights[i]
   outputP += weights[-1]

   outputP = activation_function(outputP)

   return outputP

#Input Layer: le tre carte, la briscola, la carta giù sul tavolo (+ Le carte già giocate a difficoltà massima)
for i in range(3) : # Più lo fa, più impara
   learn([Card(10,"Coppe"),Card(3,"Coppe"),Card(6,"Denari"),Card(10,"Bastoni"),Card(3,"Bastoni")],2) #Img 1

print(play([Card(10,"Coppe"),Card(3,"Coppe"),Card(6,"Denari"),Card(10,"Bastoni"),Card(3,"Bastoni")])) # Test
"""x = 0
y = 0
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0 : #activation function
   outputP = 1
else :
   outputP = 0
print(x, "or", y, "is : ", outputP)

outputP = 1/(1+numpy.exp(-outputP)) #sigmoid function
print(weights[0])
print(weights[1])
print(weights[2])"""

"""with col6:
        if game.bot.score == []:
            st.image("static/images/VUOTO.png",width=89) # Width per motivi estetici      
        else:
            st.image(game.bot.score[0].image, caption = "Bot")
    
    st.image("static/images/VUOTO.png",width=89) # Width per motivi estetici  
   if game.player.score == []:
        st.image("static/images/VUOTO.png",width=89) # Width per motivi estetici      
    else:
        st.image(game.player.score[0].image, caption = "Player") """
