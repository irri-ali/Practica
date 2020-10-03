# Practicum opdracht 2
# Exchanger - Ali Sultan
# Hier voer ik hoeveel euro je krijgt voor ieder valuta minus transactiekosten van 1,5 procent waar het minimale bedrag aan
# transactie kosten 2 euro bedraagt en maximaal 15 euro bedraagt.

# Verschillende koersen op 13-9-2020 om 14:45
dollar = 0.844
pound = 1.0801
turk = 0.11


print("Welkom bij wisselkantoor Sultan. Welk valuta wilt u inwisselen?")
# Keuze menu uit 3 keuzes. Keuze schakelt koers gelijk door naar gekozenvaluta en hierna zal koers niet meer aangesproken worden
while True:
    keuze = input("Valuta (1 = US dollar, 2 = GB pounds, 3 = Turkish Lira):")
    if keuze == "1":
        gekozenvaluta = dollar
        valuta = " Dollar"
        break  # Ontsnapt uit loop met dollar voor valuta.
    elif keuze == "2":
        gekozenvaluta = pound
        valuta = " Pound"
        break  # Ontsnapt uit loop met pound voor valuta.
    elif keuze == "3":
        gekozenvaluta = turk
        valuta = " Turkse Lira"
        break  # Ontsnapt uit loop met yen voor valuta.
    print("Dat was een ongeldige keuze. Probeer opnieuw")  # dit wordt uitgeprint als gebruiker iets anders dan 3 kiest

while True:  # loop statement waarin bedrag wordt gevraagd. Als berekende bedrag onder transactiekosten komt valt er niets te exchangen en dan hoeft het programma niet verder te gaan.
    bedrag = float(input(
        "In te wisselen bedrag: "))  # Bedrag wordt later teruggegeven in print mocht het aan onderstaande voorwaardes voldoen.
    if bedrag * gekozenvaluta < 0:  # Bedrag is minder dan 0. Is negatief getal.
        print("Voer een positief bedrag in. We doen niet aan leningen.")
    elif bedrag * gekozenvaluta == 0:  # Bedrag is 0 dus niets ingeleverd
        print("Als je niets geeft, wordt het een lange dag.")
    elif bedrag * gekozenvaluta < 2:
        print("Dit is minder dan het minimum aan transactiekosten.")
    elif bedrag * gekozenvaluta == 2:
        print("Dit zijn slechts de transactiekosten.")
    elif bedrag * gekozenvaluta > 2:
        break  # Hier kan een transactie plaatsvinden. We kunnen uit de loop

brutoeuro = gekozenvaluta * bedrag  # hierna brutoeuro gebruiken voor verdere berekening
transactiekosten = brutoeuro * 0.015
if transactiekosten < 2:
    transactiekosten = 2
if transactiekosten > 15:
    transactiekosten = 15

nettoeuro = brutoeuro - transactiekosten  # Dit is wat de gebruiker ontvangt

print(
    f"Voor {bedrag:.2f}{valuta} krijgt u {brutoeuro:.2f} Euro. De transactiekosten bedragen {transactiekosten:.2f} euro. U ontvangt {nettoeuro:.2f} euro.")
input("Wisselkantoor Sultan wenst u nog een prettige dag. Druk op enter om het programma af te sluiten.")
# Programma wordt afgesloten na enter
