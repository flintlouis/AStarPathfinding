from node import Node
from info import GRID_HEIGHT, GRID_WIDTH

class Settings(object):
	def __init__(self, surface, screen):
		self.reset()
		self.surface = surface
		self.screen = screen
		self.start = None
		self.end = None
		self.update = True

	def reset(self):
		self.running = False
		self.init = True
		self.pathFound = None
		self.openSet = []
		self.closedSet = []

	def initMaze(self, obstacle=0):
		self.maze = [[Node((x,y), obstacle) for y in range(int(GRID_HEIGHT))] for x in range(int(GRID_WIDTH))]
		if self.start:
			x, y = self.start
			self.maze[x][y].obstacle = False
		if self.end:
			x, y = self.end
			self.maze[x][y].obstacle = False

