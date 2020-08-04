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
    win_cons = functions.eliminate_space(puzzle, win_cons)
    print("You have to guess " + str(len(win_conditions)) + " letters correctly.")
    while set(win_cons) != set(win_conditions):
        guess = functions.get_guess()
        if guess == puzzle:
            print("You Win!")
            time.sleep(3)
            menu.menu()
        os.system('clear')
        functions.guess_check(win_conditions, win_cons, guess, mistakes)
        if mistakes:
            print("\nYour previous mistakes:")
            for w in mistakes:
                print(w)
        if len(mistakes) == 10:
            print("You Loose!")
            print("The puzzle was " + puzzle + ".")
            time.sleep(2)
            menu.menu()
        functions.print_puzzle(puzzle, win_cons, guess)
    print("You Win!")
    menu.menu()


def best_of_3():
    os.system('clear')
    print("Best of 3 challenge!\nLet's see how many of them you can guess!\nWatch out for capital letters!")
    puzzles = functions.get_puzzles()
    game_puzzles = []
    win_conditions_lists = []
    win_cons = [[], [], []]
    mistakes = [[], [], []]
    wins = 0
    losses = 0
    # adding puzzles to the game puzzles list and win conditions list
    for adding in range(0, 3):
        puzzle = functions.get_puzzle(puzzles)
        if puzzle not in game_puzzles:
            game_puzzles.append(puzzle)
            win_conditions_lists.append(list(set(puzzle)))
            functions.eliminate_space(puzzle, win_cons[adding])
        else:
            functions.get_puzzle(puzzles)
    # for loop defines the game cycle, one puzzle solving each time
    for pz in range(0, 3):
        puzzle = game_puzzles[pz]
        # game cycle per puzzle
        while wins:
            guess = functions.get_guess()
            os.system('clear')
            functions.guess_check(win_conditions_lists[pz], win_cons[pz], guess, mistakes[pz])
            functions.print_puzzle(puzzle, win_cons[pz], guess)
            functions.reveal_previous_mistakes(mistakes[pz])
            losses = functions.loose_check(mistakes, puzzle, losses, wins)
            functions.win_check(win_cons, win_conditions_lists, wins, losses)
            functions.best_of_3_win_check(wins, losses)
