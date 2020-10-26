#gemaakt door Aidan Middel in SD1Ab

#dit is voor het gebruiken van cmd commands en om kleine wacht tijden te maken voor het beter lezen
import os, time

#introductie van het verhaal
print("Welkom bij mijn verhaal over de vlucht van Salah en zijn familie. \n \nJe bent die ochtend wakker geworden en lekker tijdens het ontbijt kijk je naar het nieuws. \nOp het nieuws zie je dat er een burgeroorlog is uitgebroken. \n \nWat ga je doen? \n ")
print("1. Vluchten dit is niet goedkoop dus je hebt veel geld nodig je komt zo'n $3000 te kort. \n2. Hier blijven")
begin = input("Kies 1 of 2: ")
#je kiest of je gaat vluchten of niet dit heeft best wel inpact op het verhaal
if begin == "1":
    print("Oké je kiest om te vluchten maar je komt geld te kort dus wat doe je? \n1. Nog voor een maandje werken. \n2. Kijken of je de smokelaar wat naar benden kan praten")
    vluchten_1= input("Kies 1 of 2: ")
    if vluchten_1 == "1":
        print("Oké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
        #ga naar 1 voor mij
    elif vluchten_1 == "2":
        print("lel")
    else:
        print("nee")
elif begin == "2":
    print("voor nu nog niks")
else:
    print("bruh")