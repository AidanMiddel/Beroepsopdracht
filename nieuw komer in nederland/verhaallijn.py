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
                print(" \nJe pakt al je spullen en gaat terug naar je huis")
                #ga naar 2
                print(" \nAls je toch niet gaat vluchten kleine update het wordt steeds 'hotter' in jouw gebied en na 3 maanden zie je dat de school van je kinderen is afgesloten maar je besluit om toch maar niet te vluchten voor nu")
                print("De volgende dag word je rustig (nou hoe rustig het nog is) wakker tot je ineens een keiharde knal hoort buiten waar je best van schrikt en je gaat eens kijken wat die knal is. \nJe komt buiten maar ziet niet gelijk wat het is dus je gaat weer naar binnen en zet de tv aan. \nOp de tv zie je dat er een bom is laten ontploffen in het dorp hiernaast. \nWat doe je? \n1. Je familie wakker maken en zeggen dat we hier zo snel mogelijk weg moet en gaan. \n2. Rustig verder gaan met je ontbijt en straks overleggen met je vrouw")
                blijven_4= input("Kies 1 of 2: ")
                if blijven_4 == "1":
                    print(" \nJe maakt iedereen wakker en zegt dat ze alles wat ze willen houden moeten inpakken want we gaan hier nu weg. \nNa 15 min is iedereen klaar en stap je in de auto en rij je rustig naar het noorden van Jemen")
                    print(" \nNa een 15 minuten rijden richting noord zie je de schade die de oorlog tot nu toe heeft aangebracht op de radio hoor je dat er op je dorp een bom is geland. \nJe besluit om maar flink door te rijden. ")
                    print(" \nUiteindelijk kom je aan in Saudi-Arabië zonder gewond te raken. \nJe besluit hier te blijven en een leven opnieuw hier te starten\n")
                    print("███████╗██╗███╗░░██╗██████╗░███████╗  ██████╗░")
                    print("██╔════╝██║████╗░██║██╔══██╗██╔════╝  ╚════██╗")
                    print("█████╗░░██║██╔██╗██║██║░░██║█████╗░░  ░░███╔═╝")
                    print("██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░  ██╔══╝░░")
                    print("███████╗██║██║░╚███║██████╔╝███████╗  ███████╗")
                    print("╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝  ╚══════╝")
                    print(" \nDit is einde 2 het net ontsnappen van een bom en lekker in Saudi-Arabië een nieuw leven opbouwen")
                elif blijven_4 == "2":
                    print("Nadat je vrouw ook wakker is en binnenkomt zegt ze dat ze een grote knal hoorde. \nJe vertelt dat in het dorp hiernaast een bom is afgegaan. \nJe vrouw schrikt van het nieuws en stelt voor dat we misschien moeten gaan vluchten? \nGa je hierin mee? \n1. Nee het is hier naast het dorp en het leger is al onderweg deze kant op \n2. Ja laten we hier maar zo snel mogelijk vertrekken")
                    blijven_5 = input("Kies 1 of 2: ")
                    if blijven_5 == "1":
                        print(" \nJe kinderen komen net binnen omdat ze ook wakker waren geworden door de knal. \nJe vertelt ze dat het niet erg is omdat het leger toch onderweg is om de rellen buiten ons dorp te laten.")
                        print(" \nDus je gaat verder met je ontbijt met de familie.  \nJe dochter vraagt of het nog wel slim is om hier te blijven en je laat haar nog weten een keer weten dat het goed komt. ")
                        print(" \nEn dan land er een bom op je dorp \n")
                        print("███████╗██╗███╗░░██╗██████╗░███████╗  ░░██╗██╗")
                        print("██╔════╝██║████╗░██║██╔══██╗██╔════╝  ░██╔╝██║")
                        print("█████╗░░██║██╔██╗██║██║░░██║█████╗░░  ██╔╝░██║")
                        print("██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░  ███████║")
                        print("███████╗██║██║░╚███║██████╔╝███████╗  ╚════██║")
                        print("╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝  ░░░░░╚═╝")
                        print(" \ndi is einde 4 het eigenwijs blijven zitten met geen happy ending")
                    elif blijven_5 == "2":
                        print(" \nJe maakt iedereen wakker en zegt dat ze alles wat ze willen houden moeten inpakken want we gaan hier nu weg. \nNa 15 min is iedereen klaar en stap je in de auto en rij je rustig naar het noorden van Jemen")
                        print(" \nNa een 15 minuten rijden richting noord zie je de schade die de oorlog tot nu toe heeft aangebracht op de radio hoor je dat er op je dorp een bom is geland. \nJe besluit om maar flink door te rijden. ")
                        print(" \nUiteindelijk kom je aan in Saudi-Arabië zonder gewond te raken. \nJe besluit hier te blijven en een leven opnieuw hier te starten\n")
                        print("███████╗██╗███╗░░██╗██████╗░███████╗  ██████╗░")
                        print("██╔════╝██║████╗░██║██╔══██╗██╔════╝  ╚════██╗")
                        print("█████╗░░██║██╔██╗██║██║░░██║█████╗░░  ░░███╔═╝")
                        print("██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░  ██╔══╝░░")
                        print("███████╗██║██║░╚███║██████╔╝███████╗  ███████╗")
                        print("╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝  ╚══════╝")
                        print(" \nDit is einde 2 het net ontsnappen van een bom en lekker in Saudi-Arabië een nieuw leven opbouwen")")
                    else:
                        print("boo")
                else:
                    print("1 of 2 het is niet moeilijk")
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