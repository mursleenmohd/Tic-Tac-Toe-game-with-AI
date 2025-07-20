import tkinter as tk
from tkinter import messagebox, ttk
import ai  

# === Main Window Setup ===
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

# Difficulty Selection
difficulty = tk.StringVar(value="Hard")
tk.Label(root, text="AI Difficulty:", font=("Arial", 12)).pack()
ttk.Combobox(root, textvariable=difficulty, values=["Easy", "Medium", "Hard"]).pack(pady=5)

# Center the window
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# === Game Data ===
board = [""] * 9
buttons = []
x_wins = 0
o_wins = 0
draws = 0

# Scoreboard
score_label = tk.Label(root, text="X: 0   O: 0   Draws: 0", font=("Arial", 14))
score_label.pack(pady=5)

#  Background colors
colors = [
    "#FFCDD2", "#F8BBD0", "#E1BEE7",
    "#D1C4E9", "#C5CAE9", "#B2DFDB",
    "#C8E6C9", "#FFF9C4", "#FFE0B2"
]

# Update scoreboard
def update_score(winner):
    global x_wins, o_wins, draws
    if winner == "X":
        x_wins += 1
    elif winner == "O":
        o_wins += 1
    else:
        draws += 1
    score_label.config(text=f"X: {x_wins}   O: {o_wins}   Draws: {draws}")

# Game result popup
def show_result(winner):
    update_score(winner)
    if winner == "X":
        messagebox.showinfo("Game Over", "You win! \nYou're too smart!")
    elif winner == "O":
        messagebox.showinfo("Game Over", "I win! \nBetter luck next time!")
    else:
        messagebox.showinfo("Game Over", "It's a draw! \nWe're equal!")

    for btn in buttons:
        btn.config(state="disabled")

# Reset board
def reset_board():
    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", state="normal")

# Player clicks a button
def on_click(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="❌", state="disabled", disabledforeground="red")

        winner = ai.check_winner(board)
        if winner:
            show_result(winner)
            return

        # AI move
        best_move = ai.get_best_move(board, difficulty.get())
        if best_move is not None:
            board[best_move] = "O"
            buttons[best_move].config(text="⭕", state="disabled", disabledforeground="blue")

            winner = ai.check_winner(board)
            if winner:
                show_result(winner)

# === Board Layout ===
frame = tk.Frame(root)
frame.pack(expand=True)

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 32), width=8, height=3,
                    bg=colors[i], activebackground=colors[i],
                    command=lambda i=i: on_click(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Start the GUI
root.mainloop()
