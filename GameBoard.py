class GameBoard:
    teams = ['X', 'O']

    def __init__(self, preset=None):
        self.board = [[' ' for x in range(3)] for x in range(3)]
        if preset:
            self.board = preset.copy()

    def make_move(self, locations):
        """
        :param locations: dict {location, team}
        :return:
        """
        for key in locations:
            if self.board[key[0]][key[1]] not in self.teams:
                self.board[key[0]][key[1]] = locations[key]

        return GameBoard(self.board)

    def is_game_over(self):
        pass

    def get_board(self):
        return self.board

    def __repr__(self):
        ret = ''
        for i in range(3):
            ret += str(self.board[i]) + '\n'
        return ret


