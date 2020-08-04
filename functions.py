import random
import csv
import menu


def get_puzzles():
    puzzles = []
    with open("words.csv", "r+") as puzzle_list:
        puzzle_list = csv.reader(puzzle_list)
        for row in puzzle_list:
            for puzzle in row:
                puzzles.append(puzzle)
        return puzzles


def get_puzzle(puzzles):
    puzzle = random.choice(puzzles)
    return puzzle


def get_win_conditions(puzzle):
    win_conditions = list(set(puzzle))
    return win_conditions


def get_guess():
    guess = input("\nTake a guess! ")
    if guess == "quit":
        menu.menu()
    return guess


def eliminate_space(puzzle, win_cons):
    for i in range(len(puzzle)):
        if puzzle[i] == " ":
            win_cons = win_cons.append(puzzle[i])
            return win_cons


def guess_check(win_conditions, win_cons, guess, mistakes):
    if guess in win_conditions:
        win_cons = win_cons.append(guess)
        return win_cons
    else:
        print("Mistake!")
        mistakes = mistakes.append(guess)
        return mistakes


def print_puzzle(puzzle, win_cons, guess):
    for w in range(0, len(puzzle[0:])):
        if puzzle[w] == guess or puzzle[w] in win_cons:
            print(puzzle[w], end="")
        elif puzzle[w] == " ":
            print(" ", end="")
        else:
            print("_", end="")


def best_of_3_win_check(wins, losses):
    if wins >= 2:
        print("Congratulations! You won " + str(wins) + " out of 3.")
        menu.menu()
    else:
        print("Meh... You lost " + str(losses) + " out of 3.")
        menu.menu()


def comment_on_score(wins, losses):
    if wins >= 2:
        print("Congratulations! You won " + str(wins) + " out of 3.")
        menu.menu()
    else:
        print("Meh... You lost " + str(losses) + " out of 3.")
        menu.menu()
