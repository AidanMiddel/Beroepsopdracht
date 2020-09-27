from datetime import datetime
datum = datetime.now()
import locale
import os
os.system('title Dit ben ik')
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
print("Is kaas lekker?")
print(" ")
print(" A. Jaa, zeker")
print(" B. Nee, ga al over mijn nek bij het idee...")
print(" C. Wat is dit nou weer voor vraag?")
print(" D. het is wel oké")
vraag4 = input("A, B, C of D: ")
if vraag4 == "A":
    print(" ")
    print("Helemaal met je eens!")
    print(" ")
    print("Wat vindt jij van mensen die het niet lusten?")
    print(" ")
    print(" A. ieder zijn ding")
    print(" B. raar")
    vraag4A = input("A of B : ")
    if vraag4A == "A":
        print(" ")
        print("Ja waarom ook niet...")
    elif vraag4A == "B":
        print(" ")
        print("Vind ik ook!")
    else:
        print(" ")
        print("Let op je hoofdletters!")
elif vraag4 == "B":
    print(" ")
    print("De wat, je bent nederlands toch?")
    print(" ")
    print(" A. Ja.....")
    print(" B. Nee....")
    vraag4B = input("A of B : ")
    if vraag4B == "A":
        print(" ")
        print("Waarom lust je het dan niet?")
        print(" ")
        print(" A. Gewoon vies")
        print(" B. Ja weet nie")
        vraag4BA = input("A of B : ")
        if vraag4BA == "A":
            print(" ")
            print("Nou raar maar jij bent jij...")
        elif vraag4BA == "B":
            print(" ")
            print("Uhm nou sure...")
        else:
            print(" ")
            print("Let op je hoofdletters!")
    elif vraag4B == "B":
        print(" ")
        print("Begrijpelijk, fijne dag nog")
    else:
        print(" ")
        print("Let op je hoofdletters!")
elif vraag4 == "C":
    print(" ")
    print("Ja, ik weet niet moet meerdere eindes maken")
    print("laat me ja... :(")
elif vraag4 == "D":
    print(" ")
    print("Gelukkig, anders zou ik teleurgesteld zijn...")
    print("fijne dag nog")
else:
    print(" ")
    print("Let op je hoofdletters!")

print(" ")
print("Dit was de quiz voor nu bedankt voor het spelen!")
os.system('pause')
os.system('cls')
