# 🧠 Sudoku - Python Backtracking GUI Game

Welcome to the **Sudoku** project — a PyGame-based Sudoku puzzle generator and solver using backtracking, designed with a user-friendly GUI.

---

## 🎯 Features

- ✅ **Random Puzzle Generation** every run (guaranteed solvable)
- 🎮 **GUI built with `pygame`**
- ✍️ Click cells to input numbers
- 🧠 **Backtracking Solver** (Press `S`)
- 🧪 **Check Your Solution** (Press `C`)
- 🔄 Generate a new puzzle anytime (Press `N`)
- ✅ Visual validation ("Correct"/"Incorrect" popup)
- 👀 Clean, legible fonts and layout

---

## 🖼️ Proof of Functionality

Screenshots stored in the [`img/`](img/) folder:

- Puzzle screen with inputs
- Solved board display
- Correctness check message

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| S   | Auto-solve puzzle |
| C   | Check current input |
| N   | New puzzle |
| Q   | Quit the game |

Click on a cell and type digits `1-9` to manually play.

---

## 📁 Project Structure

```
Sudoku/
├── img/                # Screenshots folder
├── Sudoku.py           # Main game file
├── README.md           # Project description
└── LICENSE
```

---

## 🧠 Algorithm Used

This game uses a **recursive backtracking** algorithm that:

1. Fills the board with a complete valid solution
2. Removes a number of cells to create a playable puzzle
3. Solves the puzzle again using the same logic to ensure uniqueness

---

## 📌 Requirements

- Python 3.6+
- `pygame` (`pip install pygame`)

---

## 🚀 Run the Game

```bash
python3 Sudoku.py
```

Make sure your terminal has access to GUI display (macOS/Linux may require permissions).

---

## 🛠️ Dev Info

Created by [CodesBySanjay](https://github.com/CodesBySanjay) 🎓  
Project Branch: `Sudoku` in [Python Repo](https://github.com/CodesBySanjay/Python)

---

## 🕹️ More Projects Coming Soon

Each will have its own dedicated branch and README.
