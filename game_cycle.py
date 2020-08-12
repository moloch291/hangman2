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


def madness_main():
    wins = 0
    losses = 0
    round_counter = 0
    print("Puzzle number {}:".format(round_counter))
    if losses == 0:
        round_counter = round_counter + 1
        madness(wins, losses)
        return round_counter
    else:
        print("You lost! You solved {} puzzles".format(round_counter + 1))
        menu.menu()


def madness():
    os.system('clear')
    wins = 0
    losses = 0
    round_counter = 0
    print("You have to solve puzzles!\nLet's see how many of them can you solve in a row...")
    while losses == 0:
        round_counter = round_counter + 1
        puzzles = functions.get_puzzles()
        puzzle = functions.get_puzzle(puzzles)
        win_conditions = functions.get_win_conditions(puzzle)
        win_cons = []
        mistakes = []
        print("You have to guess " + str(len(win_conditions)) + " letters correctly!")
        win_cons = functions.eliminate_spaces(win_cons, puzzle)
        # game cycle per puzzle:
        while set(win_cons) != set(win_conditions):
            guess = functions.get_guess()
            # instant win statement:
            if guess == puzzle:
                wins = functions.update_wins(wins, losses)
                time.sleep(3)
            os.system('clear')
            functions.guess_check(win_conditions, win_cons, guess, mistakes)
            functions.print_mistakes(mistakes)
            # lost round statement:
            if len(mistakes) == 10:
                losses = functions.update_losses(wins, losses, puzzle)
                time.sleep(2)
            functions.print_puzzle(puzzle, win_cons, guess)
        wins = functions.update_wins(wins, losses)
        time.sleep(2)
    print("Your lost! You solved {} puzzles.".format(wins))


#def best_of_3():
