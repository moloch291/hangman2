import functions


def single_round():
    puzzles = functions.get_puzzles()
    puzzle = functions.get_puzzle(puzzles)
    win_conditions = functions.get_win_conditions(puzzle)
    mistakes = []
    print(puzzle)
    print("You have to guess " + str(len(win_conditions)) + " letters correctly.")
    for rounds in range(0, 10):
        guess = functions.get_guess(puzzle, mistakes)
        functions.print_puzzle(puzzle, guess, win_conditions)
        print(mistakes)