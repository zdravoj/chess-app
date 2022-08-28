# chess-app

From a code-along [on Youtube](https://www.youtube.com/watch?v=OpL0Gcfn4B4) by [Coding Spot](https://www.youtube.com/channel/UCLqXQLK6zKZg0trhanjAkkQ).

[Code Along's chess app tutorial GitHub repo](https://github.com/AlejoG10/python-chess-ai-yt)

## Controls

Use mouse to move pieces.
Press 't' to change theme (green, brown, blue, gray)
Press 'r' to restart the game.

## Install & Running the Game
Entry point is running <span>main.py</span> as a python script. Must have packages in requirements.txt installed locally to run.

## Current Functionality / Bugs
Current build is the base build from the code-along. There are several known bugs in the base functionality.
1. Move logic: Can castle into check (sometimes)
2. Move logic: King can move into check (sometimes)
3. Audio: Both capture and move sounds play upon en passant capture

## Roadmap
Current development plans:
1. Fix known bugs
2. Refactor redundant code
3. Documentation (docstrings, inline comments)
