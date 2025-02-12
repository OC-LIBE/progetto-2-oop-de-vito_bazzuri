import numpy, random, os
"""Input Layer: le tre carte, la briscola, la carta giù sul tavolo (+ Le carte già giocate a difficoltà massima)"""
inputs_lenght = 5
bias = 1 #value of bias
weights = []
for i in range(inputs_lenght):
    weights.append(random.random())

def Perceptron(inputs, output) :
   outputP = inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+
   if outputP > 0: #activation function (here Heaviside)
      outputP = 1
   else:
      outputP = 0
   error = output - outputP
   weights[0] += error * inputs[0]
   weights[1] += error * inputs[1]
   weights[2] += error * inputs[2]

for i in range(50) : # Più lo fa, più impara
    Perceptron(1,1,1) #True or true
    Perceptron(1,0,1) #True or false
    Perceptron(0,1,1) #False or true
    Perceptron(0,0,0) #False or false

x = 0
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
print(weights[2])