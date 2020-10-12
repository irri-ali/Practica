# isTussen applicatie Ali Sultan Practicum 5:
# https://github.com/irri-ali/Practica
# Deze app vraagt om input van gebruiker: hartslag, temperatuur en onder en bovendruk. Gemiddeld genomen heeft een
# gezond persoonde volgende waarden:hartslag tussen 55 en 90 slagen per minuut, lichaamstemperatuur tussen 36.3 en 37.5
# graden Celsius, bovendruk tussen 100 en 140 mm Hg. Grenzen doen mee.
import sys


# Eerst de functie istussen
def istussen(hartslag, temperatuur, bovendruk):
    if 90 >= hartslag >= 55:
        resulta = "Hartslag is goed."
    elif 90 < hartslag:
        resulta = "Uw hartslag is te hoog."
    else:
        resulta = "Uw hartslag is te laag"
    if 37.5 >= temperatuur >= 36.3:
        resultb = "Uw temperatuur is goed."
    elif 37.5 < temperatuur:
        resultb = "Uw temperatuur it te hoog. "
    else:
        resultb = "Uw temperatuur is te laag."
    if 140 >= bovendruk >= 100:
        resultc = "Uw bovendruk is goed."
    elif 140 < bovendruk:
        resultc = "Uw bovendruk is te hoog."
    else:
        resultc = "Uw bovendruk is te laag"
    return print(resulta, resultb, resultc)


# Foutacceptatie en daarin een quit-functie
def errorhandled(humaninput):
    quitlist = ['quit', 'Quit', 'q', "Q"]
    while not humaninput.isnumeric() or humaninput == '':
        if humaninput in quitlist:
            sys.exit(0)
        humaninput = input(f"Geef alstublieft een getal.")
    else:
        humanoutput = float(humaninput)
    return humanoutput


# Daarna de input van gebruiker opslaan naar variabelen
HartSlag = errorhandled(input("Hoe hoog is uw hartslag?"))
LichaamsTemperatuur = errorhandled(input("Wat is uw lichaamstemperatuur?"))
BovenDruk = errorhandled(input("Hoeveel mm Hg is uw bovendruk?"))

# Stop input in functie isTussen dat ook de resultaten print
istussen(HartSlag, LichaamsTemperatuur, BovenDruk)
