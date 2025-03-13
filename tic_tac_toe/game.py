class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_winner = None

    def make_move(self, position, player):
        """Marks the player's move"""
        if self.board[position] == " ":
            self.board[position] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        """Checks for a winning condition"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def available_moves(self):
        """Returns available move positions"""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def is_full(self):
        """Checks if the board is full"""
        return " " not in self.board
