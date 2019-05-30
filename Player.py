from GameBoard import GameBoard


class Player:
    def __init__(self, name):
        self.name = name

    def take_turn(self, game_board: GameBoard):
        raise NotImplementedError
