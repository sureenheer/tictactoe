class Game:
    def __init__(self):
        self.board = [["-", "-", "-"], ['-', '-', '-'], ['-', '-', '-']]
        self.current_player = 'X'
        self.remaining_moves = 9
        self.game_finished = False

    def check_win(self, x, y):
        marker = self.board[x][y]
        # check for horizontal match
        if self.board[x][0] == marker and self.board[x][1] == marker and self.board[x][2] == marker:
            return True
        # check for vertical match
        elif self.board[0][y] == marker and self.board[1][y] == marker and self.board[2][y] == marker:
            return True
        # check for diagonal match
        elif x == y:
            if self.board[0][0] == marker and self.board[1][1] == marker and self.board[2][2] == marker:
                return True
        elif (x == 0 and y == 2) or (x == 2 and y == 0) or (x == 1 and y == 1):
            if self.board[2][0] == marker and self.board[1][1] == marker and self.board[0][2] == marker:
                return True
        else:
            return False

    def check_tie(self, player_won):
        if self.game_finished and not player_won:
            return True
        else:
            return False

    def make_move(self, x, y):
        if self.game_finished:
            return False, "Game is finished."
        if self.board[x][y] == '-':
            self.board[x][y] = self.current_player
            print(f'Player {self.current_player} made a move.')
            self.remaining_moves -= 1
            if self.remaining_moves == 0:
                self.game_finished = True
            player_won = self.check_win(x, y)
            if player_won:
              return False, f'Player {self.current_player} won!'
            elif self.check_tie(player_won):
              return False, "The players tied!"
            else:
              if self.current_player == 'X':
                self.current_player = "O"
              elif self.current_player == "O":
                self.current_player = "X"
              return True, None
        else:
            return False, "Invalid move."

    def reset(self):
        self.__init__()
