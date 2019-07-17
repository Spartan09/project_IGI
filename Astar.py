inputMatrix = [[1,2,3],[5,6,0],[7,8,4]]
outputMatrix = [[1,2,3],[5,8,6],[0,7,4]]

class Astar:
	def __init__(self):
		self.gCost = None
		self.hCost = None

	def findHeuristicValue(inputMatrix, outputMatrix):
		h = 0
		for i in range(0, len(inputMatrix)):
			for j in range(0, len(inputMatrix)):
				if inputMatrix[i][j] != outputMatrix[i][j]:
					h += 1
		return h

	findHeuristicValue(inputMatrix, outputMatrix)