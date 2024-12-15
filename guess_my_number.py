import sys, random

def guess_my_number(name):
    game_count = 0
    player_wins = 0
    number = random.choice([1, 2, 3])
    print(f"{name}, I am thinking of a number between 1 and 3. Can you guess it?")
    guess = input("Enter your guess: ")
    def check_guess(guess):
        nonlocal name
        nonlocal number
        if guess < 1 or guess > 3:
            return guess_my_number(name)
        elif type(guess) != int:
            return guess_my_number(name)
        else:
            return guess
    user_guess = check_guess(int(guess))
    def check_win(user_guess, number):
        nonlocal name
        nonlocal player_wins
        if user_guess == number:
            player_wins += 1
            return f"😎 {name}, you choose {user_guess}, I choose {number}. You win!"
        else:
            return f"😩 {name}, you choose {user_guess}, I choose {number}. You lose!"
    print(check_win(user_guess, number))

    game_count += 1
    print(f"{name}, you won {player_wins} out of {game_count} games")
    print(f"{name}, your winning pecentage is {round((player_wins / game_count) * 100, 2)}%")

    while True:
        play_again = input(f"{name}, would you like to play again? (y/n): ")
        if play_again.lower() not in ["y", "n"]:
            continue
        else:
            if play_again.lower() == "y":
                guess_my_number(name)
            else:
                sys.exit(f"{name}, you won {player_wins} out of {game_count} games. Your winning pecentage is {round((player_wins / game_count) * 100, 2)}%")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Play a game of guess my number against the computer"
    )
    parser.add_argument("-n", "--name", metavar="name", help="The name of the person playing the game", required=True)
    args = parser.parse_args()
    guess_my_number(args.name)