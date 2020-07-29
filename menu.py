import game_cycle


def menu():
    option = input("Choose an option:\n1: Single round.\n2: Best of 3..\n3: Madness\n4: Exit\n")
    if option == "1":
        game_cycle.single_round()
    elif option == "4":
        print("Adios!")
        quit()
