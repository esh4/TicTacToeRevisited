from Player import Player
from inspect import getouterframes, currentframe
from GameBoard import GameBoard


class MinMaxPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.mark = 'O'

    def take_turn(self, board):
        return {self.calculate_best_move(board): self.mark}

    def calculate_best_move(self, board: GameBoard):
        return self.score_move(board)[0]

    def score_move(self, board: GameBoard, my_team_index=0, recursion_level=0):
        teams = ['O', 'X']
        game_over, winner = board.is_game_over()
        if game_over:
            if winner == 'O':
                return None, 100 - recursion_level
            elif winner == 'X':
                return None, -100 + recursion_level
            else:
                return None, 0
        else:   # current board has no score so we score recursively
            move_scores = []
            for move in self.find_available_moves(board):
                to_insert = {move: teams[my_team_index]}
                child_board = board.insert_game_piece(to_insert)
                score = self.score_move(child_board, my_team_index=abs(my_team_index - 1),
                                        recursion_level=recursion_level+1)[1]
                move_scores.append((move, score))

            min_max_score = move_scores[0]
            if recursion_level == 0:
                print(move_scores)
                print(min_max_score)

            for move_score in move_scores:
                # print(move_score, min_max_score, my_team_index == 0)
                if my_team_index == 0:  # maximizing
                    if move_score[1] > min_max_score[1]:
                        min_max_score = move_score
                elif my_team_index == 1:    # minimizing
                    if move_score[1] < min_max_score[1]:
                        min_max_score = move_score

            return min_max_score

    def find_available_moves(self, board: GameBoard):
        ret = []
        for col in range(board.size[0]):
            for row in range(board.size[0]):
                if board.get_board()[row][col] == ' ':
                    ret.append((row, col))
        return ret



