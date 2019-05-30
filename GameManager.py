from GameBoard import GameBoard
from random import Random


class GameManager:
    def __init__(self, player1, player2):
        self.size = (3, 3)

        self.board = GameBoard(size=self.size)#, preset=[['X', 'O', 'X'],['O', ' ', 'X'],[' ', ' ', 'O']])
        self.players = [player1, player2]
        self.turn_num = 0
        self.current_player = 0
        self.all_boards = []

    def take_turn(self):
        print(self.board)
        self.all_boards.append(self.board)

        move = self.players[self.current_player].take_turn(self.board)
        self.board = self.board.insert_game_piece(move)

        # print(self.board)

        self.current_player = abs(self.current_player - 1)

    def is_game_over(self):
        # TODO: return winner object (or name)
        return self.board.is_game_over()
