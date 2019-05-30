class GameBoard:
    teams = ['X', 'O']

    def __init__(self, preset=None, size=(3, 3)):
        self.size = size
        self.board = [[' ' for x in range(size[0])] for x in range(size[1])]
        if preset:
            self.board = preset.copy()

    def insert_game_piece(self, locations):
        """
        :param locations: dict {location, team}
        :return:
        """
        for key in locations:
            if self.board[key[0]][key[1]] not in self.teams:
                self.board[key[0]][key[1]] = locations[key]

        return GameBoard(self.board)

    def get_board(self):
        return self.board

    def is_game_over(self):
        """
        check whether the game has ended when-
            * the board is full
            * there are three of the same piece in a row/column/diagonal
        :return: game_over, winner_piece (boolean, str)
        """
        board = self.get_board()

        # TODO: this is crap! these two loops are practically identical
        for col in range(self.size[0]):
            piece = board[0][col]
            in_a_row = 0
            for row in range(self.size[1]):
                if board[row][col] == ' ':
                    break
                elif board[row][col] == piece:
                    in_a_row += 1
            if in_a_row == self.size[0]:
                return True, piece

        for row in range(self.size[0]):
            piece = board[row][0]
            in_a_row = 0
            for col in range(self.size[1]):
                if board[row][col] == ' ':
                    break
                elif board[row][col] == piece:
                    in_a_row += 1
            if in_a_row == self.size[0]:
                return True, piece

        return False, None

    def __repr__(self):
        ret = ''
        for i in range(3):
            ret += str(self.board[i]) + '\n'
        return ret


