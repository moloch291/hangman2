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
    win_conditions_lists = []
    win_cons = [[], [], []]
    mistakes = [[], [], []]
    wins = 0
    loses = 0
    for i in range(0, 3):
        puzzle = functions.get_puzzle(puzzles)
        if puzzle not in game_puzzles:
            game_puzzles.append(puzzle)
            win_conditions_lists.append(list(set(puzzle)))
        else:
            functions.get_puzzle(puzzles)
    for i in range(len(game_puzzles)):
        puzzle = game_puzzles[i]
        while set(win_cons[i]) != set(win_conditions_lists[i]):
            guess = functions.get_guess(puzzle)
            os.system('clear')
            functions.guess_check(win_conditions_lists[i], win_cons[i], guess, mistakes[i])
            if len(mistakes[i]) == 10:
                print("Round lost!")
                print("The puzzle was: " + puzzle)
                loses = loses + 1
                print("Loses: " + str(loses))
                print("Wins: " + str(wins))
                time.sleep(3)
            functions.print_puzzle(puzzle, win_cons[i], guess)
            print("\nYour previous mistakes:")
            for w in mistakes[i]:
                print(w)
        print("Round won!")
        wins = wins + 1
        print("Loses: " + str(loses))
        print("Wins: " + str(wins))
    if wins >= 2:
        print("Congratulations! You won " + str(wins) + " out of 3.")
        menu.menu()
    else:
        print("Meh... You lost " + str(loses) + " out of 3.")
        menu.menu()
