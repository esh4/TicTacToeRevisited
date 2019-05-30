import copy

class GameBoard:
    teams = ['X', 'O']

    def __init__(self, preset: list=None, size=(3, 3)):
        self.size = size
        self.__board = [[' ' for x in range(size[0])] for x in range(size[1])]
        if preset:
            self.__board = copy.deepcopy(preset)

    def insert_game_piece(self, locations):
        """
        :param locations: dict {location, team}
        :return:
        """
        new_board = GameBoard(self.get_board())
        # print(locations)
        for key in locations:
            if new_board.get_board()[key[0]][key[1]] not in self.teams:
                new_board.get_board()[key[0]][key[1]] = locations[key]

        return new_board

    def get_board(self):
        return self.__board

    def is_game_over(self):
        """
        check whether the game has ended when-
            * the board is full
            * there are three of the same piece in a row/column/diagonal
        :return: game_over, winner_piece (boolean, str)
        """
        board = self.get_board()

        # TODO: this is crap! these two loops are practically identical
        # identical row
        for row in range(self.size[0]):
            piece = board[0][row]
            in_a_row = 0
            for col in range(self.size[1]):
                if board[col][row] == ' ':
                    break
                elif board[col][row] == piece:
                    in_a_row += 1
            if in_a_row == self.size[0]:
                return True, piece

        # identical column
        for col in range(self.size[0]):
            piece = board[col][0]
            in_a_row = 0
            for row in range(self.size[1]):
                if board[col][row] == ' ':
                    break
                elif board[col][row] == piece:
                    in_a_row += 1
            if in_a_row == self.size[0]:
                return True, piece

        # diagonal
        in_a_row = 0
        piece = board[0][0]
        for i in range(self.size[0]):
            if piece == ' ':
                break
            elif board[i][i] == piece:
                in_a_row += 1
        if in_a_row == self.size[0]:
            return True, piece

        # other diagonal
        in_a_row = 0
        piece = board[2][0]
        for i in range(self.size[0]):
            if piece == ' ':
                break
            elif board[self.size[0] - 1 - i][i] == piece:
                in_a_row += 1
        if in_a_row == self.size[0]:
            return True, piece

        for i in range(self.size[0]):
            for j in range(self.size[0]):
                if board[i][j] == ' ':
                    return False, ' '

        return True, None

    def __repr__(self):
        ret = ''
        for i in range(3):
            ret += str(self.__board[i]) + '\n'
        return ret


