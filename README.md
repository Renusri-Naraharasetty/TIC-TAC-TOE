# 🎮 Rolling Tic Tac Toe (GUI Edition)

A fun spin on the classic Tic Tac Toe game implemented using Python's `tkinter` library. This one includes an innovative **"rolling move"** feature—players can only maintain three moves on the board at any given time, resulting in an ever-hungry and strategic game!

> 💡 No tie games here! The first player to align three of their moves wins, and the oldest move gets removed after each new one.

---

## ✨ Features

- 🟪 **Purple Neon Theme**: Simple, eye-pleasant UI with sleek colors.
- 🔁 **Rolling Game Logic**: Continues the game in motion with no ties.
- 🧠 **Single Player (Pass & Play)**: Ideal for two players using one screen.
- 🖱️ **GUI Simple**: Implemented using `tkinter` for quick setup and simple interaction.
- 🎉 **Win Popup**: Flashy popup announces the winner with a play-again option.

---

## 📸 Preview

 ![image](https://github.com/user-attachments/assets/fe22c26b-6d07-4824-a3ed-5fd8342c09fb)
 
---

## 🚀 How to Run

### Requirements
- Python 3.x installed
- No external libraries needed (uses built-in `tkinter`)

### Steps

1. Clone or download this repository.
2. Ensure `main.py` is in your project directory.
3. Run the script:
- Using **IDLE**: Open `main.py`, press `F5`.
- Using **VS Code**: Open the folder, then `Run > Run Without Debugging`.

---

## 🧠 How It Works

### 🎲 Rolling Logic
- Each player can only have **3 active moves** at a time.
- If a 4th move is added, the **oldest move is discarded**.
- This avoids ties and maintains the game's dynamic nature.

### 🧩 Win Check
- At every move, the game checks if the current player has a straight line (horizontal, vertical, diagonal).
- If a win is found, a **popup appears** with a reset option.

### 💻 GUI Layout
- **3x3 Button Grid**: Board representation.
- **Label**: Displays whose turn it is.
- **Reset Button**: Resumes a new game at any time.
- **Popup Window**: Animated alert when somebody wins.

---

## 📁 Project Structure

RollingTicTacToe/

├── main.py       # Main game script

└── README.md     # Project description


---

## 🎯 Customization Ideas

- Incorporate sound effects through `pygame` or `playsound`
- Incorporate animations for moves
- Develop a multiplayer (online) version
- Extend to 4x4 or 5x5 dynamic boards

---

## Sample Output 

![image](https://github.com/user-attachments/assets/7f2073a6-205c-467a-b07c-3c0245b35855)

---

## 🧑‍🎓 Made For

This project was created as part of a **Python mini project** for academic submission. Fork, change, or extend it for your learning or enjoyment!

---

Happy gaming and keep coding! 😄



