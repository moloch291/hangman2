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


def get_guess(puzzle, mistakes):
    guess = input("Take a guess! ")
    if guess in puzzle:
        return guess
    elif guess == puzzle:
        print("You Win!")
        menu.menu()
    else:
        print("Mistake!")
        return guess


def print_puzzle(puzzle, win_conditions, guess):
    for w in range(0, len(puzzle[0:])):
        if puzzle[w] == guess or puzzle[w] in win_conditions:
            print(puzzle[w], end="")
        elif puzzle[w] == " ":
            print(" ", end="")
        else:
            print("_", end="")
