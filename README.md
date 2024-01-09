# README for Snake Game in Python using Curses

## Introduction
This repository contains a Python implementation of the classic Snake game. It utilizes the `curses` library to create a text-based interface. The game is a simple yet engaging example of using curses for creating interactive applications in a terminal environment.

## Features
- **Text-Based Interface:** The game runs in the terminal, using text characters to represent the snake, food, and game boundaries.
- **Controls:** Players use the arrow keys to control the snake's direction.
- **Dynamic Food Generation:** Food items appear at random positions on the screen.
- **Score Tracking:** The score, based on the length of the snake, is displayed on screen.
- **Game Over Handling:** The game ends when the snake collides with the screen border or itself, displaying a 'Game Over' message.
- **Pause and Exit:** Players can pause the game with the spacebar and exit by pressing 'X'.

## Requirements
- Python 3.x
- A terminal that supports the `curses` library (commonly available in Unix-like systems)

## Installation
1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Usage
Navigate to the cloned repository's directory and run the game using Python:

```bash
python snake_game.py
```

## Controls
- **Arrow Keys:** Move the snake in the respective direction.
- **Spacebar:** Pause and resume the game.
- **X Key:** Exit the game.
