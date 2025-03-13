import tkinter as tk
from tic_tac_toe.config import API_KEY
from tic_tac_toe.gui import TicTacToeGUI  
print(f"Using API Key: {API_KEY}")
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()