# Asteroids Game

## Overview
A classic Asteroids arcade game built with Python and Pygame. Players control a spaceship, shoot asteroids to score points, and avoid collisions.

## Project Structure
- `main.py` - Main game entry point with game loop
- `main_web.py` - Web-compatible version using asyncio
- `player.py` - Player spaceship class
- `asteroid.py` - Asteroid entity class
- `asteroidfield.py` - Asteroid spawning manager
- `shot.py` - Projectile class
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game configuration (screen size, speeds, etc.)
- `logger.py` - Game state logging
- `logger_web.py` - Web version logging

## Running the Game
The game runs as a desktop application using VNC output:
```bash
python main.py
```

## Controls
- Arrow keys or WASD to move
- Space to shoot
- ESC to quit

## Scoring
- Large asteroids: 20 points
- Medium asteroids: 50 points
- Small asteroids: 100 points

## Dependencies
- Python 3.11+
- pygame 2.6.1
