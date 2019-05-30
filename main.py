from GameManager import GameManager
from HumanPlayer import HumanPlayer
from MinMaxPlayer import MinMaxPlayer


p1 = HumanPlayer('e0')
p2 = HumanPlayer('s')

gm = GameManager(p1, p2)

while not gm.is_game_over():
    gm.take_turn()

