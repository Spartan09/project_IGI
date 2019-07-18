inputMatrix = [[1,2,3],[5,6,0],[7,8,4]]
outputMatrix = [[1,2,3],[5,8,6],[0,7,4]]

class Astar:
	def __init__(self):
		self.grid = []
		self.flag = ()
		self.gCost = None
		self.hCost = None
		self.fCost = None

	def findHeuristicValue(inputMatrix, outputMatrix):
		h = 0
		for i in range(0, len(inputMatrix)):
			for j in range(0, len(inputMatrix)):
				if inputMatrix[i][j] != outputMatrix[i][j]:
					h += 1
		return h

	#def calFCost(inputMatrix):
	#	return (inputMatrix.gCost + inputMatrix.hCost)

	def findBestMatrix(openList):
		current = []
		currentFCost = float("inf")
		for matrix in openList:
			if matrix.fCost < currentFCost:
				currentFCost = matrix.fCost
		return matrix

	def generateNeighbours(inputMatrix, depth):
		slot = ()
		neighbours = []
		depth = 0
		for i in range(0,len(inputMatrix.grid)):
			for j in range(0,len(inputMatrix.grid)):
				if inputMatrix.grid[i][j] == 0:
					slot = (i,j)
					break
		x,y = slot
		px,py = inputMatrix.flag
		delx = x - px
		dely = y - px
		depth += 1

		
		if delx < 0 and dely == 0:
			if x - 1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x-1][y] = tempMatrixObj[x-1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x-1, y)
				neighbours.append(tempMatrixObj)
			elif y+1 <= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y+1] = tempMatrixObj[x][y+1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y+1)
				neighbours.append(tempMatrixObj)
			elif y-1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y-1] = tempMatrixObj[x][y-1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y-1)
				neighbours.append(tempMatrixObj)

		if delx == 0 and dely < 0:
			if  x-1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x-1][y] = tempMatrixObj[x-1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x-1, y)
				neighbours.append(tempMatrixObj)
			elif x+1 <= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x+1][y] = tempMatrixObj[x+1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x+1, y)
				neighbours.append(tempMatrixObj)
			elif y-1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y-1] = tempMatrixObj[x][y-1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y-1)
				neighbours.append(tempMatrixObj)


		if delx > 0 and dely == 0:
			if 	x+1 >= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x+1][y] = tempMatrixObj[x+1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x+1, y)
				neighbours.append(tempMatrixObj)
			elif y+1 <= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y+1] = tempMatrixObj[x][y+1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y+1)
				neighbours.append(tempMatrixObj)
			elif y-1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y-1] = tempMatrixObj[x][y-1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y-1)
				neighbours.append(tempMatrixObj)


		if delx == 0 and dely > 0:
			if 	x-1 >= 0:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x-1][y] = tempMatrixObj[x-1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x-1, y)
				neighbours.append(tempMatrixObj)
			elif x+1 <= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x+1][y] = tempMatrixObj[x+1][y], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x+1, y)
				neighbours.append(tempMatrixObj)
			elif y+1 >= 2:
				tempMatrixObj = Astar()
				tempMatrixObj.grid = inputMatrix.grid.copy()
				tempMatrixObj[x][y], tempMatrixObj[x][y+1] = tempMatrixObj[x][y+1], tempMatrixObj[x][y]
				tempMatrixObj.flag = (x, y+1)
				neighbours.append(tempMatrixObj)

		for tempMatrixObj in neighbours:
			tempMatrixObj.gCost = depth
			tempMatrixObj.hCost = findHeuristicValue(tempMatrixObj.grid)
			tempMatrixObj.fCost = tempMatrixObj.gCost + tempMatrixObj.hCost

		return neighbours
			
		

	def pathFinder():
		openList = []
		closedList = []
		current = []
		depth = 0
		returnStatement = ()
		inputMatrixObj = Astar()
		inputMatrixObj.grid = inputMatrix
		openList.append(inputMatrixObj)

		while true:
			current = findBestMatrix(openList)
			openList.remove(current)
			closedList.append(current)

			if findHeuristicValue(current.grid) == 0:
				returnStatement(current.grid, current.depth)
				return returnStatement

			if openList is empty:
				return

			for neighbour in generateNeighbours(current):
				if neighbour not in openList:
					openList.append(neighbour)

Astar.pathFinder()	
	

