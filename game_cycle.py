import functions


def single_round():
    puzzles = functions.get_puzzles()
    puzzle = functions.get_puzzle(puzzles)
    win_conditions = functions.get_win_conditions(puzzle)
    win_cons = []
    mistakes = []
    print(puzzle)
    print("You have to guess " + str(len(win_conditions)) + " letters correctly.")
    for rounds in range(0, 10):
        guess = functions.get_guess()
        win_cons = functions.guess_check(guess, puzzle, mistakes, win_cons)
        functions.print_puzzle(puzzle, guess, win_cons)
        print(mistakes)
        print(win_cons)