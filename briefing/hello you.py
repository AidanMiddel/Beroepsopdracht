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

os.system('pause')
os.system('cls')
