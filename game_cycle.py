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
    game_puzzles = functions.add_puzzles(puzzles)
    win_cons = [[], [], []]
    mistakes = [[], [], []]
    win_conditions_lists = functions.add_win_conditions_lists(game_puzzles)
    for adding in range(0, 3):
        win_cons[adding] = functions.eliminate_spaces(game_puzzles, win_cons)
    wins = 0
    losses = 0
    for rnd in range(0, 3):
        puzzle = game_puzzles[rnd]
        while functions.win_check(win_cons[rnd], win_conditions_lists[rnd]) and functions.loose_check(mistakes[rnd],
                                                                                                      puzzle):
            guess = functions.get_guess()
            os.system('clear')
            guess = functions.guess_check(win_conditions_lists[rnd], win_cons[rnd], guess, mistakes[rnd])
            functions.print_puzzle(puzzle, win_cons[rnd], guess)
            functions.reveal_previous_mistakes(mistakes[rnd])
            functions.win_check(win_cons[rnd], win_conditions_lists[rnd])
            functions.loose_check(mistakes[rnd], puzzle)
        wins = functions.update_wins(wins, losses)
        losses = functions.update_wins(wins, losses)
