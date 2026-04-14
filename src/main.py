from grid import Grid
from astar import astar
from visualize import show_path
from yolo_detection import run_yolo   # ✅ NEW

# Run YOLO detection first
run_yolo()   # ✅ NEW

grid = Grid(20, 20)
start = (0, 0)
goal = (19, 19)

path = astar(grid, start, goal)

show_path(grid, path, start, goal)