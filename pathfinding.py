from info import TAXI

def findPath(openSet, closedSet, maze, end):
	current = openSet[0]
	# Find node with lowest f
	for node in openSet:
		if node.f < current.f:
			current = node
	# Remove from openSet and add to closedSet
	openSet.remove(current)
	closedSet.append(current)
	# Stop if end node has been found
	if current.pos == end:
		return current
	# check all neigbouring nodes to see which to add to openSet
	for neighbour in current.getNeighbours(maze):
		# If taxi distance is active, only look at adjacent neighbours
		if TAXI and current.getG(neighbour.pos) != 1:
			continue
		# Make sure node wasn't already visited
		if neighbour not in closedSet:
			g = current.g + current.getG(neighbour.pos)
			if neighbour not in openSet:
				neighbour.update(g, end, current)
				openSet.append(neighbour)
			else:
				# Update node in openSet because better g was found
				if g < node.g:
					neighbour.update(g, end, current)
	return None