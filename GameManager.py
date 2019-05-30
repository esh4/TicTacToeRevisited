from GameBoard import GameBoard
from random import Random


class GameManager:
    def __init__(self, player1, player2):
        self.board = GameBoard()
        self.players = [player1, player2]
        self.turn_num = 0
        self.current_player = 0#Random().randint(0, 1)

        self.all_boards = []

    def take_turn(self):
        self.all_boards.append(self.board)

        move = self.players[self.current_player].take_turn()
        self.board = self.board.make_move(move)
        print(self.board)

        self.current_player = abs(self.current_player - 1)

    def is_game_over(self):
        pass
