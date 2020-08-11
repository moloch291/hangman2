import game_cycle
import os


def menu():
    os.system('clear')
    option = input("Choose an option:\n1: Single round.\n2: Best of 3..\n3: Madness\n4: Exit\n")
    if option == "1":
        game_cycle.single_round()
    elif option == "2":
        game_cycle.best_of_3()
    elif option == "3":
        game_cycle.madness()
    elif option == "4":
        print("Adios!")
        quit()
