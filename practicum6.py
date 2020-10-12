import random
import subprocess
from datetime import datetime
dateTimeObj = datetime.now()

subprocess.call("cls", shell=True)

spawn_list = []
history_list = []

def anyexit(humaninput):
    list_stop = ["Q", "q", "quit", "Quit", "Stop", "stop"]
    if humaninput in list_stop:
        quit("Tot de volgende keer.")
        return 0
    else:
        return humaninput


def lettercorrecter(stringinput):
    while not stringinput.isnumeric() or stringinput == '':
        stringinput = input(f"Geef alstublieft een getal.")
    else:
        stringinput = int(stringinput)
        return stringinput


def five_twentyfiverange(stringinput):
    while True:
        numbersinput = lettercorrecter(stringinput)
        if 5 <= numbersinput <= 25:
            return numbersinput
        stringinput = input("Dit is geen getal tussen de 5 en de 25. Probeert u opnieuw.")


def intro():
    print("Welkom bij de randommatcher")
    menu()


def menu():
    subprocess.call("cls", shell=True)
    one_list = ["1", "one", "One", "Een", "een", "EEN"]
    two_list = ["2", "Two", "TWO", "two", "twee", "TWEE", "Twee"]
    print("Kies 1 voor een nieuwe reeks getallen.")
    print("Kies 2 voor jouw geschiedenisoverzicht.")
    print("Voer op elk moment stop in om het programma te beindigen.")
    print("")
    entry_user = anyexit(input(""))
    if entry_user in one_list:
        numbers_menu()
    elif entry_user in two_list:
        history_menu()
    else:
        print("U voerde geen geldige invoer. Probeer het opnieuw.")
        menu()


def numbers_menu():
    subprocess.call("cls", shell=True)
    spawn_list = []
    print("dit is de random menu")
    number_of_spawns = five_twentyfiverange(anyexit(input("Hoe groot moet de lijst getallen zijn [5 - 25]? ")))
    print(f"U heeft {number_of_spawns} keer een getal tussen de 0 en 10 gegenereerd.")
    random_number = random.randint(0, 10)
    str(random_number)
    for i in range(number_of_spawns):
        spawn_list.append(f"{random_number}")
        random_number = random.randint(0, 10)
    print(", ".join(spawn_list), end='.\n')
    search_number = anyexit(input("Welke getal moet ik zoeken?"))
    print(f"Ik moet het getal {search_number} zoeken.")
    index = 0
    count = 0
    while index < len(spawn_list):
       if spawn_list[index] == search_number:
           count += 1
       index += 1
    print(f"Het getal {search_number} komt {count} keer voor.")
    percentage_of_numbers = (count / len(spawn_list)) * 100
    print(f"Het getal {search_number} komt {percentage_of_numbers} procent voor.")
    history_list.append(f"Je getallen reeks {spawn_list}.")
    anyexit(input("Druk een toets om verder te gaan."))
    spawn_list.clear()
    menu()


def history_menu():
    subprocess.call("cls", shell=True)
    print("dit is jouw historie menu.")
    index_history = 0
    while index_history < len(history_list):
        print(history_list[index_history])
        index_history += 1
        print("\n")
    anyexit(input("Druk een toets om terug naar het menu te gaan."))
    menu()


intro()
