import functions
import os
import menu
import time


def single_round():
    os.system('clear')
    print("Single word challenge! Watch out for capital letters!")
    puzzles = functions.get_puzzles()
    puzzle = functions.get_puzzle(puzzles)
    win_conditions = functions.get_win_conditions(puzzle)
    win_cons = []
    mistakes = []
    print("You have to guess " + str(len(win_conditions)) + " letters correctly.")
    while set(win_cons) != set(win_conditions):
        guess = functions.get_guess(puzzle)
        os.system('clear')
        functions.guess_check(win_conditions, win_cons, guess, mistakes)
        if len(mistakes) == 10:
            print("You Loose!")
            print("The puzzle was " + puzzle + ".")
            time.sleep(3)
            menu.menu()
        functions.print_puzzle(puzzle, win_cons, guess)
    print("You Win!")
    menu.menu()


def best_of_3():
    os.system('clear')
    print("Best of 3 challenge!\nLet's see how many of them you can guess!")
    puzzles = functions.get_puzzles()
    game_puzzles = []
    for i in range(0, 3):
        puzzle = functions.get_puzzle(puzzles)
        if puzzle not in game_puzzles:
            game_puzzles.append(puzzle)
        else:
            functions.get_puzzle(puzzles)
    print(game_puzzles)
