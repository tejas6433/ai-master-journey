class Player:
    total_players = 0       # CLASS var — counts all players
    starting_score = 100    # CLASS var — shared default

    def __init__(self, name):
        self.name = name                 # INSTANCE var
        self.score = Player.starting_score
        Player.total_players += 1        # increment on each new player

# YOUR TASK — fill in below:
#  → create 3 players
player1 = Player("Ronaldo")
player2 = Player("Messi")
player3 = Player("Tejas")

#  → print Player.total_players  (should be 3 *Done*)
print(Player.total_players)
#  → print one player's starting score (should be 100)
print(player1.starting_score)
#  → change Player.starting_score to 50
Player.starting_score = 50
#  → create a 4th player, print THEIR score  (should be 50 — proves it's shared)
player4 = Player("Virat")
print(player4.starting_score)
#  → print total_players again  (should be 4)
print(Player.total_players)