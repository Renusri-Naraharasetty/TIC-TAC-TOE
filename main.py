import tkinter as tk
from tkinter import Toplevel

# Theme Colors
bg_color = "#1e1e2f"
cell_bg = "#2a2a3d"
cell_click_bg = "#3d3d5c"
text_color = "#d9a7ff"

# Game State
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
moves_X = []
moves_O = []

# Place move
def place_move(row, col):
    global current_player

    if board[row][col] != '':
        return

    # Rolling move logic
    if current_player == 'X':
        if len(moves_X) == 3:
            old_row, old_col = moves_X.pop(0)
            board[old_row][old_col] = ''
            buttons[old_row][old_col].config(text='', bg=cell_bg)
        moves_X.append((row, col))
    else:
        if len(moves_O) == 3:
            old_row, old_col = moves_O.pop(0)
            board[old_row][old_col] = ''
            buttons[old_row][old_col].config(text='', bg=cell_bg)
        moves_O.append((row, col))

    board[row][col] = current_player
    buttons[row][col].config(text=current_player, fg=text_color, bg=cell_click_bg)

    if check_win(current_player):
        show_popup(f"🎉 Player {current_player} Wins! 🎉")
        return

    current_player = 'O' if current_player == 'X' else 'X'
    label.config(text=f"Player {current_player}'s Turn", fg=text_color)

# Check win condition
def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Reset the game
def reset_board():
    global board, moves_X, moves_O, current_player
    board = [['' for _ in range(3)] for _ in range(3)]
    moves_X.clear()
    moves_O.clear()
    current_player = 'X'
    label.config(text="Player X's Turn", fg=text_color)
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', bg=cell_bg)

# Animated popup for win
def show_popup(message):
    popup = Toplevel(window)
    popup.title("🎊 Game Over")
    popup.geometry("300x120")
    popup.config(bg=bg_color)
    popup.attributes('-topmost', True)

    popup_label = tk.Label(popup, text=message, font=('Consolas', 14, 'bold'),
                           fg=text_color, bg=bg_color)
    popup_label.pack(pady=20)

    close_btn = tk.Button(popup, text="Play Again", command=lambda: [popup.destroy(), reset_board()],
                          bg=cell_click_bg, fg='white')
    close_btn.pack(pady=5)

# GUI setup
window = tk.Tk()
window.title("Rolling Tic Tac Toe - Purple Neon")
window.geometry("400x480")
window.resizable(False, False)
window.configure(bg=bg_color)

label = tk.Label(window, text="Player X's Turn", font=('Consolas', 16, 'bold'),
                 bg=bg_color, fg=text_color)
label.pack(pady=10)

frame = tk.Frame(window, bg=bg_color)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text='', font=('Consolas', 22, 'bold'),
                                  width=5, height=2, bg=cell_bg, fg='white',
                                  activebackground=cell_click_bg,
                                  command=lambda i=i, j=j: place_move(i, j))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_btn = tk.Button(window, text="Reset Game", font=('Consolas', 13),
                      command=reset_board, bg="#444", fg="white",
                      activebackground="#666")
reset_btn.pack(pady=10)

window.mainloop()
