inputMatrix = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
outputMatrix = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]


class Astar:

	def __init__(self):
		self.grid = []
		self.flag = (-1, -1)
		self.gCost = 0
		self.hCost = 0
		self.fCost = 0


def generateNeighbours(inMatrix):
	slot = ()
	neighbours = []
	for i in range(0, len(inMatrix.grid)):
		for j in range(0, len(inMatrix.grid)):
			if inMatrix.grid[i][j] == 0:
				slot = (i, j)
				break

	x, y = slot
	px, py = inMatrix.flag
	delx = x - px
	dely = y - px

	if px == -1 and py == -1:
		if x - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x - 1][y] = tobj.grid[x - 1][y], tobj.grid[x][y]
			tobj.flag = (x - 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		if x + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x + 1][y] = tobj.grid[x + 1][y], tobj.grid[x][y]
			tobj.flag = (x + 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("-------------------------------------------------check neighbours " + str(
				[x.grid for x in neighbours]))
		if y - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y - 1] = tobj.grid[x][y - 1], tobj.grid[x][y]
			tobj.flag = (x, y - 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("+++++++++++++++++++++++++++++++check neighbours " + str([x.grid for x in neighbours]))
		if y + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y + 1] = tobj.grid[x][y + 1], tobj.grid[x][y]
			tobj.flag = (x, y + 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
	if delx < 0 and dely == 0:
		if x - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x - 1][y] = tobj.grid[x - 1][y], tobj.grid[x][y]
			tobj.flag = (x - 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))

		elif y + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y + 1] = tobj.grid[x][y + 1], tobj.grid[x][y]
			tobj.flag = (x, y + 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif y - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y - 1] = tobj.grid[x][y - 1], tobj.grid[x][y]
			tobj.flag = (x, y - 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))

	if delx == 0 and dely < 0:
		if x - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x - 1][y] = tobj.grid[x - 1][y], tobj.grid[x][y]
			tobj.flag = (x - 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif x + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x + 1][y] = tobj.grid[x + 1][y], tobj.grid[x][y]
			tobj.flag = (x + 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif y - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y - 1] = tobj.grid[x][y - 1], tobj.grid[x][y]
			tobj.flag = (x, y - 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))

	if delx > 0 and dely == 0:
		if x + 1 >= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x + 1][y] = tobj.grid[x + 1][y], tobj.grid[x][y]
			tobj.flag = (x + 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif y + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y + 1] = tobj.grid[x][y + 1], tobj.grid[x][y]
			tobj.flag = (x, y + 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif y - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y - 1] = tobj.grid[x][y - 1], tobj.grid[x][y]
			tobj.flag = (x, y - 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))

	if delx == 0 and dely > 0:
		if x - 1 >= 0:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x - 1][y] = tobj.grid[x - 1][y], tobj.grid[x][y]
			tobj.flag = (x - 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif x + 1 <= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x + 1][y] = tobj.grid[x + 1][y], tobj.grid[x][y]
			tobj.flag = (x + 1, y)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))
		elif y + 1 >= 2:
			tobj = Astar()
			tobj.grid = inMatrix.grid.copy()
			tobj.grid[x][y], tobj.grid[x][y + 1] = tobj.grid[x][y + 1], tobj.grid[x][y]
			tobj.flag = (x, y + 1)
			tobj.gCost += 1
			tobj.hCost = findHeuristicValue(tobj.grid)
			tobj.fCost = tobj.gCost + tobj.hCost
			neighbours.append(tobj)
			print("check neighbours " + str([x.grid for x in neighbours]))

	print("check neighbours " + str([x.grid for x in neighbours]))
	return neighbours


def findHeuristicValue(inMatrix):
	h = 0
	for i in range(0, len(inMatrix)):
		for j in range(0, len(inMatrix)):
			if inMatrix[i][j] != outputMatrix[i][j]:
				h += 1
	print("check hval " + str(h))
	return h


def findBestMatrix(current, openList):
	currentfcost = current.fCost
	flag = True
	for matrix in openList:
		if matrix.fCost < currentfcost:
			currentfcost = matrix.fCost
			flag = False
			print("inside best if " + str(matrix.fCost))
		print("outside best if " + str(current.grid))
	if not flag:
		return matrix
	else:
		return current


def pathFinder():
	openList = []
	closedList = []
	current = Astar()
	current.grid = inputMatrix
	openList.append(current)
	checklist = [x.grid for x in openList]
	print(checklist)
	while True:
		current = findBestMatrix(current, openList)
		print("-----before---rem" + str(current.grid))
		openList.remove(current)
		print("-----after---rem" + str(current.grid))
		closedList.append(current)

		if findHeuristicValue(current.grid) == 0:
			returnStatement = (current.grid, current.gCost)
			return returnStatement
		print("-----before---nhb" + str(current.grid))
		neighbourList = generateNeighbours(current)
		print("--nhb list---" + str(neighbourList))
		for neighbour in neighbourList:
			if neighbour not in openList:
				openList.append(neighbour)
		print("-----after---nhb" + str(current.grid))


print(pathFinder())
