class searchPaths():
    def __init__(self, vector):
        # Initialize the Pathfinder object
        self.vector = vector
        self.paths = []

    def findAllPaths(self, position, solution):
        # Recursively explore the possible paths and store valid paths
        # This method will not be tested, so you can modify the parameters as needed
        if position == 0:
            queue = [[position]]
        while queue != []:
            path = queue.pop(0)
            vector = path[-1]
            if vector not in path[0:len(path)-1]: 
                neighbors = self.findAllNeighbors(vector, path[0:len(path)-1])
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    if neighbor == len(self.vector)-1:
                        self.paths.append(new_path)
                        solution = solution+1
                    else:
                        queue.append(new_path)
        pass

    def findAllNeighbors(self, position, explored):
        neighbors = []
        if position + self.vector[position] <= len(self.vector)-1:
            if position + self.vector[position] not in explored:
                neighbors.append(position+self.vector[position])
            
        if position - self.vector[position] >= 0:
            if position - self.vector[position] not in explored:
                neighbors.append(position-self.vector[position])
        return neighbors
        pass

    def getPaths(self):
        # Return the list of viable paths, or [None] if there are no solutions
        self.findAllPaths(0, 0)
        return self.paths
        pass

# The searchPaths class is initialized with a list of integers, the target of which is the position with value 0.
# The findAllPaths method recursively explores the list.
# The getPaths method returns the list of viable paths, or [None] if there are no solutions

# Similar to A* or Dijkstra's

