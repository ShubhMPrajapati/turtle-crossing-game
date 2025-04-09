# Turtle Race Game

This is a simple racing game built using Python's `turtle` module. The game features a player (represented by a turtle) that must navigate through a series of moving cars. The player wins by reaching the finish line while avoiding collisions with the cars. The game keeps track of the player's level, increasing as they successfully cross the finish line without getting hit.

## Features:
- **Player Movement**: The player can move the turtle upward using the "Up" arrow key.
- **Car Movement**: Cars move from right to left at random speeds, with different colors and positions on the screen.
- **Leveling System**: Every time the player reaches the finish line, their level increases, and the game speed (car movement) becomes faster.
- **Collision Detection**: The game ends when the player collides with a car, and a "GAME OVER" message is displayed.
- **Score Display**: The player's current level is displayed at the top of the screen.

## How to Play:
1. Run the script to start the game.
2. Use the "Up" arrow key to move the turtle upwards.
3. Avoid getting hit by the cars.
4. Reach the finish line to level up.
5. The game ends if you collide with a car.

## Files:
- **player.py**: Contains the `Player` class responsible for the player's turtle character.
- **car_manager.py**: Contains the `CarManager` class responsible for creating and moving the cars.
- **scoreboard.py**: Contains the `Scoreboard` class responsible for displaying and updating the player's level.
- **main.py**: The main script that runs the game and manages the game loop.

## Setup:
1. Install Python (version 3.x).
2. Install the `turtle` module (it comes pre-installed with Python).
3. Clone or download the repository.
4. Run `main.py` to start the game.

```bash
python main.py
