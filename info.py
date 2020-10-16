# Change OBSTACLE density, should be between 0 and 1
OBSTACLE = 0.5
# Change to True if you want Taxi Distance instead of Euclidian Distance
TAXI = False
# Lower FPS to go slower
FPS = 100


# -----------------
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

GRIDSIZE = 10
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

RIGHT_CLICK = (False, False, True, False, False)
LEFT_CLICK = (True, False, False, False, False)

UP = (0, -1)
UPRIGHT = (1, -1)
UPLEFT = (-1, -1)
DOWN = (0, 1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (-1, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT, LEFT, UPLEFT]

BLACK = (0,0,0)
WHITE = (255,255,255)
BG = (210,200,200)
RED = (150,0,0)
GREEN = (0,150,0)
BLUE = (0,0,100)
PATH = (50,50,200)
OPENSET = (255,180,100)
CLOSEDSET = (255,100,100)