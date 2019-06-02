from GameManager import GameManager
from HumanPlayer import HumanPlayer
from MinMaxPlayer import MinMaxPlayer
from GameBoard import GameBoard

p2 = MinMaxPlayer('mm')
p1 = HumanPlayer('e0')

gm = GameManager(p1, p2)

game_over, winner = False, None
while not game_over:
    gm.take_turn()
    game_over, winner = gm.is_game_over()

print(gm.board)
print(winner)
