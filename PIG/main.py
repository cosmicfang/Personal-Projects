import random

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.total_score = 0

    def roll(self):
        return random.randint(1, 5)

    def play_turn(self):
        current_score = 0
        print(f"{self.player_name}'s turn has started")
        while True:
            roll_or_not = input("Wanna continue or not? Op are - y, q")
            if roll_or_not != 'y' and roll_or_not != 'q':
                break
            if roll_or_not == 'q':
                quit()
            roll_value = self.roll()   #if 'y'
            if roll_value == 1:
                print(f"{self.player_name} rolled a 1, so no points")
                current_score = 0
                break
            else:
                current_score += roll_value
                print(f"{self.player_name} rolled a {roll_value}.")
        self.total_score += current_score
        print(f"{self.player_name}'s total score is {self.total_score}")


class DiceGame:
    def __init__(self, players):
        self.players = []
        self.max_score = 50

    def get_player_count(self):
        while True:
            player_input = input("Enter the number of players (2-4) ")
            if player_input.isdigit():
                num_players = int(player_input)
                if 2 <= num_players <= 4:
                    for player in self.players:
                        # create pbjects for each of the player in player[] list
                        self.players.append(Player(f"Player {player+1}"))
                    break
                else:
                    print("Invalid")
            else:
                print("Invalid")

    def play_game(self):
        self.get_player_count()
        while True:
            for player in self.players:
                player.play_turn()
                if player.total_score >= self.max_score:
                    print(f"\n{player.nane} wins with a score of {player.total_score}")
                    return

if __name__ == "__main__":
    game = DiceGame()
    game.play_game()