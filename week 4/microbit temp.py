from microbit import *
import math

#tot hier import dingen

script = True

#tot hier het script aanzetten

mintien = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "90000")

minacht = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "99000")

minzes = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "99900")

minvier = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "99990")

mintwee = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "99999")
nul = Image("00000:"
             "00000:"
             "00000:"
             "90000:"
             "99999")

#tot hier alle plaatjes voor de temparatuur

temp = temperature()
mingetal = 6
temp2 = temp - mingetal

#tot hier de afwijking van mijn (Aidan Middel) microbit bijstellen

while script == True:
    if button_a.was_pressed():
        display.scroll(temp2) #als je de a knop in drukt zie je de acuraate temparatuur
    elif temp2 in range(-10, -8):
        display.show(mintien)
    elif temp2 in range(-8, -6):
        display.show(minacht)
    elif temp2 in range(-6, -4):
        display.show(minzes)
    elif temp2 in range(-4, -2):
        display.show(minvier)
    elif temp2 in range(-2, 0):
        display.show(mintwee)
    elif temp2 in range(0, 2):
        display.show(nul)
    sleep(200)

#tot hier de plaatjes laten zien en knop voor temparatuur in getallen
