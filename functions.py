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


def add_puzzle(puzzles, game_puzzles, win_conditions_lists, win_cons):
    for adding in range(0, 3):
        puzzle = get_puzzle(puzzles)
        if puzzle not in game_puzzles:
            game_puzzles.append(puzzle)
            win_conditions_lists.append(list(set(puzzle)))
            eliminate_space(puzzle, win_cons[adding])
        else:
            get_puzzle(puzzles)


def analyze_score(wins, losses):
    if wins >= 2:
        print("Congratulations! You won " + str(wins) + " out of 3.")
        menu.menu()
    else:
        print("Meh... You lost " + str(losses) + " out of 3.")
        menu.menu()


def reveal_previous_mistakes(mistakes):
    if mistakes:
        print("\nYour previous mistakes:")
        for element in mistakes:
            print(element)


def loose_check(mistakes, puzzle):
    if len(mistakes) == 10:
        print("Round lost!")
        print("The puzzle was: " + puzzle)
        return True
    else:
        return False


def update_losses(losses, wins):
    losses = losses + 1
    print("Loses: " + str(losses))
    print("Wins: " + str(wins))
    return losses


def win_check(win_cons, win_conditions_lists):
    if set(win_cons) == set(win_conditions_lists):
        print("Round won!")
        return True
    else:
        return False


def update_wins(wins, losses):
    print("You Loose!")
    print("Wins: " + str(wins) + "Losses: " + str(losses))
    wins = wins + 1
    return wins


def update_losses(wins, losses, puzzle):
    print("You Loose!")
    print("The puzzle was " + puzzle + ".")
    print("Wins: " + str(wins) + "Losses: " + str(losses))
    losses = losses + 1
    return losses


def add_puzzles(puzzles):
    game_puzzles = []
    for adding in range(0, 3):
        puzzle = get_puzzle(puzzles)
        if puzzle not in game_puzzles:
            game_puzzles.append(puzzle)
        else:
            get_puzzle(puzzles)
    return game_puzzles


def add_win_conditions_lists(game_puzzles):
    print(game_puzzles)
    win_conditions_lists = []
    for puzzle in game_puzzles:
        win_conditions_lists.append(list(set(puzzle)))
    print(win_conditions_lists)
    return win_conditions_lists


def eliminate_spaces(win_cons, game_puzzles):
    for strings in game_puzzles:
        for char in range(len(strings)):
            if char == " ":
                win_cons = win_cons.append(" ")
        return win_cons


def print_mistakes(mistakes):
    if mistakes:
        print("\nYour previous mistakes:")
        for w in mistakes:
            print(w)


