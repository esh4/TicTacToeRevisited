from Player import Player
from inspect import getouterframes, currentframe
from GameBoard import GameBoard


class MinMaxPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.mark = 'O'

    def take_turn(self, board):
        return {self.calculate_best_move(board): self.mark}

    def calculate_best_move(self, board: GameBoard) -> int:
        # find all available moves
        moves = []
        for move in self.find_available_moves(board):
            moves.append((move, self.score_move(board, move)))

        print(moves)

        best_move = ()
        max_score = -10
        for move in moves:
            if move[1] > max_score:
                best_move = move[0]
                max_score = move[1]

        return best_move

    def score_move(self, board: GameBoard, move, my_team_index=0, recursion_level=1):
        teams = ['O', 'X']
        new_board = board.insert_game_piece({move: teams[my_team_index]})
        game_over, winner = new_board.is_game_over()
        if game_over:
            if winner == 'O':
                return 10 - recursion_level
            elif winner == 'X':
                return -10 + recursion_level
            else:
                return 0
        else:   # current board has no score so we score recursively
            move_scores = []
            for move in self.find_available_moves(new_board):
                to_insert = {move: teams[abs(my_team_index - 1)]}
                # print(to_insert)
                new_board = new_board.insert_game_piece(to_insert)
                score = self.score_move(new_board, move, my_team_index=abs(my_team_index - 1),
                                        recursion_level=recursion_level+1)
                move_scores.append(score)

            min_max_score = move_scores[0]
            for score in move_scores:
                if my_team_index == 0:
                    if score > min_max_score:
                        # print(score)
                        min_max_score = score
                elif my_team_index == 1:
                    if score < min_max_score:
                        min_max_score = score
                        # print(score)
                else:
                    print('BIG UH OH!')

            return min_max_score

    def find_available_moves(self, board: GameBoard):
        ret = []
        for col in range(board.size[0]):
            for row in range(board.size[0]):
                if board.get_board()[row][col] == ' ':
                    ret.append((row, col))
        return ret



