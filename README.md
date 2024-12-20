Unbeatable Tic-Tac-Toe
This is a Python implementation of Tic-Tac-Toe, featuring an unbeatable AI powered by the Minimax algorithm. The AI starts first and ensures that it either wins or draws every game.

Features
Unbeatable AI: The AI always makes the optimal move using the Minimax algorithm.
Enhanced Visuals: The game board is displayed with clear labels for rows (A, B, C) and columns (1, 2, 3) for intuitive interaction.
Player-Friendly Input: Players input moves using a chess-like format (e.g., A1, B3).
AI First-Move Advantage: The AI always makes the first move.
How to Play
Clone this repository or copy the Python script into your local environment.
Run the script using Python:
bash
Copy code
python tic_tac_toe.py
The AI will make the first move.
To make your move, enter a position using the format <row><column>:
For example:
A1 for the top-left corner
B3 for the middle-right position
The game will announce the result when it's over:
Win (Player or AI)
Draw
Rules
The board is a 3x3 grid labeled as follows:

lua
Copy code
     1   2   3
  -------------
A |   |   |   |
  -------------
B |   |   |   |
  -------------
C |   |   |   |
  -------------
The player is X, and the AI is O.

Players alternate turns, starting with the AI.

The goal is to align three of your symbols (horizontally, vertically, or diagonally).

Example Game
Starting Board:
lua
Copy code
     1   2   3
   -------------
 A |   |   |   |
   -------------
 B |   |   |   |
   -------------
 C |   |   |   |
   -------------
AI moves first: O is placed.
Player moves next: Enter B2 to place X in the middle of the board.
Final Board (AI Wins):
lua
Copy code
     1   2   3
   -------------
 A | O | O | O |
   -------------
 B |   | X |   |
   -------------
 C |   |   | X |
   -------------
Technology Stack
Language: Python 3.x
How It Works
The AI uses the Minimax algorithm to evaluate all possible game states and chooses the move with the highest probability of winning (or drawing).
The player interacts with the game through text-based input.
Future Improvements
Add a graphical user interface (GUI) for a better user experience.
Support multiplayer mode.
Add difficulty levels by tweaking the AI's decision-making.
License
This project is open-source and free to use. Feel free to fork, modify, and share!

[Watch the demo here]([https://www.youtube.com/watch?v=LXDJ7LZ5PhI])


