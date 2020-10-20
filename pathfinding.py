def findPath(openSet, closedSet, maze, end, taxi):
	currentF = -1
	# Find node with lowest f
	for node in openSet:
		if currentF == -1:
			current = node
			currentF = node.f
		elif node.f < currentF:
			current = node
			currentF = node.f
	# Remove from openSet and add to closedSet
	openSet.remove(current)
	closedSet.add(current)
	# Stop if end node has been found
	if current.pos == end:
		return current
	# check all neigbouring nodes to see which to add to openSet
	for neighbour in current.getNeighbours(maze):
		# If taxi distance is active, only look at adjacent neighbours
		if taxi and current.getG(neighbour.pos) != 1:
			continue
		# Make sure node wasn't already visited
		if neighbour not in closedSet:
			g = current.g + current.getG(neighbour.pos)
			if neighbour not in openSet:
				neighbour.update(g, end, current, taxi)
				openSet.add(neighbour)
			else:
				# Update node in openSet because better g was found
				if g < node.g:
					neighbour.update(g, end, current, taxi)
	return None