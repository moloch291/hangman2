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


def get_guess(puzzle):
    guess = input("\nTake a guess! ")
    if guess == puzzle:
        print("You Win!")
        menu.menu()
    elif guess == "quit":
        menu.menu()
    return guess


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
