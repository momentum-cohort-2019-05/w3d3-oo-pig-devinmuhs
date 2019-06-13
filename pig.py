import random

class GameClass:
    def __init__(self):
        self.player1 = Player("Devin")
        self.player2 = Player("Computer")
    
    def player_selection(self):
        players = []
        players.append(self.player1)
        players.append(self.player2)
        print(players)
        # random_player = random.choice(players)
        # print(random_player)
    def round(self):

        
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.score = 0

        
class Computer:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# die = Dice()
# rolled = die.roll()

class Turn:
    def __init__(self, turn, conditions, hold, roll):
        self.turn = turn
        self.conditions = conditions
    # def
        

if __name__ == "__main__":
    die = Dice()
    rolled = die.roll()
    
    


# class Turn:
#     def __init__(self, )