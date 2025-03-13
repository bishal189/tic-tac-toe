import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        # Game state variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.x_score = 0
        self.y_score = 0
        self.game_active = True
        
        # Create frame for game board
        self.game_frame = tk.Frame(root)
        self.game_frame.pack(pady=10)
        
        # Create buttons for the game board
        self.buttons = [[tk.Button(self.game_frame, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda r=r, c=c: self.make_move(r, c))
                        for c in range(3)] for r in range(3)]
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)
        
        # Create status frame
        self.status_frame = tk.Frame(root)
        self.status_frame.pack(fill=tk.X, pady=10)
        
        # Player turn indicator
        self.status_label = tk.Label(self.status_frame, text="Player X's turn", font=("Arial", 12))
        self.status_label.pack()
        
        # Create score frame
        self.score_frame = tk.Frame(root)
        self.score_frame.pack(fill=tk.X, pady=5)
        
        # Score display
        self.score_x_label = tk.Label(self.score_frame, text="Player X: 0", font=("Arial", 12))
        self.score_x_label.pack(side=tk.LEFT, padx=20)
        
        self.score_o_label = tk.Label(self.score_frame, text="Player O: 0", font=("Arial", 12))
        self.score_o_label.pack(side=tk.RIGHT, padx=20)
        
        # Create control frame for buttons
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)
        
        # Reset Button
        self.reset_button = tk.Button(self.control_frame, text="Reset Game", font=("Arial", 12), 
                                     command=self.reset_board, bg="red", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # New Game Button
        self.new_game_button = tk.Button(self.control_frame, text="New Game", font=("Arial", 12),
                                        command=self.new_game, bg="green", fg="white")
        self.new_game_button.pack(side=tk.LEFT, padx=5)
        
        # Settings Button
        self.settings_button = tk.Button(self.control_frame, text="Settings", font=("Arial", 12),
                                        command=self.open_settings, bg="blue", fg="white")
        self.settings_button.pack(side=tk.LEFT, padx=5)
        
        # Exit Button
        self.exit_button = tk.Button(self.control_frame, text="Exit", font=("Arial", 12),
                                    command=root.destroy, bg="gray", fg="white")
        self.exit_button.pack(side=tk.LEFT, padx=5)
    
    def make_move(self, row, col):
        if not self.game_active:
            return
            
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.current_player == "X":
                self.buttons[row][col].config(fg="blue")
            else:
                self.buttons[row][col].config(fg="red")
                
            if self.check_winner():
                self.game_active = False
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.update_score()
                return
            elif self.check_draw():
                self.game_active = False
                messagebox.showinfo("Game Over", "It's a draw!")
                return
                
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
            
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def update_score(self):
        if self.current_player == "X":
            self.x_score += 1
            self.score_x_label.config(text=f"Player X: {self.x_score}")
        else:
            self.y_score += 1
            self.score_o_label.config(text=f"Player O: {self.y_score}")
    
    def reset_board(self):
        """Clears the board and resets the game."""
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_active = True
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", fg="black")
        
        self.status_label.config(text="Player X's turn")
    
    def new_game(self):
        """Starts a completely new game with reset scores."""
        self.reset_board()
        self.x_score = 0
        self.y_score = 0
        self.score_x_label.config(text="Player X: 0")
        self.score_o_label.config(text="Player O: 0")
    
    def open_settings(self):
        """Opens a settings dialog."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        
        # Add some sample settings
        tk.Label(settings_window, text="Game Settings", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Player X color setting
        x_color_frame = tk.Frame(settings_window)
        x_color_frame.pack(fill=tk.X, pady=5)
        tk.Label(x_color_frame, text="Player X Color:").pack(side=tk.LEFT, padx=10)
        x_color_btn = tk.Button(x_color_frame, text="Blue", bg="blue", fg="white", 
                               width=10, command=lambda: self.change_color("X"))
        x_color_btn.pack(side=tk.RIGHT, padx=10)
        
        # Player O color setting
        o_color_frame = tk.Frame(settings_window)
        o_color_frame.pack(fill=tk.X, pady=5)
        tk.Label(o_color_frame, text="Player O Color:").pack(side=tk.LEFT, padx=10)
        o_color_btn = tk.Button(o_color_frame, text="Red", bg="red", fg="white", 
                               width=10, command=lambda: self.change_color("O"))
        o_color_btn.pack(side=tk.RIGHT, padx=10)
        
        # Close button
        tk.Button(settings_window, text="Close", command=settings_window.destroy).pack(pady=20)
    
    def change_color(self, player):
        """Placeholder for color change functionality."""
        messagebox.showinfo("Color Change", f"Color settings for Player {player} would change here")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()