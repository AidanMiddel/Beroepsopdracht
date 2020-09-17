from datetime import datetime
datum = datetime.now()
import locale
import os
os.system('title Hello You')
locale.setlocale(locale.LC_TIME, 'nl_NL')
print("Hello You!, ik ben Aidan")
print("De datum en tijd is: ", datum.strftime('%A %d %B %Y'))
print("Wie ben jij?")
naamvanandere = input()
if naamvanandere == "Aidan":
    print("hé jij ook hier")
    print("Hoe grote kamer heb je?")
    print("Hoe lang is jou kamer in meters?")
    lengtekamer = int(input())
    print("Hoe breed is jou kamer in meters?")
    breedtekamer = int(input())
    grotekamer = breedtekamer * lengtekamer;
    print("je kamer is: " , grotekamer , "m² groot")
else:
    print("Hello " + naamvanandere)
    print(" ")

print("Ik ben zelf een nieuwkomer op het mediacollege,")
print("hier een klein quizje over mij zelf:")
print(" ")
print("Waar kom ik vandaan?")
print(" ")
print(" A. Alkmaar")
print(" B. Haarlem-noord")
print(" C. Amsterdam-zuid")
vraag1 = input("A, B of C: ")
if vraag1 == "A":
    print(" ")
    print("Nee helaas, volgende keer beter")
elif vraag1 == "B":
    print(" ")
    print("Goedzo, daar kom ik inderdaad vandaan")
elif vraag1 == "C":
    print(" ")
    print("Nee helaas, volgende keer beter")
else:
    print(" ")
    print("Let op je hoofdletters!")

print(" ")
print("Van welke middelbare school kom ik?")
print(" ")
print(" A. Ichthuslyceum")
print(" B. Mendel")
print(" C. Schoter")
vraag2 = input("A, B of C: ")
if vraag2 == "A":
    print(" ")
    print("Nee, maar heb wel het ichthus gedaan maar niet gehaalt")
elif vraag2 == "B":
    print(" ")
    print("Nee helaas, volgende keer beter")
elif vraag2 == "C":
    print(" ")
    print("ja, ik kom inderdaad van het schoter")
else:
    print(" ")
    print("Let op je hoofdletters!")

print(" ")
print("Welk seizoen ben ik jarig?")
print(" ")
print(" A. Lente")
print(" B. Zomer")
print(" C. Herfst")
print(" D. Winter")
vraag3 = input("A, B, C of D: ")
if vraag3 == "A":
    print(" ")
    print("Nee helaas, volgende keer beter")
elif vraag3 == "B":
    print(" ")
    print("Nee helaas, volgende keer beter")
elif vraag3 == "C":
    print(" ")
    print("Nee helaas, volgende keer beter")
elif vraag3 == "D":
    print(" ")
    print("Ja, ik ben inderdaad jarig in de winter. goed gegokt")
else:
    print(" ")
    print("Let op je hoofdletters!")

print(" ")
print("Dit was de quiz voor nu bedankt voor het spelen!")
os.system('pause')
os.system('cls')
