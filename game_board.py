class Games:
    def __init__(self, size):
        self.size = size

    def board_width(self):
        print(self.size * " ---")

    def board_row(self):
        print((self.size + 1) * "|   ")

    def game_board(self):
        for i in range(self.size):
            Games.board_width(self)
            Games.board_row(self)
        Games.board_width(self)


if __name__ == "__main__":
    gbs = Games(int(input("Please enter the board number: ")))
    gbs.game_board()
