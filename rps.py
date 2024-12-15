import sys, random

def rps(name):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_count = 0

    def play_rps():
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_count
            print(" ")

            playerChoice = input(f"{name}, please enter... \n1 for ROCK, \n2 for PAPER, or \n3 for SCISSORS: \n\n")
            if playerChoice not in ["1", "2", "3"]:
                return play_rps()

            playerChoice = int(playerChoice)

            if playerChoice == 1:
                playerChoice = "ROCK"
            elif playerChoice == 2:
                playerChoice = "PAPER"
            elif playerChoice == 3:
                playerChoice = "SCISSORS"



            computerChoice = random.choice([1, 2, 3])

            if computerChoice == 1:
                computerChoice = "ROCK"
            elif computerChoice == 2:
                computerChoice = "PAPER"
            elif computerChoice == 3:
                computerChoice = "SCISSORS"

            print(" ")
            print(f"{name}, you chose {playerChoice} and the computer chose {computerChoice}.")
            print(" ")

            def check_win(playerChoice, computerChoice):
                nonlocal name
                nonlocal player_wins
                nonlocal computer_wins
                nonlocal tie_count

                if playerChoice == computerChoice:
                    tie_count += 1
                    return "😳 It's a tie!"
                elif playerChoice == "ROCK" and computerChoice == "SCISSORS": 
                    player_wins += 1
                    return f"🥳 {name} You win!"
                elif playerChoice == "PAPER" and computerChoice == "ROCK":
                    player_wins += 1
                    return f"🥳 {name} You win!"
                elif playerChoice == "SCISSORS" and computerChoice == "PAPER":
                    player_wins += 1
                    return f"🥳 {name} You win!"
                else:
                    computer_wins += 1
                    return f"😩 {name}, you lose!"
            
            print(check_win(playerChoice, computerChoice))

            nonlocal game_count
            game_count += 1
            print(f"{name}, you have played {game_count} games.")
            print(f"{name}, you have won {player_wins} times.")
            print(f"The computer has won {computer_wins} times.")
            print(f"{name}, you have tied {tie_count} times.")
            print(" ")

            while True:
                playagain = input(f"{name}, would you like to play again? (y for yes/n for no): ")
                if playagain not in ["y", "n"]:
                    continue
                else:
                    break

            if playagain.lower() == 'y':
                return play_rps()
            else:
                sys.exit(f"Thank you for playing {name}!")
            
            
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Play a game of rock, paper, scissors against the computer"
    )
    parser.add_argument("-n", "--name", metavar="name", help="The name of the person playing the game", required=True)
    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)

    rock_paper_scissors()