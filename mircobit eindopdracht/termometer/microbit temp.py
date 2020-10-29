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

twee = Image("00000:"
             "00000:"
             "00000:"
             "99000:"
             "99999")

vier = Image("00000:"
             "00000:"
             "00000:"
             "99900:"
             "99999")

zes = Image("00000:"
             "00000:"
             "00000:"
             "99990:"
             "99999")

acht = Image("00000:"
             "00000:"
             "00000:"
             "99999:"
             "99999")

tien = Image("00000:"
             "00000:"
             "90000:"
             "99999:"
             "99999")

twaalf = Image("00000:"
             "00000:"
             "99000:"
             "99999:"
             "99999")

veertien = Image("00000:"
             "00000:"
             "99900:"
             "99999:"
             "99999")

zestien = Image("00000:"
             "00000:"
             "99990:"
             "99999:"
             "99999")

achttien = Image("00000:"
             "00000:"
             "99999:"
             "99999:"
             "99999")

twintig = Image("00000:"
             "90000:"
             "99999:"
             "99999:"
             "99999")

tweeentwintig = Image("00000:"
             "99000:"
             "99999:"
             "99999:"
             "99999")

vierentwintig = Image("00000:"
             "99900:"
             "99999:"
             "99999:"
             "99999")

zesentwintig = Image("00000:"
             "99990:"
             "99999:"
             "99999:"
             "99999")

achtentwintig = Image("00000:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

dertig = Image("90000:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

tweeendertig = Image("99000:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

vierendertig = Image("99900:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

zesendertig = Image("99990:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

achtendertig = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

#tot hier alle plaatjes voor de temparatuur

while script == True:
    temp = temperature()
    mingetal = 6
    temp2 = temp - mingetal
#tot hier de afwijking van mijn (Aidan Middel) microbit bijstellen
    if button_a.was_pressed():
        display.scroll(temp2)
        #als je de a knop in drukt zie je de acuraate temparatuur
    elif temp2 in range(-100, -8):
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
    elif temp2 in range(2, 4):
        display.show(twee)
    elif temp2 in range(4, 6):
        display.show(vier)
    elif temp2 in range(6, 8):
        display.show(zes)
    elif temp2 in range(8, 10):
        display.show(acht)
    elif temp2 in range(10, 12):
        display.show(tien)
    elif temp2 in range(12, 14):
        display.show(twaalf)
    elif temp2 in range(14, 16):
        display.show(veertien)
    elif temp2 in range(16, 18):
        display.show(zestien)
    elif temp2 in range(18, 20):
        display.show(zestien)
    elif temp2 in range(20, 22):
        display.show(twintig)
    elif temp2 in range(22, 24):
        display.show(tweeentwintig)
    elif temp2 in range(24, 26):
        display.show(vierentwintig)
    elif temp2 in range(26, 28):
        display.show(zesentwintig)
    elif temp2 in range(28, 30):
        display.show(achtentwintig)
    elif temp2 in range(30, 32):
        display.show(dertig)
    elif temp2 in range(32, 34):
        display.show(tweeendertig)
    elif temp2 in range(34, 36):
        display.show(vierendertig)
    elif temp2 in range(36, 38):
        display.show(zesendertig)
    elif temp2 in range(38, 100):
        display.show(achtendertig)
    sleep(200)

#tot hier de plaatjes laten zien en knop voor temparatuur in getallen
