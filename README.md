# A* Pathfinding

A* pathfinding algorithm using Pygame

![](.pathfinding.gif)

## Install Pygame

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame

```bash
python3 -m pip install -U pygame --user
```

## Run
```bash
python main.py
```
## Controls

LeftMouse - select starting point

RightMouse - select ending point

Space - blank grid

R - randomize grid with obstacles

Enter/Return - start algorithm if both start and end point have been selected
## Settings
Change these settings in info.py
```python
# Change density of grid, should be between 0 and 1
OBSTACLE = 0.5
# Change to switch between Manhattan distance and Euclidian Distance
TAXI = False
# Change FPS to change speed of program
FPS = 100
```
