from Player import Player
from GameBoard import GameBoard


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.mark: str = 'X'

    def set_mark(self, m):
        self.mark = m

    def take_turn(self, move_callback=lambda: input('x, y:     ').split(',')):
        location = move_callback()
        location = (int(location[0]), int(location[1]))
        to_play = {location: self.mark}
        return to_play
