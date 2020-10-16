import pygame
import sys
from info import GRIDSIZE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, LEFT_CLICK, RIGHT_CLICK, OBSTACLE
from settings import Settings
from draw import drawGrid, updateGrid, drawPath
from pathfinding import findPath

def handleKeys(settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		elif settings.running:
			return
		elif event.type == pygame.KEYDOWN:
			# Start game with enter if start and end have been placed
			if event.key == pygame.K_RETURN and settings.start and settings.end:
				settings.running = True
			elif event.key == ord('r'):
				settings.initMaze(OBSTACLE)
				settings.update = True
			elif event.key == pygame.K_SPACE:
				settings.initMaze()
				settings.update = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pressed = pygame.mouse.get_pressed()
			if pressed == LEFT_CLICK:
				x, y = pygame.mouse.get_pos()
				point = (x//GRIDSIZE, y//GRIDSIZE)
				if point != settings.end and not settings.maze[point[0]][point[1]].obstacle:
					settings.start = point
					settings.update = True
			elif pressed == RIGHT_CLICK:
				x, y = pygame.mouse.get_pos()
				point = (x//GRIDSIZE, y//GRIDSIZE)
				if point != settings.start and not settings.maze[point[0]][point[1]].obstacle:
					settings.end = point
					settings.update = True
	if settings.update:
		settings.reset()


# Initiate Pygame
def initPygame():
	pygame.init()
	pygame.display.set_caption("A* Pathfinding")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	surface = pygame.Surface(screen.get_size())
	surface = surface.convert()
	return surface, screen


def main():
	# Create settings
	surface, screen = initPygame()
	settings = Settings(surface, screen)
	# Initiate empty maze
	settings.initMaze()
	
	clock = pygame.time.Clock()

	# Start mainloop
	while True:
		clock.tick(FPS)
		handleKeys(settings)
		if settings.update:
			drawGrid(settings.surface, settings.maze, settings.start, settings.end)
			settings.update = False
		# If pathfiniding has started and path has not been found yet
		if settings.running and not settings.pathFound:
			# Draw open and closed sets on grid
			updateGrid(settings.surface, settings.openSet, settings.closedSet, settings.start, settings.end)
			# Put start node into openSet
			if settings.init:
				settings.init = False
				x, y = settings.start
				settings.openSet.append(settings.maze[x][y])
			# If openSet is empty no path was found
			if len(settings.openSet):
				settings.pathFound = findPath(settings.openSet, settings.closedSet, settings.maze, settings.end)
			else:
				settings.running = False
		# Draw found path
		elif settings.pathFound and settings.running:
			drawPath(settings.surface, settings.pathFound)
			settings.running = False

		settings.screen.blit(settings.surface, (0,0))
		pygame.display.update()


main()
