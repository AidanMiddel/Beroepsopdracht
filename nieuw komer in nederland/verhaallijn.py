#dit is voor het inlezen van text bestanden
import io

#open de text in ram in read mode
test = open("test.txt", "r")

#lees wat de tekst zegt in het bestand
test_lees = test.read()

#laat zien wat er in het bestand staat
print (test_lees)

#kleine pauze voordat het programma exit
yes = input()