import functions
import os
import menu


def single_round():
    os.system('clear')
    puzzles = functions.get_puzzles()
    puzzle = functions.get_puzzle(puzzles)
    win_conditions = functions.get_win_conditions(puzzle)
    win_cons = []
    mistakes = []
    print("You have to guess " + str(len(win_conditions)) + " letters correctly.")
    while set(win_cons) != set(win_conditions):
        os.system('clear')
        guess = functions.get_guess()
        functions.guess_check(win_conditions, win_cons, guess, mistakes)
        if len(mistakes) == 10:
            print("You Loose!")
            menu.menu()
        functions.print_puzzle(puzzle, win_cons, guess)
    print("The puzzle was " + puzzle + " !")
    print("\nYou Win!")
    menu.menu()
