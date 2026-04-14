import random

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.add_obstacles()

    def add_obstacles(self):
        for _ in range(60):
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.cols-1)
            self.grid[x][y] = 1

    def is_obstacle(self, node):
        x, y = node
        return self.grid[x][y] == 1
