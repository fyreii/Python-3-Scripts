import random

"""

Teresa Henderson
CST 100 - Bansal
05/31/2016

assign3.py

Offers users a choice of game to play:
1.  Number Guessing Game
2.  RoShamBo (Rock, Paper, Scissors)

06/01/2016 - added input validation for numbers guessing game
           - refined game menu
           - added title screen for RoShamBo
06/03/2016 - Refined determine_winner()

"""


def guessing_game():
    # answer is set to a random integer
    # between 1 and 20 inclusive
    number = int(random.randint(1, 20))
    # number of tries counter initially set to 1 because
    # we want the first number of logged tries to be 1 and not 0
    numAttempts = 1

    # Create a title screen for the game ...
    print("\n")
    print("#############################################")
    print("Welcome to the Numbers Guessing Game!")
    print("#############################################")
    print("\n")
    # ask for the player's name
    name = input("Please enter your name: ")
    # Get a number to guess against the generated one
    print("Okay " + name + " I am thinking of a number...")
    print("\n")

    # This input validation sequence referenced from stackoverflow and the article
    # posted in Discussion Board 3 topic "Input Validation"
    #
    # http://stackoverflow.com/questions/11594605/python-excepting-input-only-if-in-range
    # http://www.tldp.org/LDP/LG/issue83/evans.html

    # This loop is always true - the user must enter a valid number to continue
    while True:
        try:
            # prompt for the user to enter a number
            guess = int(input("Please enter a number between 1 and 20: "))
        # if the value is invalid due to type or value, throw exception
        except (TypeError, ValueError):
            print("You entered an invalid option!")
        # if input passes check in else, break out of loop and continue
        # the program
        else:
            # This method of defining a range was recommended for
            # performance purposes on several boards
            if 1 <= guess <= 20:
                break

    # this loop is only true if numAttempts is less than max
    while numAttempts < 3:
        # if the guess is less than the number increment one
        if guess < number:
            guess = int(input("Too low, guess again: "))
            numAttempts += 1
        # if the guess is more than the number increment one
        elif guess > number:
            guess = int(input("Too high, guess again: "))
            numAttempts += 1
        # if neither condition above is true, the guess must be correct
        else:
            print("\nYour guess of " + str(guess) + " is correct!")
            print("It took you this many tries: " + str(numAttempts))
            break
    # this else is for the while loop - it returns the outcome
    # if none of the statements inside it are true and
    # if the guess does not match the number in the allotted
    # number of tries (3)
    else:
        print("You did not guess in 3 tries!")
        print("The number I was thinking of was: " + str(number))

"""
R-P-S criteria:

Choice => Defeated By
---------------------
Rock => Paper
Paper => Scissors
Scissors => Rock
Choice <=> Choice == No winner

"""


def roshambo_game():

    # Create a title screen for the game ...
    print("\n")
    print("#############################################")
    print("Welcome to Ro-Sham-Bo!")
    print("#############################################")
    print("\n")

    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")

    play_game(player1, player2)


def play_game(player1, player2):

    # set control variable
    cont = 'y'

    # keeps track of my scores
    games = 0
    p1_score = 0
    p2_score = 0

    # fixed strings
    player1_wins = "Player 1 " + str(player1) + " Wins!"
    player2_wins = "Player 2 " + str(player2) + " Wins!"
    no_winner = "No Winner"

    while cont != 'n':

        print("   (R)OCK     ", "   (P)APER    ", "  (S)CISSORS  ")

        player1_choice = input(player1 + ", please enter your choice: ")
        p1_choice = player1_choice.lower()

        if p1_choice == 'r':
            print("    _______ ")
            print("---'   ____)")
            print("     (_____)")
            print("     (_____)")
            print("     (____) ")
            print("---.__(___) ")
            print("\n")
            print(player1 + " chose ROCK!")
        elif p1_choice == 'p':
            print("    _______ ")
            print("---'   ____)____")
            print("          ______)")
            print("         _______)")
            print("        _______)")
            print("---.__________)")
            print("\n")
            print(player1 + " chose PAPER!")
        elif p1_choice == 's':
            print("   _______   ")
            print("---'  ____)__")
            print("       ______)")
            print("    __________)")
            print("     (____)")
            print(" --.__(___)")
            print("\n")
            print(player1 + " chose SCISSORS!")
        else:
            raise ValueError("Please choose a valid option!")

        player2_choice = input(player2 + ", please enter your choice: ")
        p2_choice = player2_choice.lower()

        if p2_choice == 'r':
            print("    _______ ")
            print("---'   ____)")
            print("     (_____)")
            print("     (_____)")
            print("     (____) ")
            print("---.__(___) ")
            print("\n")
            print(player2 + " chose ROCK!")
        elif p2_choice == 'p':
            print("    _______ ")
            print("---'   ____)____")
            print("          ______)")
            print("         _______)")
            print("        _______)")
            print("---.__________)")
            print("\n")
            print(player2 + " chose PAPER!")
        elif p2_choice == 's':
            print("   _______   ")
            print("---'  ____)__")
            print("       ______)")
            print("    __________)")
            print("     (____)")
            print(" --.__(___)")
            print("\n")
            print(player2 + " chose SCISSORS!")
        else:
            raise ValueError("Please choose a valid option!")

        game_results = determine_winner(p1_choice, p2_choice)

        # increment the number of games played
        # to calculate the final score
        games += 1
        # choose the winner based on
        # results passed to
        # determine_winner function
        if game_results == 0:
            print(no_winner)
        elif game_results == 1:
            p1_score += 1
            print(player1_wins)
        elif game_results == 2:
            p2_score += 1
            print(player2_wins)

        # gives the user the chance to play roshambo as often as they wish
        play_again_prompt = input("Want to play again? (y/n): ")
        cont = play_again_prompt.lower()

    print("------------------------")
    print("Total Games Played: " + str(games))
    print("The final scores are: ")
    print("------------------------")
    print(player1 + ": " + str(p1_score))
    print(player2 + ": " + str(p2_score))
    print("\n")
    if p1_score > p2_score:
        print(player1 + " is the Ro-Sham-Bo Champion!")
        print("\n")
    elif p1_score < p2_score:
        print(player2 + " is the Ro-Sham-Bo Champion!")
        print("\n")
    else:
        print("It's a tie!")


# Also referenced:
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences


def determine_winner(choice1, choice2):

    # this dictionary uses tuples as keys that
    # represent all possible combinations for
    # both players in the game

    game_states = {
        # tuple key : outcome
        ('p', 'r'): 1,
        ('r', 'p'): 2,
        ('s', 'p'): 1,
        ('p', 's'): 2,
        ('r', 's'): 1,
        ('s', 'r'): 2,
        ('r', 'r'): 0,
        ('p', 'p'): 0,
        ('s', 's'): 0
    }

    return game_states[choice1, choice2]


def main_menu():
    # create a main menu for the games
    # provide an exit sequence and a sanity check
    print("\n")
    print("Welcome to CST 100 Assignment 3!")
    print("\n")
    print("-------------------")
    print("Available games: ")
    print("-------------------")
    print("1. Number Guessing Game")
    print("2. Ro-Sham-Bo (Rock, Paper, Scissors)")
    print("3. Exit Menu")
    print("\n")

    game = int(input("Please choose a game to play: "))

    if game == 1:
        guessing_game()
    elif game == 2:
        roshambo_game()
    elif game == 3:
        print("Goodbye!")
        exit(0)
    else:
        raise ValueError("You did not pick a valid option.")


main_menu()

