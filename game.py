class Game:
    def __init__(self):
        self.board = [["-", "-", "-"], ['-', '-', '-'], ['-', '-', '-']]
        self.spots_taken = []
        self.current_player = 1
        self.remaining_moves = 9
        self.error_messages = ["Please enter two coordinates only.", "Invalid coordinates", "This spot is already marked."]
        self.game_finished = False
        print("Board initialized.")

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
        if self.remaining_moves == 0 and not player_won:
            return True
        else:
            return False

    def make_move(self, x, y):
        if self.current_player == 1:
            self.board[x][y] = 'X'
        elif self.current_player == 2:
            self.board[x][y] = 'O'
        self.spots_taken.append([x, y])
        print(f'Player {self.current_player} made a move.')
        self.remaining_moves -= 1
        player_won = self.check_win(x, y)
        if player_won:
            print(f'Player {self.current_player} won!')
            self.game_finished = True
            return
        elif self.check_tie(player_won):
            print("The players tied!")
            self.game_finished = True
            return
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1

    def display_board(self):
        print(f'{self.board[0]} \n')
        print(f'{self.board[1]} \n')
        print(f'{self.board[2]} \n')

    def process_coordinates(self, text):
        text = text.strip()
        coordinates = text.split(",")
        if len(coordinates) == 2:
            # check if valid
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            x = coordinates[0]
            y = coordinates[1]
            if 0 <= x < 3 and 0 <= y < 3:
                # check if not taken
                if [x, y] not in self.spots_taken:
                    return x, y
                else:
                    print(self.error_messages[2])
            else:
                print(self.error_messages[1])
        else:
            print(self.error_messages[0])
        return None

    def get_coordinates(self):
        while True:
            text = input("Please enter the x and y coordinates of where you would like to place your marker. Ex. 1, 1 (this would be the center)\n")
            output = self.process_coordinates(text)
            if output:
                return output

    def play(self):
        while not self.game_finished:
            self.display_board()
            x, y = self.get_coordinates()
            self.make_move(x, y)

    def reset(self):
        self.__init__()

def main():
    game = Game()
    while True:
        game.play()
        text = input("Do you want to play again? Y/N \n")
        text = text.strip().lower()
        if text == "n":
            break
        game.reset()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()


