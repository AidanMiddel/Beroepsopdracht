#gemaakt door Aidan Middel in SD1Ab

#dit is voor het gebruiken van cmd commands en om kleine wacht tijden te maken voor het beter lezen
import os, time

#introductie van het verhaal
print("Welkom bij mijn verhaal over de vlucht van Salah en zijn familie. \n \nJe bent die ochtend wakker geworden en lekker tijdens het ontbijt kijk je naar het nieuws. \nOp het nieuws zie je dat er een burgeroorlog is uitgebroken. \n \nWat ga je doen? \n ")
print("1. Vluchten dit is niet goedkoop dus je hebt veel geld nodig je komt zo'n $3000 te kort. \n2. Hier blijven")
begin = input("Kies 1 of 2: ")
#je kiest of je gaat vluchten of niet dit heeft best wel inpact op het verhaal
if begin == "1":
    print(" \nOké je kiest om te vluchten maar je komt geld te kort dus wat doe je? \n1. Nog voor een maandje werken. \n2. Kijken of je de smokelaar wat naar benden kan praten")
    vluchten_1= input("Kies 1 of 2: ")
    if vluchten_1 == "1":
        print(" \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
        #ga naar 1 voor mij
        print(" \nJe komt aan bij de vrachtwagen op de dag dat je gaat vluchten richting Europa. \nJe hebt het geld en geeft het aan de smokkelaar. \nJe vrouw is een beetje bang maar het moet maar. \nJe dochter kijkt je ook bang aan maar je autistische zoon snapt er al helemaal niks meer van. \nJe aarzelt nog even wil ik dit echt wel doen? \n1. Ja, het is hier niet meer veilig \n2. Je kijkt nog een keer naar je familie en kiest om toch te blijven gezien de risico te groot is.")
        vluchten_2= input("Kies 1 of 2: ")
        if vluchten_2 == "1":
            print(" \nOké, dus je kiest om gewoon weg te gaan hier is voor nu toch geen toekomst meer.")
            print(" \nDus je gaat zitten achter in de vrachtwagen er zijn een paar families die ook in de vrachtwagen zitten. \nHet is best een hobbelig tripje. \nJe zoon raak een beetje in paniek van alle bewegingen. \nDus je neemt hem op je schoot en rijden verder.")
            print(" \nJullie komen nu eindelijk bij de grens van Jemen en Saudi-Arabië aan, gelukkig gaat de grenscontrole niet jullie vrachtwagen controleren. \nEn jullie komen veilig aan in Saudi-Arabië.")
            print(" \nHelaas zegt je smokkelaar dat wegens omstandig heden jullie niet verder kunnen naar Saudi-Arabië dus eindigt de reis hiervoor nu. \nNou heeft hij een contact die jullie verder kan krijgen die gelijk morgen weggaat. \nGa je gelijk met de hele familie morgen verder vluchten of wacht je nog even in Saudi-Arabië? \n 1. Ja, ik wil hier snel weg \n2. Nah, ik blijf nog even in dit land")
            vluchten_3= input("Kies 1 of 2: ")
            if vluchten_3 == "1":
                print(" \nOké de volgende dag ga je naar het contact wat je hebt gekregen van je smokkelaar. \nHij zet dat hij toevallig nog 4 plaatsen over en hoorde dat wij interesse had dus we kunnen nu instappen.")
                print(" \nHij gaat naar een land genaamd Nederland, je hebt nog nooit van dit land gehoord maar hij zegt dat je daar een goed nieuw begin kan starten. ")
                print(" \nNa een reis van een week in een vrachtwagen kom je aan in Rotterdam waar je wordt geadviseerd om naar het politiebureau te gaan om je te laten registreren in dit land.")
                print(" \nDit doe je ook en na wat papieren kom je in een azc met allemaal aardige mensen en medewerkers")
                print("")
                print("███████╗██╗███╗░░██╗██████╗░███████╗  ░░███╗░░")
                print("██╔════╝██║████╗░██║██╔══██╗██╔════╝  ░████║░░")
                print("█████╗░░██║██╔██╗██║██║░░██║█████╗░░  ██╔██║░░")
                print("██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░  ╚═╝██║░░")
                print("███████╗██║██║░╚███║██████╔╝███████╗  ███████╗")
                print("╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝  ╚══════╝")
                print("")
                print("Dit is einde 1 de reis zonder te veel problemen :) bedankt voor het spelen")
            elif vluchten_3 == "2":
                #ga naar 3 voor mij
            else:
                print("iek spreek geen:" , vluchten_3) 
        elif vluchten_2 == "2":
            print(" \n Vraag je je geld terug? \n1. Nee het zal wel \n2. Ja ik kan het hard gebruiken")
            vluchten_4= input("Kies 1 of 2: ")
            if vluchten_4 == "1":
                print("Je pakt al je spullen en gaat terug naar je huis")
                #ga naar 2
            elif vluchten_4 == "2":
                print("Je vraagt je geld terug maar de smokkelaar kijkt je raar aan en lacht. Sorry maar we geven geen 'refunds' op ons werk ")
                #ga naar 2
            else: 
                print("............. nee")
        else:
            print("iek begrijpen nie")
    elif vluchten_1 == "2":
        print(" \nDit is helaas gefaald dus moet je alsnog gaan werken voor een maandje \n \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
        #ga naar 1 voor mij
    else:
        print("uhm wat")
elif begin == "2":
    print(" \nJe bent al een maand lang gewoon gebleven in Jemen. \nMaar het wordt nu wel een beetje erg de oorlog en je hoort op het nieuws dat het steeds meer jou kant op komt \n wat doe je? \n1. Toch maar vluchten \n2. Toch hier nog een maandje blijven")
    blijven_1 = input("Kies 1 of 2: ")
    if blijven_1 == "1":
        print(" \nOké je kiest om te vluchten maar je komt geld te kort dus wat doe je? \n1. Nog voor een maandje werken. \n2. Kijken of je de smokelaar wat naar benden kan praten")
        vluchten_1= input("Kies 1 of 2: ")
        if vluchten_1 == "1":
            print(" \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
            #ga naar 1 voor mij
        elif vluchten_1 == "2":
            print(" \nDit is helaas gefaald dus moet je alsnog gaan werken voor een maandje \n \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
            #ga naar 1 voor mij
    elif blijven_1 == "2":
        print("Je hoort op het nieuws dat het nu wel erg 'hot' wordt in je regio ga je nu wel of nog steeds niet? \n1. Nee ik zit hier prima voor nu \n2. Ja misschien wordt het eens tijd")
        blijven_2 = input("Kies 1 of 2: ")
        if blijven_2 == "1":
            print("Oké nu een maand later breng je je kinderen naar school. \nMaar op de school staat dat de school is gesloten gezien de dreigingen ga je nu toch maar eens vluchten? \n1. Nee heb geen zin om te vluchten \n2. Ja misschien wordt het eens tijd")
            blijven_3 = input("Kies 1 of 2: ")
            if blijven_3 == "1":
                print("yes")
                #ga naar 2

            elif blijven_3 == "2":
                print(" \nOké je kiest om te vluchten maar je komt geld te kort dus wat doe je? \n1. Nog voor een maandje werken. \n2. Kijken of je de smokelaar wat naar benden kan praten")
                vluchten_1= input("Kies 1 of 2: ")
                if vluchten_1 == "1":
                    print(" \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
                    #ga naar 1 voor mij
                elif vluchten_1 == "2":
                    print(" \nDit is helaas gefaald dus moet je alsnog gaan werken voor een maandje \n \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
                    #ga naar 1 voor mij
                else:
                    print("uhhhh idk man wat je wil het is niet moeilijk om 1 of 2 in te drukken")
            else:
                print("uuuh idk wat dat bedenkt")
        elif blijven_2 == "2":
            print(" \nOké je kiest om te vluchten maar je komt geld te kort dus wat doe je? \n1. Nog voor een maandje werken. \n2. Kijken of je de smokelaar wat naar benden kan praten")
            vluchten_1= input("Kies 1 of 2: ")
            if vluchten_1 == "1":
                print(" \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
                #ga naar 1 voor mij
            elif vluchten_1 == "2":
                print(" \nDit is helaas gefaald dus moet je alsnog gaan werken voor een maandje \n \nOké gelukkig heb je precies $3000 gekregen deze maand \nDus je gaat maar gelijk de volgende dag vluchten \n \nJe bent teruggegaan naar de smokkelaar hij is alleen al vertrokken. \nDus zoek je een nieuwe smokkelaar. \nGelukkig heb je er 1 gevonden die je via een vrachtwagen je naar Europa gaat brengen")
                #ga naar 1 voor mij
            else:
                print("uhhhh idk man wat je wil het is niet moeilijk om 1 of 2 in te drukken")
        else:
            print("")
    else:
        print("uuuhmmm wat")
else:
    print("uhm wat")